import pytest

from src.data_structures.linked_lists.circular_list import CircularLinkedList, Node


class TestCircularLinkedList:

    def test_node_creation(self):
        """Test Node creation"""
        node = Node(5)
        assert node.data == 5
        assert node.next is None

    def test_empty_list_creation(self):
        """Test empty list creation"""
        cll = CircularLinkedList()
        assert cll.head is None
        assert cll.length_iterative() == 0
        assert cll.length() == 0

    def test_list_creation_with_head(self):
        """Test list creation with initial head node"""
        node = Node(10)
        cll = CircularLinkedList(node)
        assert cll.head == node
        assert cll.head.next == node
        assert cll.length_iterative() == 1

    def test_append_to_empty_list(self):
        """Test appending to empty list"""
        cll = CircularLinkedList()
        node = Node(5)
        cll.append(node)
        assert cll.head == node
        assert cll.head.next == node
        assert cll.length_iterative() == 1

    def test_append_multiple_nodes(self):
        """Test appending multiple nodes"""
        cll = CircularLinkedList()
        nodes = [Node(i) for i in range(1, 4)]
        for node in nodes:
            cll.append(node)

        assert cll.length_iterative() == 3
        assert cll.head.data == 1
        assert cll.head.next.data == 2
        assert cll.head.next.next.data == 3
        assert cll.head.next.next.next == cll.head

    def test_prepend_to_empty_list(self):
        """Test prepending to empty list"""
        cll = CircularLinkedList()
        node = Node(5)
        cll.prepend(node)
        assert cll.head == node
        assert cll.head.next == node
        assert cll.length_iterative() == 1

    def test_prepend_multiple_nodes(self):
        """Test prepending multiple nodes"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.prepend(Node(i))

        assert cll.length_iterative() == 3
        assert cll.head.data == 3
        assert cll.head.next.data == 2
        assert cll.head.next.next.data == 1
        assert cll.head.next.next.next == cll.head

    def test_find_maximum_empty_list(self):
        """Test finding maximum in empty list"""
        cll = CircularLinkedList()
        assert cll.find_maximum_value() is None

    def test_find_maximum_single_node(self):
        """Test finding maximum with single node"""
        cll = CircularLinkedList()
        cll.append(Node(5))
        assert cll.find_maximum_value() == 5

    def test_find_maximum_multiple_nodes(self):
        """Test finding maximum with multiple nodes"""
        cll = CircularLinkedList()
        values = [3, 7, 1, 9, 4]
        for val in values:
            cll.append(Node(val))
        assert cll.find_maximum_value() == 9

    def test_find_minimum_empty_list(self):
        """Test finding minimum in empty list"""
        cll = CircularLinkedList()
        assert cll.find_minimum_value() is None

    def test_find_minimum_single_node(self):
        """Test finding minimum with single node"""
        cll = CircularLinkedList()
        cll.append(Node(5))
        assert cll.find_minimum_value() == 5

    def test_find_minimum_multiple_nodes(self):
        """Test finding minimum with multiple nodes"""
        cll = CircularLinkedList()
        values = [3, 7, 1, 9, 4]
        for val in values:
            cll.append(Node(val))
        assert cll.find_minimum_value() == 1

    def test_delete_node_with_max_value(self):
        """Test deleting node with maximum value"""
        cll = CircularLinkedList()
        values = [3, 7, 1, 9, 4]
        for val in values:
            cll.append(Node(val))

        cll.delete_node_with_max_value()
        assert cll.find_maximum_value() == 7
        assert cll.length_iterative() == 4
        assert not cll.check_if_exists(9)

    def test_delete_node_with_min_value(self):
        """Test deleting node with minimum value"""
        cll = CircularLinkedList()
        values = [3, 7, 1, 9, 4]
        for val in values:
            cll.append(Node(val))

        cll.delete_node_with_min_value()
        assert cll.find_minimum_value() == 3
        assert cll.length_iterative() == 4
        assert not cll.check_if_exists(1)

    def test_delete_max_min_empty_list(self):
        """Test deleting max/min from empty list"""
        cll = CircularLinkedList()
        cll.delete_node_with_max_value()
        cll.delete_node_with_min_value()
        assert cll.head is None

    def test_square_every_value_empty_list(self):
        """Test squaring values in empty list"""
        cll = CircularLinkedList()
        cll.square_every_value()
        assert cll.head is None

    def test_square_every_value(self):
        """Test squaring every value"""
        cll = CircularLinkedList()
        values = [2, 3, 4]
        for val in values:
            cll.append(Node(val))

        cll.square_every_value()
        current = cll.head
        expected = [4, 9, 16]
        for expected_val in expected:
            assert current.data == expected_val
            current = current.next

    def test_delete_first_empty_list(self):
        """Test deleting first from empty list"""
        cll = CircularLinkedList()
        result = cll.delete_first()
        assert result is None
        assert cll.head is None

    def test_delete_first_single_node(self):
        """Test deleting first from single node list"""
        cll = CircularLinkedList()
        cll.append(Node(5))
        cll.delete_first()
        assert cll.head is None
        assert cll.length_iterative() == 0

    def test_delete_first_multiple_nodes(self):
        """Test deleting first from multiple nodes"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.append(Node(i))

        cll.delete_first()
        assert cll.head.data == 2
        assert cll.length_iterative() == 2
        assert cll.head.next.next == cll.head

    def test_delete_last_empty_list(self):
        """Test deleting last from empty list"""
        cll = CircularLinkedList()
        result = cll.delete_last()
        assert result is None
        assert cll.head is None

    def test_delete_last_single_node(self):
        """Test deleting last from single node list"""
        cll = CircularLinkedList()
        cll.append(Node(5))
        cll.delete_last()
        assert cll.head is None
        assert cll.length_iterative() == 0

    def test_delete_last_multiple_nodes(self):
        """Test deleting last from multiple nodes"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.append(Node(i))

        cll.delete_last()
        assert cll.length_iterative() == 2
        assert cll.head.data == 1
        assert cll.head.next.data == 2
        assert cll.head.next.next == cll.head

    def test_get_value_from_position_empty_list(self):
        """Test getting value from position in empty list"""
        cll = CircularLinkedList()
        assert cll.get_value_from_position(1) is None
        assert cll.get_value_from_position(0) is None
        assert cll.get_value_from_position(-1) is None

    def test_get_value_from_position_invalid_position(self):
        """Test getting value from invalid positions"""
        cll = CircularLinkedList()
        cll.append(Node(1))
        cll.append(Node(2))

        assert cll.get_value_from_position(0) is None
        assert cll.get_value_from_position(-1) is None
        assert cll.get_value_from_position(3) is None

    def test_get_value_from_position_valid(self):
        """Test getting value from valid positions"""
        cll = CircularLinkedList()
        values = [10, 20, 30]
        for val in values:
            cll.append(Node(val))

        assert cll.get_value_from_position(1).data == 10
        assert cll.get_value_from_position(2).data == 20
        assert cll.get_value_from_position(3).data == 30

    def test_insert_on_position_invalid_position(self):
        """Test inserting at invalid positions"""
        cll = CircularLinkedList()
        node = Node(5)
        result = cll.insert_on_position(node, 0)
        assert result is None
        result = cll.insert_on_position(node, -1)
        assert result is None

    def test_insert_on_position_empty_list(self):
        """Test inserting in empty list at position > 1"""
        cll = CircularLinkedList()
        node = Node(5)
        cll.insert_on_position(node, 2)
        assert cll.head is None

    def test_insert_on_position_first(self):
        """Test inserting at first position"""
        cll = CircularLinkedList()
        cll.append(Node(10))
        cll.insert_on_position(Node(5), 1)
        assert cll.head.data == 5
        assert cll.head.next.data == 10

    def test_insert_on_position_middle(self):
        """Test inserting in middle position"""
        cll = CircularLinkedList()
        for i in [1, 3, 5]:
            cll.append(Node(i))

        cll.insert_on_position(Node(2), 2)
        assert cll.head.data == 1
        assert cll.head.next.data == 2
        assert cll.head.next.next.data == 3
        assert cll.length_iterative() == 4

    def test_delete_value_empty_list(self):
        """Test deleting value from empty list"""
        cll = CircularLinkedList()
        cll.delete_value(5)
        assert cll.head is None

    def test_delete_value_single_node_match(self):
        """Test deleting value from single node list when it matches"""
        cll = CircularLinkedList()
        cll.append(Node(5))
        cll.delete_value(5)
        assert cll.head is None
        assert cll.length_iterative() == 0

    def test_delete_value_single_node_no_match(self):
        """Test deleting value from single node list when it doesn't match"""
        cll = CircularLinkedList()
        cll.append(Node(5))
        cll.delete_value(10)
        assert cll.head.data == 5
        assert cll.length_iterative() == 1

    def test_delete_value_head_node(self):
        """Test deleting head node value"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.append(Node(i))

        cll.delete_value(1)
        assert cll.head.data == 2
        assert cll.length_iterative() == 2

    def test_delete_value_middle_node(self):
        """Test deleting middle node value"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.append(Node(i))

        cll.delete_value(2)
        assert cll.head.data == 1
        assert cll.head.next.data == 3
        assert cll.length_iterative() == 2

    def test_delete_value_nonexistent(self):
        """Test deleting nonexistent value"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.append(Node(i))

        original_length = cll.length_iterative()
        cll.delete_value(5)
        assert cll.length_iterative() == original_length

    def test_delete_from_position_empty_list(self):
        """Test deleting from position in empty list"""
        cll = CircularLinkedList()
        result = cll.delete_from_position(1)
        assert result is None
        assert cll.head is None

    def test_delete_from_position_invalid(self):
        """Test deleting from invalid positions"""
        cll = CircularLinkedList()
        cll.append(Node(1))

        result = cll.delete_from_position(0)
        assert result is None
        result = cll.delete_from_position(-1)
        assert result is None
        result = cll.delete_from_position(3)
        assert result is None

    def test_delete_from_position_first(self):
        """Test deleting from first position"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.append(Node(i))

        cll.delete_from_position(1)
        assert cll.head.data == 2
        assert cll.length_iterative() == 2

    def test_delete_from_position_middle(self):
        """Test deleting from middle position"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.append(Node(i))

        cll.delete_from_position(2)
        assert cll.head.data == 1
        assert cll.head.next.data == 3
        assert cll.length_iterative() == 2

    def test_length_methods_consistency(self):
        """Test that iterative and recursive length methods give same results"""
        cll = CircularLinkedList()
        assert cll.length_iterative() == cll.length()

        for i in range(5):
            cll.append(Node(i))
            assert cll.length_iterative() == cll.length()

    def test_print_list_empty(self, capsys):
        """Test printing empty list"""
        cll = CircularLinkedList()
        cll.print_list()
        captured = capsys.readouterr()
        assert "[ ]" in captured.out

    def test_print_list_single_node(self, capsys):
        """Test printing single node list"""
        cll = CircularLinkedList()
        cll.append(Node(5))
        cll.print_list()
        captured = capsys.readouterr()
        assert "[ 5 ] (circular)" in captured.out

    def test_print_list_multiple_nodes(self, capsys):
        """Test printing multiple nodes list"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.append(Node(i))
        cll.print_list()
        captured = capsys.readouterr()
        assert "[ 1  ➝  2  ➝  3 ] (circular)" in captured.out

    def test_print_list_2_empty(self, capsys):
        """Test printing empty list vertically"""
        cll = CircularLinkedList()
        cll.print_list_2()
        captured = capsys.readouterr()
        assert captured.out == ""

    def test_print_list_2_with_nodes(self, capsys):
        """Test printing nodes vertically"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.append(Node(i))
        cll.print_list_2()
        captured = capsys.readouterr()
        lines = captured.out.strip().split("\n")
        assert lines == ["1", "2", "3"]

    def test_check_if_exists_empty_list(self):
        """Test checking existence in empty list"""
        cll = CircularLinkedList()
        assert not cll.check_if_exists(5)

    def test_check_if_exists_true(self):
        """Test checking existence when value exists"""
        cll = CircularLinkedList()
        values = [1, 2, 3, 4, 5]
        for val in values:
            cll.append(Node(val))

        for val in values:
            assert cll.check_if_exists(val)

    def test_check_if_exists_false(self):
        """Test checking existence when value doesn't exist"""
        cll = CircularLinkedList()
        for i in range(1, 4):
            cll.append(Node(i))

        assert not cll.check_if_exists(5)
        assert not cll.check_if_exists(0)

    def test_count_nodes_greater_than_empty_list(self):
        """Test counting nodes greater than value in empty list"""
        cll = CircularLinkedList()
        assert cll.count_nodes_greater_than(5) == 0

    def test_count_nodes_greater_than(self):
        """Test counting nodes greater than value"""
        cll = CircularLinkedList()
        values = [1, 3, 5, 7, 9]
        for val in values:
            cll.append(Node(val))

        assert cll.count_nodes_greater_than(0) == 5
        assert cll.count_nodes_greater_than(5) == 2
        assert cll.count_nodes_greater_than(10) == 0
        assert cll.count_nodes_greater_than(4) == 3

    def test_delete_every_second_node_empty_list(self):
        """Test deleting every second node from empty list"""
        cll = CircularLinkedList()
        cll.delete_every_second_node()
        assert cll.head is None

    def test_delete_every_second_node_single_node(self):
        """Test deleting every second node from single node list"""
        cll = CircularLinkedList()
        cll.append(Node(1))
        cll.delete_every_second_node()
        assert cll.head.data == 1
        assert cll.length_iterative() == 1

    def test_delete_every_second_node_multiple(self):
        """Test deleting every second node from multiple nodes"""
        cll = CircularLinkedList()
        for i in range(1, 6):
            cll.append(Node(i))

        cll.delete_every_second_node()
        remaining = []
        current = cll.head
        remaining.append(current.data)
        current = current.next
        while current != cll.head:
            remaining.append(current.data)
            current = current.next

        assert remaining == [1, 3, 5]

    def test_reverse_empty_list(self):
        """Test reversing empty list"""
        cll = CircularLinkedList()
        cll.reverse()
        assert cll.head is None

    def test_reverse_single_node(self):
        """Test reversing single node list"""
        cll = CircularLinkedList()
        cll.append(Node(5))
        cll.reverse()
        assert cll.head.data == 5
        assert cll.head.next == cll.head
        assert cll.length_iterative() == 1

    def test_reverse_multiple_nodes(self):
        """Test reversing multiple nodes"""
        cll = CircularLinkedList()
        original_values = [1, 2, 3, 4, 5]
        for val in original_values:
            cll.append(Node(val))

        cll.reverse()

        # Check that the list is still circular and has correct values in reverse order
        current = cll.head
        reversed_values = []
        reversed_values.append(current.data)
        current = current.next
        while current != cll.head:
            reversed_values.append(current.data)
            current = current.next

        assert reversed_values == [5, 4, 3, 2, 1]
        assert cll.length_iterative() == 5

    def test_concat_empty_lists(self):
        """Test concatenating two empty lists"""
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()
        cll1.concat(cll2)
        assert cll1.head is None
        assert cll1.length_iterative() == 0

    def test_concat_empty_with_non_empty(self):
        """Test concatenating empty list with non-empty list"""
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()
        for i in range(1, 4):
            cll2.append(Node(i))

        cll1.concat(cll2)
        assert cll1.head == cll2.head
        assert cll1.length_iterative() == 3

    def test_concat_non_empty_with_empty(self):
        """Test concatenating non-empty list with empty list"""
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()
        for i in range(1, 4):
            cll1.append(Node(i))

        original_length = cll1.length_iterative()
        cll1.concat(cll2)
        assert cll1.length_iterative() == original_length

    def test_concat_two_non_empty_lists(self):
        """Test concatenating two non-empty lists"""
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()

        for i in range(1, 4):
            cll1.append(Node(i))
        for i in range(4, 7):
            cll2.append(Node(i))

        cll1.concat(cll2)

        # Check that all values are present and list is still circular
        values = []
        current = cll1.head
        values.append(current.data)
        current = current.next
        while current != cll1.head:
            values.append(current.data)
            current = current.next

        assert values == [1, 2, 3, 4, 5, 6]
        assert cll1.length_iterative() == 6

    def test_equality_both_empty(self):
        """Test equality of two empty lists"""
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()
        assert cll1 == cll2

    def test_equality_one_empty(self):
        """Test equality when one list is empty"""
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()
        cll2.append(Node(1))
        assert cll1 != cll2
        assert cll2 != cll1

    def test_equality_different_lengths(self):
        """Test equality of lists with different lengths"""
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()

        cll1.append(Node(1))
        cll1.append(Node(2))

        cll2.append(Node(1))
        cll2.append(Node(2))
        cll2.append(Node(3))

        assert cll1 != cll2

    def test_equality_same_values(self):
        """Test equality of lists with same values"""
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()

        values = [1, 2, 3, 4, 5]
        for val in values:
            cll1.append(Node(val))
            cll2.append(Node(val))

        assert cll1 == cll2

    def test_equality_different_values(self):
        """Test equality of lists with different values"""
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()

        for i in range(1, 4):
            cll1.append(Node(i))
            cll2.append(Node(i + 1))

        assert cll1 != cll2

    def test_equality_same_length_different_order(self):
        """Test equality of lists with same values in different order"""
        cll1 = CircularLinkedList()
        cll2 = CircularLinkedList()

        values1 = [1, 2, 3]
        values2 = [3, 2, 1]

        for val in values1:
            cll1.append(Node(val))
        for val in values2:
            cll2.append(Node(val))

        assert cll1 != cll2

    def test_negative_values(self):
        """Test operations with negative values"""
        cll = CircularLinkedList()
        values = [-5, -2, -8, -1]
        for val in values:
            cll.append(Node(val))

        assert cll.find_maximum_value() == -1
        assert cll.find_minimum_value() == -8
        assert cll.check_if_exists(-2)
        assert not cll.check_if_exists(0)
        assert cll.count_nodes_greater_than(-3) == 2

    def test_duplicate_values(self):
        """Test operations with duplicate values"""
        cll = CircularLinkedList()
        values = [3, 1, 3, 2, 3]
        for val in values:
            cll.append(Node(val))

        assert cll.find_maximum_value() == 3
        assert cll.find_minimum_value() == 1

        # Delete one instance of 3
        cll.delete_value(3)
        assert cll.length_iterative() == 4
        assert cll.check_if_exists(3)  # Should still exist

        # Delete all instances of 3
        while cll.check_if_exists(3):
            cll.delete_value(3)
        assert cll.length_iterative() == 2
        assert not cll.check_if_exists(3)

    def test_large_list_operations(self):
        """Test operations on larger lists"""
        cll = CircularLinkedList()
        size = 100

        # Create list with values 0 to 99
        for i in range(size):
            cll.append(Node(i))

        assert cll.length_iterative() == size
        assert cll.length() == size
        assert cll.find_maximum_value() == 99
        assert cll.find_minimum_value() == 0
        assert cll.get_value_from_position(50).data == 49  # 1-indexed
        assert cll.count_nodes_greater_than(50) == 49

    def test_zero_values(self):
        """Test operations with zero values"""
        cll = CircularLinkedList()
        values = [0, 5, 0, -3, 0]
        for val in values:
            cll.append(Node(val))

        assert cll.find_maximum_value() == 5
        assert cll.find_minimum_value() == -3
        assert cll.check_if_exists(0)
        assert cll.count_nodes_greater_than(0) == 1

        # Test squaring with zeros
        cll2 = CircularLinkedList()
        cll2.append(Node(0))
        cll2.append(Node(2))
        cll2.square_every_value()
        assert cll2.head.data == 0
        assert cll2.head.next.data == 4

    def test_single_value_operations(self):
        """Test all operations on single-value list"""
        cll = CircularLinkedList()
        cll.append(Node(42))

        # Test all methods that should work with single node
        assert cll.length_iterative() == 1
        assert cll.length() == 1
        assert cll.find_maximum_value() == 42
        assert cll.find_minimum_value() == 42
        assert cll.check_if_exists(42)
        assert not cll.check_if_exists(0)
        assert cll.count_nodes_greater_than(40) == 1
        assert cll.count_nodes_greater_than(50) == 0
        assert cll.get_value_from_position(1).data == 42
        assert cll.get_value_from_position(2) is None

    def test_edge_cases_position_operations(self):
        """Test edge cases for position-based operations"""
        cll = CircularLinkedList()

        # Test with exact boundary positions
        for i in range(1, 4):
            cll.append(Node(i * 10))

        # Test position at exact length
        assert cll.get_value_from_position(3).data == 30
        assert cll.get_value_from_position(4) is None

        # Test deletion at exact length
        cll.delete_from_position(3)
        assert cll.length_iterative() == 2
        assert not cll.check_if_exists(30)

        # Test insertion at positions
        cll.insert_on_position(Node(25), 3)
        assert cll.get_value_from_position(3).data == 25
        assert cll.length_iterative() == 3

    def test_circular_property_maintained(self):
        """Test that circular property is maintained after all operations"""
        cll = CircularLinkedList()

        # Build list
        for i in range(1, 6):
            cll.append(Node(i))

        # Perform various operations and check circularity after each
        operations = [
            lambda: cll.delete_first(),
            lambda: cll.delete_last(),
            lambda: cll.prepend(Node(0)),
            lambda: cll.append(Node(10)),
            lambda: cll.delete_value(3),
            lambda: cll.insert_on_position(Node(3), 2),
        ]

        for operation in operations:
            if cll.head:  # Only test if list is not empty
                operation()
                if cll.head:  # Check circularity if list still has nodes
                    # Traverse the list and ensure we get back to head
                    current = cll.head
                    count = 0
                    max_iterations = cll.length_iterative() + 1

                    while count < max_iterations:
                        current = current.next
                        count += 1
                        if current == cll.head:
                            break

                    assert current == cll.head, f"Circular property broken after operation"

    def test_memory_and_reference_integrity(self):
        """Test that node references are properly maintained"""
        cll = CircularLinkedList()
        nodes = [Node(i) for i in range(3)]

        for node in nodes:
            cll.append(node)

        # Verify that the actual node objects are in the list
        current = cll.head
        found_nodes = []
        found_nodes.append(current)
        current = current.next

        while current != cll.head:
            found_nodes.append(current)
            current = current.next

        # Check that we found all original nodes
        for original_node in nodes:
            assert original_node in found_nodes
