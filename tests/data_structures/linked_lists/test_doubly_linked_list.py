import pytest

from src.data_structures.linked_lists.doubly_linked_list import DoublyLinkedList, Node


class TestDoublyLinkedListBasics:
    """Test basic DoublyLinkedList functionality."""

    def test_empty_list_creation(self):
        """Test creating an empty doubly linked list."""
        dll = DoublyLinkedList()
        assert dll.head is None

    def test_list_creation_with_head(self):
        """Test creating a doubly linked list with initial head node."""
        node = Node(10)
        dll = DoublyLinkedList(node)
        assert dll.head == node
        assert dll.head.value == 10
        assert dll.head.prev is None
        assert dll.head.next is None


class TestNodeCreation:
    """Test Node creation and properties."""

    def test_node_creation(self):
        """Test creating a node with value."""
        node = Node(5)
        assert node.value == 5
        assert node.prev is None
        assert node.next is None

    def test_node_with_various_types(self):
        """Test node creation with different data types."""
        node_int = Node(42)
        node_str = Node("hello")
        node_list = Node([1, 2, 3])
        node_dict = Node({"key": "value"})

        assert node_int.value == 42
        assert node_str.value == "hello"
        assert node_list.value == [1, 2, 3]
        assert node_dict.value == {"key": "value"}


class TestPrepend:
    """Test prepend functionality."""

    def test_prepend_to_empty_list(self):
        """Test prepending to an empty list."""
        dll = DoublyLinkedList()
        node = Node(1)
        dll.prepend(node)

        assert dll.head == node
        assert dll.head.value == 1
        assert dll.head.prev is None
        assert dll.head.next is None

    def test_prepend_to_single_node_list(self):
        """Test prepending to a list with one node."""
        dll = DoublyLinkedList()
        first_node = Node(2)
        second_node = Node(1)

        dll.prepend(first_node)
        dll.prepend(second_node)

        assert dll.head == second_node
        assert dll.head.value == 1
        assert dll.head.prev is None
        assert dll.head.next == first_node
        assert first_node.prev == second_node
        assert first_node.next is None

    def test_prepend_multiple_nodes(self):
        """Test prepending multiple nodes."""
        dll = DoublyLinkedList()
        nodes = [Node(i) for i in range(5, 0, -1)]

        for node in nodes:
            dll.prepend(node)

        # Should be: 1 <-> 2 <-> 3 <-> 4 <-> 5
        current = dll.head
        for expected_value in range(1, 6):
            assert current.value == expected_value
            current = current.next


class TestAppend:
    """Test append functionality."""

    def test_append_to_empty_list(self):
        """Test appending to an empty list."""
        dll = DoublyLinkedList()
        node = Node(1)
        dll.append(node)

        assert dll.head == node
        assert dll.head.value == 1
        assert dll.head.prev is None
        assert dll.head.next is None

    def test_append_to_single_node_list(self):
        """Test appending to a list with one node."""
        dll = DoublyLinkedList()
        first_node = Node(1)
        second_node = Node(2)

        dll.append(first_node)
        dll.append(second_node)

        assert dll.head == first_node
        assert dll.head.value == 1
        assert dll.head.prev is None
        assert dll.head.next == second_node
        assert second_node.prev == first_node
        assert second_node.next is None

    def test_append_multiple_nodes(self):
        """Test appending multiple nodes."""
        dll = DoublyLinkedList()
        nodes = [Node(i) for i in range(1, 6)]

        for node in nodes:
            dll.append(node)

        # Should be: 1 <-> 2 <-> 3 <-> 4 <-> 5
        current = dll.head
        for expected_value in range(1, 6):
            assert current.value == expected_value
            current = current.next


class TestDeleteFirst:
    """Test delete_first functionality."""

    def test_delete_first_from_empty_list(self):
        """Test deleting first node from empty list."""
        dll = DoublyLinkedList()
        dll.delete_first()  # Should not raise error
        assert dll.head is None

    def test_delete_first_from_single_node_list(self):
        """Test deleting first node from single node list."""
        dll = DoublyLinkedList()
        node = Node(1)
        dll.append(node)
        dll.delete_first()

        assert dll.head is None

    def test_delete_first_from_multi_node_list(self):
        """Test deleting first node from multi-node list."""
        dll = DoublyLinkedList()
        nodes = [Node(i) for i in range(1, 4)]
        for node in nodes:
            dll.append(node)

        dll.delete_first()

        assert dll.head.value == 2
        assert dll.head.prev is None
        assert dll.head.next.value == 3


