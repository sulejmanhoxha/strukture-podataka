import pytest

from src.data_structures.linked_lists.linked_list import LinkedList, Node


class TestNode:
    """Test cases for the Node class."""

    def test_node_creation(self):
        """Test that a node can be created with a value."""
        node = Node(5)
        assert node.value == 5
        assert node.next is None

    def test_node_with_different_types(self):
        """Test node creation with different data types."""
        node_int = Node(42)
        node_str = Node("hello")
        node_float = Node(3.14)

        assert node_int.value == 42
        assert node_str.value == "hello"
        assert node_float.value == 3.14


class TestLinkedListBasics:
    """Test basic LinkedList functionality."""

    def test_empty_list_creation(self):
        """Test creating an empty linked list."""
        ll = LinkedList()
        assert ll.head is None

    def test_list_creation_with_head(self):
        """Test creating a linked list with initial head node."""
        node = Node(10)
        ll = LinkedList(node)
        assert ll.head == node
        assert ll.head.value == 10


class TestAppendPrepend:
    """Test append and prepend operations."""

    def test_append_to_empty_list(self):
        """Test appending to an empty list."""
        ll = LinkedList()
        node = Node(1)
        ll.append(node)

        assert ll.head == node
        assert ll.head.value == 1
        assert ll.head.next is None

    def test_append_multiple_nodes(self):
        """Test appending multiple nodes."""
        ll = LinkedList()
        nodes = [Node(i) for i in range(1, 6)]

        for node in nodes:
            ll.append(node)

        assert ll.length_iterative() == 5
        assert ll.head.value == 1

        # Check order
        current = ll.head
        for i in range(1, 6):
            assert current.value == i
            current = current.next

    def test_prepend_to_empty_list(self):
        """Test prepending to an empty list."""
        ll = LinkedList()
        node = Node(1)
        ll.prepend(node)

        assert ll.head == node
        assert ll.head.value == 1
        assert ll.head.next is None

    def test_prepend_multiple_nodes(self):
        """Test prepending multiple nodes."""
        ll = LinkedList()
        for i in range(1, 6):
            ll.prepend(Node(i))

        assert ll.length_iterative() == 5
        assert ll.head.value == 5  # Last prepended becomes head

        # Check reverse order
        current = ll.head
        for i in range(5, 0, -1):
            assert current.value == i
            current = current.next


class TestFindValues:
    """Test finding minimum and maximum values."""

    def test_find_maximum_value(self):
        """Test finding maximum value in the list."""
        ll = LinkedList()
        values = [3, 1, 4, 1, 5, 9, 2]
        for val in values:
            ll.append(Node(val))

        assert ll.find_maximum_value() == 9

    def test_find_maximum_single_node(self):
        """Test finding maximum in single-node list."""
        ll = LinkedList()
        ll.append(Node(42))
        assert ll.find_maximum_value() == 42

    def test_find_minimum_value(self):
        """Test finding minimum value in the list."""
        ll = LinkedList()
        values = [3, 1, 4, 1, 5, 9, 2]
        for val in values:
            ll.append(Node(val))

        assert ll.find_minimum_value() == 1

    def test_find_minimum_single_node(self):
        """Test finding minimum in single-node list."""
        ll = LinkedList()
        ll.append(Node(42))
        assert ll.find_minimum_value() == 42

    def test_find_values_with_negatives(self):
        """Test finding min/max with negative values."""
        ll = LinkedList()
        values = [-5, 3, -1, 7, -10, 2]
        for val in values:
            ll.append(Node(val))

        assert ll.find_maximum_value() == 7
        assert ll.find_minimum_value() == -10


