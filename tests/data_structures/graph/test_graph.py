import io
import sys
from unittest.mock import patch

import pytest

from src.data_structures.graph.graph import Graph


class TestGraphCreation:
    def test_graph_creation_basic(self):
        graph = Graph(5)
        assert graph.num_nodes == 5
        assert graph.size() == 5
        assert len(graph.adjacency_matrix) == 5
        assert len(graph.adjacency_matrix[0]) == 5

    def test_graph_creation_single_node(self):
        graph = Graph(1)
        assert graph.num_nodes == 1
        assert graph.size() == 1
        assert graph.adjacency_matrix == [[0]]

    def test_graph_creation_zero_nodes(self):
        graph = Graph(0)
        assert graph.num_nodes == 0
        assert graph.size() == 0
        assert graph.adjacency_matrix == []

    def test_graph_creation_large(self):
        graph = Graph(100)
        assert graph.num_nodes == 100
        assert graph.size() == 100
        assert len(graph.adjacency_matrix) == 100
        assert len(graph.adjacency_matrix[0]) == 100

    def test_initial_adjacency_matrix_all_zeros(self):
        graph = Graph(3)
        for i in range(3):
            for j in range(3):
                assert graph.adjacency_matrix[i][j] == 0


class TestEdgeOperations:
    def test_add_edge_basic(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        assert graph.adjacency_matrix[0][1] == 1
        assert graph.adjacency_matrix[1][0] == 0  # Directed graph

    def test_add_multiple_edges(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 0)

        assert graph.adjacency_matrix[0][1] == 1
        assert graph.adjacency_matrix[1][2] == 1
        assert graph.adjacency_matrix[2][3] == 1
        assert graph.adjacency_matrix[3][0] == 1

    def test_add_self_loop(self):
        graph = Graph(3)
        graph.add_edge(1, 1)
        assert graph.adjacency_matrix[1][1] == 1

    @patch("builtins.print")
    def test_add_edge_invalid_indices(self, mock_print):
        graph = Graph(3)
        graph.add_edge(-1, 0)
        mock_print.assert_called_with("Invalid node indices: -1 or 0")

        graph.add_edge(0, 3)
        mock_print.assert_called_with("Invalid node indices: 0 or 3")

        graph.add_edge(5, 2)
        mock_print.assert_called_with("Invalid node indices: 5 or 2")

    def test_contains_edge_existing(self):
        graph = Graph(3)
        graph.add_edge(0, 2)
        assert graph.contains_edge(0, 2) is True
        assert graph.contains_edge(2, 0) is False

    def test_contains_edge_non_existing(self):
        graph = Graph(3)
        assert graph.contains_edge(0, 1) is False
        assert graph.contains_edge(1, 2) is False

    def test_contains_edge_invalid_indices(self):
        graph = Graph(3)
        assert graph.contains_edge(-1, 0) is False
        assert graph.contains_edge(0, 3) is False
        assert graph.contains_edge(5, 2) is False

    def test_remove_edge_existing(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.remove_edge(0, 1)
        assert graph.adjacency_matrix[0][1] == 0

    @patch("builtins.print")
    def test_remove_edge_non_existing(self, mock_print):
        graph = Graph(3)
        graph.remove_edge(0, 1)
        mock_print.assert_called_with("Grana izmedu cvorova 0 i 1 ne postoji.")

    @patch("builtins.print")
    def test_remove_edge_invalid_indices(self, mock_print):
        graph = Graph(3)
        graph.remove_edge(-1, 0)
        mock_print.assert_called_with("Invalid node indices: -1 or 0")


class TestUndirectedEdgeOperations:
    def test_add_undirected_edge(self):
        graph = Graph(3)
        graph.add_undirected_edge(0, 2)
        assert graph.adjacency_matrix[0][2] == 1
        assert graph.adjacency_matrix[2][0] == 1

    def test_remove_undirected_edge(self):
        graph = Graph(3)
        graph.add_undirected_edge(0, 2)
        graph.remove_undirected_edge(0, 2)
        assert graph.adjacency_matrix[0][2] == 0
        assert graph.adjacency_matrix[2][0] == 0

    def test_undirected_self_loop(self):
        graph = Graph(3)
        graph.add_undirected_edge(1, 1)
        assert graph.adjacency_matrix[1][1] == 1


class TestGraphProperties:
    def test_get_edges_count_empty_graph(self):
        graph = Graph(3)
        assert graph.get_edges_count() == 0

    def test_get_edges_count_with_edges(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)
        assert graph.get_edges_count() == 3

    def test_get_edges_count_with_self_loops(self):
        graph = Graph(3)
        graph.add_edge(0, 0)
        graph.add_edge(1, 1)
        assert graph.get_edges_count() == 2

    def test_get_neighbors_empty(self):
        graph = Graph(3)
        assert graph.get_neighbors(0) == []
        assert graph.get_neighbors(1) == []
        assert graph.get_neighbors(2) == []

    def test_get_neighbors_with_edges(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(0, 3)

        neighbors = graph.get_neighbors(0)
        assert set(neighbors) == {1, 2, 3}
        assert graph.get_neighbors(1) == []

    def test_get_neighbors_invalid_node(self):
        graph = Graph(3)
        assert graph.get_neighbors(-1) == []
        assert graph.get_neighbors(3) == []

    def test_get_in_degree(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(2, 1)

        assert graph.get_in_degree(1) == 2
        assert graph.get_in_degree(0) == 0
        assert graph.get_in_degree(2) == 0

    def test_get_out_degree(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)

        assert graph.get_out_degree(0) == 2
        assert graph.get_out_degree(1) == 0
        assert graph.get_out_degree(2) == 0

    def test_degree_invalid_node(self):
        graph = Graph(3)
        assert graph.get_in_degree(-1) == 0
        assert graph.get_out_degree(3) == 0

    def test_is_isolated_node(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(2, 3)

        assert graph.is_isolated(0) is False  # Has outgoing edge
        assert graph.is_isolated(1) is False  # Has incoming edge
        # Node with no edges would be isolated in a graph without these connections

    def test_get_isolated_nodes(self):
        graph = Graph(5)
        graph.add_edge(0, 1)
        graph.add_edge(2, 3)
        # Nodes 4 is isolated

        isolated = graph.get_isolated_nodes()
        assert 4 in isolated


class TestAdjacencyList:
    def test_to_adjacency_list_empty_graph(self):
        graph = Graph(3)
        adj_list = graph.to_adjacency_list()
        expected = {0: [], 1: [], 2: []}
        assert adj_list == expected

    def test_to_adjacency_list_with_edges(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)

        adj_list = graph.to_adjacency_list()
        expected = {0: [1, 2], 1: [2], 2: []}
        assert adj_list == expected

    def test_to_adjacency_list_with_self_loop(self):
        graph = Graph(2)
        graph.add_edge(0, 0)
        graph.add_edge(0, 1)

        adj_list = graph.to_adjacency_list()
        expected = {0: [0, 1], 1: []}
        assert adj_list == expected


class TestTraversals:
    def setup_method(self):
        # Create a simple directed graph: 0->1->2->3
        self.graph = Graph(4)
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)

    def test_dfs_traversal_linear_graph(self):
        result = self.graph.dfs_traversal(0)
        assert result == [0, 1, 2, 3]

    def test_dfs_traversal_single_node(self):
        single_graph = Graph(1)
        result = single_graph.dfs_traversal(0)
        assert result == [0]

    def test_dfs_traversal_disconnected_component(self):
        result = self.graph.dfs_traversal(3)
        assert result == [3]

    def test_dfs_traversal_invalid_start(self):
        result = self.graph.dfs_traversal(-1)
        assert result == []

        result = self.graph.dfs_traversal(4)
        assert result == []

    def test_bfs_traversal_linear_graph(self):
        result = self.graph.bfs_traversal(0)
        assert result == [0, 1, 2, 3]

    def test_bfs_traversal_tree_structure(self):
        tree_graph = Graph(4)
        tree_graph.add_edge(0, 1)
        tree_graph.add_edge(0, 2)
        tree_graph.add_edge(1, 3)

        result = tree_graph.bfs_traversal(0)
        # BFS should visit level by level: 0, then 1,2, then 3
        assert result[0] == 0
        assert set(result[1:3]) == {1, 2}
        assert result[3] == 3

    def test_bfs_traversal_invalid_start(self):
        result = self.graph.bfs_traversal(-1)
        assert result == []

        result = self.graph.bfs_traversal(4)
        assert result == []


class TestPathFinding:
    def setup_method(self):
        # Create a simple path: 0->1->2->3
        self.linear_graph = Graph(4)
        self.linear_graph.add_edge(0, 1)
        self.linear_graph.add_edge(1, 2)
        self.linear_graph.add_edge(2, 3)

    def test_find_path_exists_linear(self):
        assert self.linear_graph.find_path_exists(0, 3) is True
        assert self.linear_graph.find_path_exists(1, 3) is True
        assert self.linear_graph.find_path_exists(3, 0) is False

    def test_find_path_exists_same_node(self):
        assert self.linear_graph.find_path_exists(0, 0) is True
        assert self.linear_graph.find_path_exists(2, 2) is True

    def test_find_path_exists_disconnected(self):
        disconnected_graph = Graph(4)
        disconnected_graph.add_edge(0, 1)
        disconnected_graph.add_edge(2, 3)

        assert disconnected_graph.find_path_exists(0, 1) is True
        assert disconnected_graph.find_path_exists(0, 2) is False
        assert disconnected_graph.find_path_exists(2, 3) is True

    def test_get_shortest_path_linear(self):
        path = self.linear_graph.get_shortest_path(0, 3)
        assert path == [0, 1, 2, 3]

    def test_get_shortest_path_same_node(self):
        path = self.linear_graph.get_shortest_path(1, 1)
        assert path == [1]

    def test_get_shortest_path_no_path(self):
        path = self.linear_graph.get_shortest_path(3, 0)
        assert path == []

    def test_get_shortest_path_direct_connection(self):
        graph = Graph(3)
        graph.add_edge(0, 2)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)

        path = graph.get_shortest_path(0, 2)
        assert path == [0, 2]  # Direct path should be shorter

    def test_get_all_paths_simple(self):
        # Create a graph with multiple paths: 0->1->3 and 0->2->3
        multi_path_graph = Graph(4)
        multi_path_graph.add_edge(0, 1)
        multi_path_graph.add_edge(0, 2)
        multi_path_graph.add_edge(1, 3)
        multi_path_graph.add_edge(2, 3)

        paths = multi_path_graph.get_all_paths(0, 3)
        assert len(paths) == 2
        assert [0, 1, 3] in paths
        assert [0, 2, 3] in paths

    def test_get_all_paths_no_path(self):
        paths = self.linear_graph.get_all_paths(3, 0)
        assert paths == []

    def test_get_all_paths_invalid_nodes(self):
        paths = self.linear_graph.get_all_paths(-1, 0)
        assert paths == []

        paths = self.linear_graph.get_all_paths(0, 4)
        assert paths == []


class TestConnectivity:
    def test_is_connected_strongly_connected(self):
        # Create a cycle: 0->1->2->0
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)

        assert graph.is_connected() is True

    def test_is_connected_not_strongly_connected(self):
        # Create a path: 0->1->2
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)

        assert graph.is_connected() is False

    def test_is_connected_single_node(self):
        graph = Graph(1)
        assert graph.is_connected() is True

    def test_is_connected_empty_graph(self):
        graph = Graph(0)
        assert graph.is_connected() is True

    def test_is_weakly_connected_true(self):
        # Create a path: 0->1->2
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)

        assert graph.is_weakly_connected() is True

    def test_is_weakly_connected_false(self):
        # Create disconnected components
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(2, 3)

        assert graph.is_weakly_connected() is False

    def test_is_weakly_connected_single_node(self):
        graph = Graph(1)
        assert graph.is_weakly_connected() is True