class TestDeleteLast:
    """Test delete_last functionality."""

    def test_delete_last_from_empty_list(self):
        """Test deleting last node from empty list."""
        dll = DoublyLinkedList()
        dll.delete_last()  # Should not raise error
        assert dll.head is None

    def test_delete_last_from_single_node_list(self):
        """Test deleting last node from single node list."""
        dll = DoublyLinkedList()
        node = Node(1)
        dll.append(node)
        dll.delete_last()

        assert dll.head is None

    def test_delete_last_from_multi_node_list(self):
        """Test deleting last node from multi-node list."""
        dll = DoublyLinkedList()
        nodes = [Node(i) for i in range(1, 4)]
        for node in nodes:
            dll.append(node)

        dll.delete_last()

        # Should be: 1 <-> 2
        current = dll.head
        assert current.value == 1
        assert current.next.value == 2
        assert current.next.next is None


class TestGetMiddleNode:
    """Test get_middle_node functionality."""

    def test_get_middle_from_empty_list(self):
        """Test getting middle node from empty list."""
        dll = DoublyLinkedList()
        result = dll.get_middle_node()
        assert result is None

    def test_get_middle_from_single_node(self):
        """Test getting middle node from single node list."""
        dll = DoublyLinkedList()
        node = Node(1)
        dll.append(node)

        middle = dll.get_middle_node()
        assert middle.value == 1

    def test_get_middle_from_odd_length_list(self):
        """Test getting middle node from odd length list."""
        dll = DoublyLinkedList()
        for i in range(1, 6):  # 1, 2, 3, 4, 5
            dll.append(Node(i))

        middle = dll.get_middle_node()
        assert middle.value == 3

    def test_get_middle_from_even_length_list(self):
        """Test getting middle node from even length list."""
        dll = DoublyLinkedList()
        for i in range(1, 5):  # 1, 2, 3, 4
            dll.append(Node(i))

        middle = dll.get_middle_node()
        assert middle.value == 2  # First of two middle nodes


class TestEquality:
    """Test __eq__ functionality."""

    def test_empty_lists_equal(self):
        """Test that two empty lists are equal."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()
        assert dll1 == dll2

    def test_single_node_lists_equal(self):
        """Test that two single-node lists with same value are equal."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()
        dll1.append(Node(1))
        dll2.append(Node(1))
        assert dll1 == dll2

    def test_single_node_lists_not_equal(self):
        """Test that two single-node lists with different values are not equal."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()
        dll1.append(Node(1))
        dll2.append(Node(2))
        assert dll1 != dll2

    def test_multi_node_lists_equal(self):
        """Test that two multi-node lists with same values are equal."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()
        for i in range(1, 4):
            dll1.append(Node(i))
            dll2.append(Node(i))
        assert dll1 == dll2

    def test_different_length_lists_not_equal(self):
        """Test that lists with different lengths are not equal."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()
        dll1.append(Node(1))
        dll2.append(Node(1))
        dll2.append(Node(2))
        assert dll1 != dll2

    def test_empty_vs_non_empty_not_equal(self):
        """Test that empty list is not equal to non-empty list."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()
        dll2.append(Node(1))
        assert dll1 != dll2