class TestDeleteOperations:
    """Test various delete operations."""

    def test_delete_first_node(self):
        """Test deleting the first node."""
        ll = LinkedList()
        for i in range(1, 4):
            ll.append(Node(i))

        ll.delete_first()
        assert ll.head.value == 2
        assert ll.length_iterative() == 2

    def test_delete_first_single_node(self):
        """Test deleting first node when only one exists."""
        ll = LinkedList()
        ll.append(Node(1))
        ll.delete_first()
        assert ll.head is None

    def test_delete_last_node(self):
        """Test deleting the last node."""
        ll = LinkedList()
        for i in range(1, 4):
            ll.append(Node(i))

        ll.delete_last()
        assert ll.length_iterative() == 2
        # Check that last node is now 2
        current = ll.head
        while current.next:
            current = current.next
        assert current.value == 2

    def test_delete_value(self):
        """Test deleting a node by value."""
        ll = LinkedList()
        values = [1, 2, 3, 4, 5]
        for val in values:
            ll.append(Node(val))

        ll.delete_value(3)
        assert ll.length_iterative() == 4
        assert not ll.check_if_exists(3)

    def test_delete_value_head(self):
        """Test deleting head node by value."""
        ll = LinkedList()
        for i in range(1, 4):
            ll.append(Node(i))

        ll.delete_value(1)
        assert ll.head.value == 2
        assert ll.length_iterative() == 2

    def test_delete_node_with_max_value(self):
        """Test deleting node with maximum value."""
        ll = LinkedList()
        values = [3, 1, 4, 1, 5, 2]
        for val in values:
            ll.append(Node(val))

        ll.delete_node_with_max_value()
        assert ll.find_maximum_value() == 4
        assert not ll.check_if_exists(5)

    def test_delete_node_with_min_value(self):
        """Test deleting node with minimum value."""
        ll = LinkedList()
        values = [3, 1, 4, 5, 2]
        for val in values:
            ll.append(Node(val))

        ll.delete_node_with_min_value()
        assert ll.find_minimum_value() == 2
        assert not ll.check_if_exists(1)


class TestPositionalOperations:
    """Test position-based operations."""

    def test_get_value_from_position(self):
        """Test getting value from specific position."""
        ll = LinkedList()
        values = [10, 20, 30, 40, 50]
        for val in values:
            ll.append(Node(val))

        assert ll.get_value_from_position(1).value == 10
        assert ll.get_value_from_position(3).value == 30
        assert ll.get_value_from_position(5).value == 50
        assert ll.get_value_from_position(6) is None
        assert ll.get_value_from_position(0) is None

    def test_insert_on_position(self):
        """Test inserting node at specific position."""
        ll = LinkedList()
        for i in range(1, 4):
            ll.append(Node(i * 10))

        # Insert at beginning
        ll.insert_on_position(Node(5), 1)
        assert ll.head.value == 5

        # Insert at middle
        ll.insert_on_position(Node(25), 3)
        assert ll.get_value_from_position(3).value == 25

        assert ll.length_iterative() == 5

    def test_delete_from_position(self):
        """Test deleting node from specific position."""
        ll = LinkedList()
        values = [10, 20, 30, 40, 50]
        for val in values:
            ll.append(Node(val))

        # Delete from middle
        ll.delete_from_position(3)
        assert ll.length_iterative() == 4
        assert ll.get_value_from_position(3).value == 40

        # Delete from beginning
        ll.delete_from_position(1)
        assert ll.head.value == 20


class TestLengthOperations:
    """Test length calculation methods."""

    def test_length_iterative_empty(self):
        """Test iterative length on empty list."""
        ll = LinkedList()
        assert ll.length_iterative() == 0

    def test_length_iterative_multiple(self):
        """Test iterative length with multiple nodes."""
        ll = LinkedList()
        for i in range(5):
            ll.append(Node(i))
        assert ll.length_iterative() == 5

    def test_length_recursive_empty(self):
        """Test recursive length on empty list."""
        ll = LinkedList()
        assert ll.length() == 0

    def test_length_recursive_multiple(self):
        """Test recursive length with multiple nodes."""
        ll = LinkedList()
        for i in range(7):
            ll.append(Node(i))
        assert ll.length() == 7

    def test_length_methods_consistency(self):
        """Test that both length methods return same result."""
        ll = LinkedList()
        for i in range(10):
            ll.append(Node(i))

        assert ll.length_iterative() == ll.length()