class TestCycleDetection:
    def test_has_cycle_true_simple(self):
        # Create a simple cycle: 0->1->0
        graph = Graph(2)
        graph.add_edge(0, 1)
        graph.add_edge(1, 0)

        assert graph.has_cycle() is True

    def test_has_cycle_true_self_loop(self):
        graph = Graph(2)
        graph.add_edge(0, 0)

        assert graph.has_cycle() is True

    def test_has_cycle_false_linear(self):
        # Create a path: 0->1->2
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)

        assert graph.has_cycle() is False

    def test_has_cycle_false_empty(self):
        graph = Graph(3)
        assert graph.has_cycle() is False

    def test_has_cycle_complex_true(self):
        # Create a more complex graph with cycle
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 1)  # Creates cycle 1->2->3->1

        assert graph.has_cycle() is True


class TestUtilityMethods:
    def test_clear_graph(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)

        graph.clear_graph()

        assert graph.get_edges_count() == 0
        for i in range(3):
            for j in range(3):
                assert graph.adjacency_matrix[i][j] == 0

    def test_copy_graph(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)

        copied_graph = graph.copy()

        # Test that the copy has the same structure
        assert copied_graph.num_nodes == graph.num_nodes
        assert copied_graph.get_edges_count() == graph.get_edges_count()
        assert copied_graph.contains_edge(0, 1) is True
        assert copied_graph.contains_edge(1, 2) is True

        # Test that modifying original doesn't affect copy
        graph.add_edge(2, 0)
        assert copied_graph.contains_edge(2, 0) is False
        assert graph.contains_edge(2, 0) is True

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_graph(self, mock_stdout):
        graph = Graph(2)
        graph.add_edge(0, 1)
        graph.print_graph()

        # Just test that it doesn't crash and prints something
        assert mock_stdout.getvalue() != ""

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_graph_info(self, mock_stdout):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.print_graph_info()

        output = mock_stdout.getvalue()
        assert "Graph with 3 nodes and 2 edges" in output
        assert "Node degrees:" in output