class TestIntersection:
    """Test intersection functionality."""

    def test_intersection_empty_lists(self):
        """Test intersection of two empty lists."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()
        result = dll1.intersection(dll2)
        assert result.head is None

    def test_intersection_one_empty_list(self):
        """Test intersection when one list is empty."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()
        dll1.append(Node(1))
        result = dll1.intersection(dll2)
        assert result.head is None

    def test_intersection_no_common_elements(self):
        """Test intersection with no common elements."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()
        dll1.append(Node(1))
        dll1.append(Node(2))
        dll2.append(Node(3))
        dll2.append(Node(4))

        result = dll1.intersection(dll2)
        assert result.head is None

    def test_intersection_with_common_elements(self):
        """Test intersection with common elements."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()

        # dll1: 1, 2, 3, 4
        for i in range(1, 5):
            dll1.append(Node(i))

        # dll2: 3, 4, 5, 6
        for i in range(3, 7):
            dll2.append(Node(i))

        result = dll1.intersection(dll2)

        # Should contain 3, 4
        current = result.head
        assert current.value == 3
        current = current.next
        assert current.value == 4
        assert current.next is None

    def test_intersection_duplicate_values(self):
        """Test intersection with duplicate values."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()

        # dll1: 1, 2, 2, 3
        for val in [1, 2, 2, 3]:
            dll1.append(Node(val))

        # dll2: 2, 3, 3, 4
        for val in [2, 3, 3, 4]:
            dll2.append(Node(val))

        result = dll1.intersection(dll2)

        # Should contain 2, 2, 3 (all matching occurrences from first list)
        values = []
        current = result.head
        while current:
            values.append(current.value)
            current = current.next

        assert values == [2, 2, 3]


class TestAppendSort:
    """Test append_sort functionality."""

    def test_append_sort_to_empty_list(self):
        """Test append_sort to empty list."""
        dll = DoublyLinkedList()
        node = Node({"cijena": 10})
        dll.append_sort(node)

        assert dll.head == node
        assert dll.head.value["cijena"] == 10

    def test_append_sort_smallest_value(self):
        """Test append_sort with smallest value (should become head)."""
        dll = DoublyLinkedList()
        dll.append(Node({"cijena": 20}))
        dll.append(Node({"cijena": 30}))

        new_node = Node({"cijena": 10})
        dll.append_sort(new_node)

        assert dll.head == new_node
        assert dll.head.value["cijena"] == 10

    def test_append_sort_middle_value(self):
        """Test append_sort with middle value."""
        dll = DoublyLinkedList()
        dll.append(Node({"cijena": 10}))
        dll.append(Node({"cijena": 30}))

        new_node = Node({"cijena": 20})
        dll.append_sort(new_node)

        # Should be: 10 <-> 20 <-> 30
        current = dll.head
        assert current.value["cijena"] == 10
        current = current.next
        assert current.value["cijena"] == 20
        current = current.next
        assert current.value["cijena"] == 30

    def test_append_sort_largest_value(self):
        """Test append_sort with largest value (should become tail)."""
        dll = DoublyLinkedList()
        dll.append(Node({"cijena": 10}))
        dll.append(Node({"cijena": 20}))

        new_node = Node({"cijena": 30})
        dll.append_sort(new_node)

        # Should be: 10 <-> 20 <-> 30
        current = dll.head
        while current.next:
            current = current.next
        assert current.value["cijena"] == 30

    def test_append_sort_equal_values(self):
        """Test append_sort with equal values."""
        dll = DoublyLinkedList()
        dll.append(Node({"cijena": 20}))

        new_node = Node({"cijena": 20})
        dll.append_sort(new_node)

        # Both nodes should be in the list
        current = dll.head
        assert current.value["cijena"] == 20
        current = current.next
        assert current.value["cijena"] == 20


class TestPrintMethods:
    """Test print methods (capture output)."""

    def test_print_list_empty(self, capsys):
        """Test printing empty list."""
        dll = DoublyLinkedList()
        dll.print_list()
        captured = capsys.readouterr()
        assert captured.out.strip() == "[ ]"

    def test_print_list_single_node(self, capsys):
        """Test printing single node list."""
        dll = DoublyLinkedList()
        dll.append(Node(1))
        dll.print_list()
        captured = capsys.readouterr()
        assert captured.out.strip() == "[ 1 ]"

    def test_print_list_multiple_nodes(self, capsys):
        """Test printing multiple node list."""
        dll = DoublyLinkedList()
        for i in range(1, 4):
            dll.append(Node(i))
        dll.print_list()
        captured = capsys.readouterr()
        assert captured.out.strip() == "[ 1   ⇄   2   ⇄   3 ]"

    def test_print_list_2_empty(self, capsys):
        """Test printing empty list vertically."""
        dll = DoublyLinkedList()
        dll.print_list_2()
        captured = capsys.readouterr()
        assert captured.out == ""

    def test_print_list_2_multiple_nodes(self, capsys):
        """Test printing multiple nodes vertically."""
        dll = DoublyLinkedList()
        for i in range(1, 4):
            dll.append(Node(i))
        dll.print_list_2()
        captured = capsys.readouterr()
        assert captured.out == "1\n2\n3\n"

    def test_print_list_reversed_empty(self, capsys):
        """Test printing empty list in reverse."""
        dll = DoublyLinkedList()
        dll.print_list_reversed()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Reversed list: [ ]"

    def test_print_list_reversed_single_node(self, capsys):
        """Test printing single node list in reverse."""
        dll = DoublyLinkedList()
        dll.append(Node(1))
        dll.print_list_reversed()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Reversed list: [ 1 ]"

    def test_print_list_reversed_multiple_nodes(self, capsys):
        """Test printing multiple node list in reverse."""
        dll = DoublyLinkedList()
        for i in range(1, 4):
            dll.append(Node(i))
        dll.print_list_reversed()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Reversed list: [ 3   ⇄   2   ⇄   1 ]"


class TestEdgeCasesAndErrorHandling:
    """Test edge cases and error conditions."""

    def test_operations_on_none_nodes(self):
        """Test that operations handle None nodes gracefully."""
        dll = DoublyLinkedList()
        # These should not raise errors
        dll.delete_first()
        dll.delete_last()
        middle = dll.get_middle_node()
        assert middle is None

    def test_very_large_list(self):
        """Test operations on a very large list."""
        dll = DoublyLinkedList()
        n = 1000

        # Create large list
        for i in range(n):
            dll.append(Node(i))

        # Test middle node
        middle = dll.get_middle_node()
        assert middle.value in range(n // 2 - 1, n // 2 + 2)  # Allow some flexibility

        # Test deletion
        dll.delete_first()
        assert dll.head.value == 1

        dll.delete_last()
        # Find last node
        current = dll.head
        while current.next:
            current = current.next
        assert current.value == n - 2

    def test_mixed_data_types(self):
        """Test list with mixed data types."""
        dll = DoublyLinkedList()
        values = [1, "hello", [1, 2, 3], {"key": "value"}, None]

        for val in values:
            dll.append(Node(val))

        # Test equality with same mixed types
        dll2 = DoublyLinkedList()
        for val in values:
            dll2.append(Node(val))

        assert dll == dll2

    def test_circular_reference_prevention(self):
        """Test that operations don't create circular references."""
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)

        dll.append(node1)
        dll.append(node2)

        # Ensure no circular references
        assert node1.prev is None
        assert node1.next == node2
        assert node2.prev == node1
        assert node2.next is None