class TestUtilityMethods:
    """Test utility methods."""

    def test_square_every_value(self):
        """Test squaring every value in the list."""
        ll = LinkedList()
        values = [2, 3, 4, 5]
        for val in values:
            ll.append(Node(val))

        ll.square_every_value()

        expected = [4, 9, 16, 25]
        current = ll.head
        for expected_val in expected:
            assert current.value == expected_val
            current = current.next

    def test_check_if_exists(self):
        """Test checking if value exists in list."""
        ll = LinkedList()
        values = [1, 2, 3, 4, 5]
        for val in values:
            ll.append(Node(val))

        assert ll.check_if_exists(3) is True
        assert ll.check_if_exists(6) is False
        assert ll.check_if_exists(1) is True

    def test_count_nodes_greater_than(self):
        """Test counting nodes with values greater than threshold."""
        ll = LinkedList()
        values = [1, 5, 3, 8, 2, 9, 4]
        for val in values:
            ll.append(Node(val))

        assert ll.count_nodes_greater_than(4) == 3  # 5, 8, 9
        assert ll.count_nodes_greater_than(10) == 0
        assert ll.count_nodes_greater_than(0) == 7

    def test_reverse(self):
        """Test reversing the linked list."""
        ll = LinkedList()
        values = [1, 2, 3, 4, 5]
        for val in values:
            ll.append(Node(val))

        ll.reverse()

        expected = [5, 4, 3, 2, 1]
        current = ll.head
        for expected_val in expected:
            assert current.value == expected_val
            current = current.next


class TestListOperations:
    """Test operations involving multiple lists."""

    def test_concat(self):
        """Test concatenating two lists."""
        ll1 = LinkedList()
        ll2 = LinkedList()

        for i in range(1, 4):
            ll1.append(Node(i))
        for i in range(4, 7):
            ll2.append(Node(i))

        ll1.concat(ll2)

        assert ll1.length_iterative() == 6
        values = []
        current = ll1.head
        while current:
            values.append(current.value)
            current = current.next
        assert values == [1, 2, 3, 4, 5, 6]

    def test_union(self):
        """Test union operation between two lists."""
        ll1 = LinkedList()
        ll2 = LinkedList()

        for val in [1, 2, 3, 4]:
            ll1.append(Node(val))
        for val in [3, 4, 5, 6]:
            ll2.append(Node(val))

        result = ll1.union(ll2)

        # Check that all unique values are present
        values = []
        current = result.head
        while current:
            values.append(current.value)
            current = current.next

        assert set(values) == {1, 2, 3, 4, 5, 6}
        assert len(values) == 6

    def test_intersection(self):
        """Test intersection operation between two lists."""
        ll1 = LinkedList()
        ll2 = LinkedList()

        for val in [1, 2, 3, 4, 5]:
            ll1.append(Node(val))
        for val in [3, 4, 5, 6, 7]:
            ll2.append(Node(val))

        result = ll1.intersection(ll2)

        values = []
        current = result.head
        while current:
            values.append(current.value)
            current = current.next

        assert set(values) == {3, 4, 5}

    def test_equality(self):
        """Test equality comparison between lists."""
        ll1 = LinkedList()
        ll2 = LinkedList()
        ll3 = LinkedList()

        values = [1, 2, 3, 4, 5]
        for val in values:
            ll1.append(Node(val))
            ll2.append(Node(val))

        for val in [1, 2, 3, 4]:
            ll3.append(Node(val))

        assert ll1 == ll2
        assert not (ll1 == ll3)