class TestEdgeCases:
    def test_zero_node_graph_operations(self):
        graph = Graph(0)

        # Test that operations don't crash
        assert graph.get_edges_count() == 0
        assert graph.get_isolated_nodes() == []
        assert graph.has_cycle() is False
        assert graph.is_connected() is True  # Vacuously true
        assert graph.is_weakly_connected() is True
        assert graph.to_adjacency_list() == {}

    def test_single_node_graph_operations(self):
        graph = Graph(1)

        # Test basic operations
        assert graph.get_neighbors(0) == []
        assert graph.get_in_degree(0) == 0
        assert graph.get_out_degree(0) == 0
        assert graph.is_isolated(0) is True
        assert graph.get_isolated_nodes() == [0]

        # Add self-loop
        graph.add_edge(0, 0)
        assert graph.is_isolated(0) is False
        assert graph.has_cycle() is True
        assert graph.get_neighbors(0) == [0]

    def test_large_graph_creation(self):
        # Test with a reasonably large graph
        graph = Graph(1000)
        assert graph.size() == 1000
        assert graph.get_edges_count() == 0

        # Add some edges
        graph.add_edge(0, 999)
        graph.add_edge(500, 250)
        assert graph.get_edges_count() == 2

    def test_all_possible_edges(self):
        # Test complete graph (all possible edges)
        graph = Graph(3)
        for i in range(3):
            for j in range(3):
                graph.add_edge(i, j)

        assert graph.get_edges_count() == 9  # 3x3 = 9 including self-loops
        assert graph.is_connected() is True
        assert graph.has_cycle() is True

    def test_duplicate_edge_addition(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(0, 1)  # Adding same edge again

        assert graph.get_edges_count() == 1  # Should still be 1
        assert graph.adjacency_matrix[0][1] == 1

    def test_operations_on_empty_graph(self):
        graph = Graph(5)

        # All nodes should be isolated
        assert len(graph.get_isolated_nodes()) == 5

        # No paths should exist
        assert graph.find_path_exists(0, 4) is False
        assert graph.get_shortest_path(0, 4) == []
        assert graph.get_all_paths(0, 4) == []

        # Traversals should only return the start node
        assert graph.dfs_traversal(0) == [0]
        assert graph.bfs_traversal(0) == [0]


class TestComplexGraphScenarios:
    def test_star_graph(self):
        # Create a star graph: center node connected to all others
        graph = Graph(5)
        center = 0
        for i in range(1, 5):
            graph.add_edge(center, i)

        assert graph.get_out_degree(center) == 4
        assert graph.get_in_degree(center) == 0

        for i in range(1, 5):
            assert graph.get_in_degree(i) == 1
            assert graph.get_out_degree(i) == 0

        # Check connectivity
        assert graph.is_weakly_connected() is True
        assert graph.is_connected() is False  # Not strongly connected
        assert graph.has_cycle() is False

    def test_complete_graph(self):
        # Create a complete directed graph
        graph = Graph(4)
        for i in range(4):
            for j in range(4):
                if i != j:  # No self-loops
                    graph.add_edge(i, j)

        assert graph.get_edges_count() == 12  # 4*3 = 12 edges
        assert graph.is_connected() is True
        assert graph.has_cycle() is True

        # Every node should have in-degree and out-degree of 3
        for i in range(4):
            assert graph.get_in_degree(i) == 3
            assert graph.get_out_degree(i) == 3

    def test_binary_tree_like_structure(self):
        # Create a binary tree-like structure
        graph = Graph(7)
        # Root: 0, Level 1: 1,2, Level 2: 3,4,5,6
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 5)
        graph.add_edge(2, 6)

        assert graph.get_edges_count() == 6
        assert graph.has_cycle() is False
        assert graph.is_weakly_connected() is True

        # Test BFS traversal (should be level-order)
        bfs_result = graph.bfs_traversal(0)
        assert bfs_result[0] == 0
        assert set(bfs_result[1:3]) == {1, 2}
        assert set(bfs_result[3:7]) == {3, 4, 5, 6}

    def test_multiple_components(self):
        # Create a graph with multiple disconnected components
        graph = Graph(6)
        # Component 1: 0->1->2
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        # Component 2: 3->4
        graph.add_edge(3, 4)
        # Component 3: 5 (isolated)

        assert graph.is_weakly_connected() is False
        assert graph.is_connected() is False
        assert graph.get_isolated_nodes() == [5]

        # Test that DFS from each component only visits that component
        assert set(graph.dfs_traversal(0)) == {0, 1, 2}
        assert set(graph.dfs_traversal(3)) == {3, 4}
        assert graph.dfs_traversal(5) == [5]

    def test_cyclic_graph_complex(self):
        # Create a graph with multiple cycles
        graph = Graph(5)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)  # First cycle: 0->1->2->0
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(4, 2)  # Second cycle: 2->3->4->2

        assert graph.has_cycle() is True
        assert graph.is_connected() is False  # Can't reach 0,1 from 3,4

        # Check that all paths from 0 to 4 go through the cycles
        paths = graph.get_all_paths(0, 4)
        assert len(paths) > 0
        for path in paths:
            assert 2 in path  # All paths must go through node 2

    def test_longest_path_scenario(self):
        # Create a long chain to test performance
        graph = Graph(20)
        for i in range(19):
            graph.add_edge(i, i + 1)

        path = graph.get_shortest_path(0, 19)
        assert len(path) == 20
        assert path == list(range(20))

        # Test that there's only one path
        all_paths = graph.get_all_paths(0, 19)
        assert len(all_paths) == 1
        assert all_paths[0] == list(range(20))