class TestComplexScenarios:
    """Test complex scenarios combining multiple operations."""

    def test_build_and_modify_list(self):
        """Test building a list and performing various modifications."""
        dll = DoublyLinkedList()

        # Build list: 1 <-> 2 <-> 3 <-> 4 <-> 5
        for i in range(1, 6):
            dll.append(Node(i))

        # Delete first and last
        dll.delete_first()  # 2 <-> 3 <-> 4 <-> 5
        dll.delete_last()  # 2 <-> 3 <-> 4

        # Prepend new node
        dll.prepend(Node(1))  # 1 <-> 2 <-> 3 <-> 4

        # Verify final state
        expected_values = [1, 2, 3, 4]
        current = dll.head
        for expected in expected_values:
            assert current.value == expected
            current = current.next

        # Verify backward links
        current = dll.head
        while current.next:
            current = current.next

        for expected in reversed(expected_values):
            assert current.value == expected
            current = current.prev

    def test_intersection_with_modifications(self):
        """Test intersection after modifying lists."""
        dll1 = DoublyLinkedList()
        dll2 = DoublyLinkedList()

        # Initial lists
        for i in [1, 2, 3, 4]:
            dll1.append(Node(i))
        for i in [3, 4, 5, 6]:
            dll2.append(Node(i))

        # Get intersection: should be [3, 4]
        result = dll1.intersection(dll2)

        # Modify original lists
        dll1.delete_first()  # Remove 1
        dll2.delete_last()  # Remove 6

        # Original intersection should be unchanged
        current = result.head
        assert current.value == 3
        current = current.next
        assert current.value == 4
        assert current.next is None

        # New intersection should be different
        new_result = dll1.intersection(dll2)
        values = []
        current = new_result.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [3, 4]