class TestSpecialOperations:
    """Test special operations like removing every nth element."""

    def test_delete_every_second_node(self):
        """Test deleting every second node."""
        ll = LinkedList()
        values = [1, 2, 3, 4, 5, 6]
        for val in values:
            ll.append(Node(val))

        ll.delete_every_second_node()

        # Should keep 1, 3, 5
        expected = [1, 3, 5]
        current = ll.head
        for expected_val in expected:
            assert current.value == expected_val
            current = current.next

    def test_square_every_second_node(self):
        """Test creating new list with every second node squared."""
        ll = LinkedList()
        values = [2, 5, 8, 3, 7]
        for val in values:
            ll.append(Node(val))

        result = ll.square_every_second_node()

        # Should be [4, 64, 49] (2², 8², 7²)
        expected = [4, 64, 49]
        current = result.head
        for expected_val in expected:
            assert current.value == expected_val
            current = current.next

    def test_squares_even_values(self):
        """Test creating list with squared odd values."""
        ll = LinkedList()
        values = [1, 2, 3, 4, 5, 6]
        for val in values:
            ll.append(Node(val))

        result = ll.squares_even_values()

        # Should square odd values: 1², 3², 5²
        expected = [1, 9, 25]
        current = result.head
        for expected_val in expected:
            assert current.value == expected_val
            current = current.next

    def test_negatives_left_positives_right(self):
        """Test rearranging negatives left, positives right."""
        ll = LinkedList()
        values = [3, -1, 4, -5, 0, 2, -3]
        for val in values:
            ll.append(Node(val))

        ll.negatives_left_positives_right()

        # Check that negatives come first, then zero, then positives
        negative_count = 0
        positive_count = 0
        zero_found = False
        found_positive = False
        found_zero = False

        current = ll.head
        while current:
            if current.value < 0:
                assert not found_positive, "Negative found after positive"
                assert not found_zero, "Negative found after zero"
                negative_count += 1
            elif current.value == 0:
                assert not found_positive, "Zero found after positive"
                zero_found = True
                found_zero = True
            else:
                found_positive = True
                positive_count += 1
            current = current.next

        # Verify we have the right counts
        assert negative_count == 3  # -1, -5, -3
        assert positive_count == 3  # 3, 4, 2
        assert zero_found == True


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_operations_on_empty_list(self):
        """Test various operations on empty list."""
        ll = LinkedList()

        # These should not raise exceptions
        ll.delete_first()
        assert ll.head is None

        ll.delete_last()
        assert ll.head is None

        # Position operations
        assert ll.get_value_from_position(1) is None
        ll.delete_from_position(1)  # Should not crash
        assert ll.head is None

        # Check if exists
        assert ll.check_if_exists(5) is False

        # Count operations
        assert ll.count_nodes_greater_than(0) == 0

        # Min/max operations should return None for empty list
        assert ll.find_minimum_value() is None
        assert ll.find_maximum_value() is None

        # Delete min/max should not crash
        ll.delete_node_with_min_value()
        ll.delete_node_with_max_value()
        assert ll.head is None

    def test_single_node_operations(self):
        """Test operations on single-node list."""
        ll = LinkedList()
        ll.append(Node(42))

        assert ll.find_maximum_value() == 42
        assert ll.find_minimum_value() == 42
        assert ll.length_iterative() == 1
        assert ll.length() == 1

        ll.square_every_value()
        assert ll.head.value == 42 * 42

    def test_invalid_positions(self):
        """Test operations with invalid positions."""
        ll = LinkedList()
        for i in range(1, 4):
            ll.append(Node(i))

        # Invalid position access
        assert ll.get_value_from_position(0) is None
        assert ll.get_value_from_position(-1) is None
        assert ll.get_value_from_position(10) is None

        # Invalid position insertion
        original_length = ll.length_iterative()
        ll.insert_on_position(Node(99), 0)
        ll.insert_on_position(Node(99), -1)
        # Length should remain the same for invalid positions
        assert ll.length_iterative() == original_length


# Fixture for common test data
@pytest.fixture
def sample_list():
    """Create a sample linked list for testing."""
    ll = LinkedList()
    values = [1, 2, 3, 4, 5]
    for val in values:
        ll.append(Node(val))
    return ll


@pytest.fixture
def empty_list():
    """Create an empty linked list for testing."""
    return LinkedList()


# Integration tests using fixtures
class TestWithFixtures:
    """Test using pytest fixtures."""

    def test_sample_list_length(self, sample_list):
        """Test that sample list has correct length."""
        assert sample_list.length_iterative() == 5
        assert sample_list.length() == 5

    def test_empty_list_operations(self, empty_list):
        """Test operations on empty list using fixture."""
        assert empty_list.length_iterative() == 0
        assert empty_list.head is None

        # Add a node and test
        empty_list.append(Node(10))
        assert empty_list.length_iterative() == 1
        assert empty_list.head.value == 10