class TestPerformanceAndStress:
    def test_dense_graph_operations(self):
        # Create a dense graph and test that operations complete
        graph = Graph(50)

        # Add many edges (about 50% density)
        import random

        random.seed(42)  # For reproducible tests

        for _ in range(500):
            i = random.randint(0, 49)
            j = random.randint(0, 49)
            graph.add_edge(i, j)

        # Test that basic operations work
        edges_count = graph.get_edges_count()
        assert edges_count > 0

        # Test connectivity operations
        is_connected = graph.is_connected()
        has_cycle = graph.has_cycle()

        # These should complete without timing out
        assert isinstance(is_connected, bool)
        assert isinstance(has_cycle, bool)

    def test_sparse_graph_operations(self):
        # Create a sparse graph (chain)
        graph = Graph(100)
        for i in range(99):
            graph.add_edge(i, i + 1)

        assert graph.get_edges_count() == 99
        assert graph.has_cycle() is False

        # Test long path finding
        path = graph.get_shortest_path(0, 99)
        assert len(path) == 100
        assert path[0] == 0
        assert path[-1] == 99


class TestMethodChaining:
    def test_method_combinations(self):
        # Test that methods work well together
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)

        # Clear and rebuild
        graph.clear_graph()
        assert graph.get_edges_count() == 0

        # Rebuild as cycle
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)

        assert graph.has_cycle() is True
        assert graph.is_connected() is True

        # Copy and modify
        graph_copy = graph.copy()
        graph.add_edge(0, 3)

        assert graph.get_edges_count() == 4
        assert graph_copy.get_edges_count() == 3

    def test_undirected_operations_combination(self):
        graph = Graph(4)

        # Mix directed and undirected edges
        graph.add_edge(0, 1)  # Directed
        graph.add_undirected_edge(1, 2)  # Undirected
        graph.add_edge(2, 3)  # Directed

        assert graph.contains_edge(0, 1) is True
        assert graph.contains_edge(1, 0) is False
        assert graph.contains_edge(1, 2) is True
        assert graph.contains_edge(2, 1) is True
        assert graph.contains_edge(2, 3) is True
        assert graph.contains_edge(3, 2) is False


class TestErrorHandlingAndRobustness:
    def test_boundary_values(self):
        graph = Graph(3)

        # Test boundary node indices
        graph.add_edge(0, 0)  # Valid
        graph.add_edge(2, 2)  # Valid

        assert graph.contains_edge(0, 0) is True
        assert graph.contains_edge(2, 2) is True

    def test_consistent_state_after_operations(self):
        graph = Graph(3)

        # Perform many operations and check consistency
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.remove_edge(0, 1)
        graph.add_undirected_edge(0, 2)
        graph.remove_undirected_edge(0, 2)

        # Graph should be consistent
        edges_count = graph.get_edges_count()
        manual_count = 0
        for i in range(3):
            for j in range(3):
                if graph.adjacency_matrix[i][j] == 1:
                    manual_count += 1

        assert edges_count == manual_count

    def test_operations_preserve_graph_properties(self):
        graph = Graph(4)

        # Add edges to create specific structure
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)

        original_size = graph.size()
        original_is_acyclic = not graph.has_cycle()

        # Operations that shouldn't change these properties
        adj_list = graph.to_adjacency_list()
        neighbors = graph.get_neighbors(0)
        degrees = [graph.get_in_degree(i) for i in range(4)]

        # Properties should remain the same
        assert graph.size() == original_size
        assert (not graph.has_cycle()) == original_is_acyclic


# Integration tests
class TestIntegration:
    def test_complete_workflow_directed_graph(self):
        """Test a complete workflow with directed graph operations"""
        # Create a small social network-like graph
        graph = Graph(5)  # 5 people

        # Add connections (A follows B, etc.)
        connections = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
        for start, end in connections:
            graph.add_edge(start, end)

        # Verify structure
        assert graph.get_edges_count() == 6
        assert graph.size() == 5

        # Test reachability
        assert graph.find_path_exists(0, 4) is True
        assert graph.find_path_exists(4, 0) is False

        # Test shortest paths
        path_0_to_4 = graph.get_shortest_path(0, 4)
        assert len(path_0_to_4) >= 3  # At least 3 hops

        # Test all paths
        all_paths_0_to_4 = graph.get_all_paths(0, 4)
        assert len(all_paths_0_to_4) >= 2  # Multiple paths exist

        # Test connectivity
        assert graph.is_weakly_connected() is True
        assert graph.is_connected() is False  # Not strongly connected

        # Test traversals
        dfs_from_0 = graph.dfs_traversal(0)
        bfs_from_0 = graph.bfs_traversal(0)
        assert len(dfs_from_0) == 5  # Should reach all nodes
        assert len(bfs_from_0) == 5
        assert dfs_from_0[0] == 0
        assert bfs_from_0[0] == 0

    def test_complete_workflow_undirected_graph(self):
        """Test workflow treating graph as undirected"""
        graph = Graph(4)

        # Create undirected connections
        graph.add_undirected_edge(0, 1)
        graph.add_undirected_edge(1, 2)
        graph.add_undirected_edge(2, 3)

        # Test that graph is now strongly connected (in undirected sense)
        assert graph.is_weakly_connected() is True

        # Test bidirectional paths
        assert graph.find_path_exists(0, 3) is True
        assert graph.find_path_exists(3, 0) is True

        # Test that edges exist in both directions
        for i in range(3):
            assert graph.contains_edge(i, i + 1) is True
            assert graph.contains_edge(i + 1, i) is True

    def test_graph_modification_workflow(self):
        """Test modifying a graph through its lifetime"""
        graph = Graph(4)

        # Phase 1: Build initial graph
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        assert graph.get_edges_count() == 2
        assert graph.has_cycle() is False

        # Phase 2: Add cycle
        graph.add_edge(2, 0)
        assert graph.has_cycle() is True

        # Phase 3: Add more connections
        graph.add_edge(1, 3)
        graph.add_edge(3, 2)
        original_count = graph.get_edges_count()

        # Phase 4: Remove some edges
        graph.remove_edge(2, 0)  # Remove cycle
        assert graph.get_edges_count() == original_count - 1

        # Phase 5: Clear and rebuild
        graph.clear_graph()
        assert graph.get_edges_count() == 0

        # Rebuild as star
        for i in range(1, 4):
            graph.add_undirected_edge(0, i)

        assert graph.get_edges_count() == 6  # 3 undirected edges = 6 directed
        assert graph.get_out_degree(0) == 3
        assert graph.get_in_degree(0) == 3


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
