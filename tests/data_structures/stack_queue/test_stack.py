import pytest

from src.data_structures.stack_queue.stack import Stack


class TestStackBasicOperations:
    """Test basic stack operations"""

    def test_init(self):
        """Test stack initialization"""
        stack = Stack()
        assert stack.is_empty() is True
        assert stack.size() == 0
        assert stack.get_stack_items() == []

    def test_push_single_item(self):
        """Test pushing a single item"""
        stack = Stack()
        stack.push(5)
        assert stack.is_empty() is False
        assert stack.size() == 1
        assert stack.get_stack_items() == [5]

    def test_push_multiple_items(self):
        """Test pushing multiple items"""
        stack = Stack()
        items = [1, 2, 3, 4, 5]
        for item in items:
            stack.push(item)
        assert stack.size() == 5
        assert stack.get_stack_items() == items

    def test_push_different_types(self):
        """Test pushing different data types"""
        stack = Stack()
        items = [1, "hello", [1, 2, 3], {"key": "value"}, None, True]
        for item in items:
            stack.push(item)
        assert stack.get_stack_items() == items

    def test_pop_single_item(self):
        """Test popping a single item"""
        stack = Stack()
        stack.push(10)
        popped = stack.pop()
        assert popped == 10
        assert stack.is_empty() is True

    def test_pop_multiple_items(self):
        """Test popping multiple items (LIFO order)"""
        stack = Stack()
        items = [1, 2, 3, 4, 5]
        for item in items:
            stack.push(item)

        popped_items = []
        while not stack.is_empty():
            popped_items.append(stack.pop())

        assert popped_items == [5, 4, 3, 2, 1]  # LIFO order

    def test_pop_empty_stack(self):
        """Test popping from empty stack raises exception"""
        stack = Stack()
        with pytest.raises(IndexError, match="pop from empty stack"):
            stack.pop()

    def test_peek_single_item(self):
        """Test peeking at single item"""
        stack = Stack()
        stack.push(42)
        peeked = stack.peek()
        assert peeked == 42
        assert stack.size() == 1  # Item should still be in stack

    def test_peek_multiple_items(self):
        """Test peeking returns top item without removing it"""
        stack = Stack()
        items = [1, 2, 3]
        for item in items:
            stack.push(item)

        peeked = stack.peek()
        assert peeked == 3  # Last pushed item
        assert stack.size() == 3  # Size unchanged
        assert stack.get_stack_items() == items

    def test_peek_empty_stack(self):
        """Test peeking at empty stack raises exception"""
        stack = Stack()
        with pytest.raises(IndexError, match="peek from empty stack"):
            stack.peek()

    def test_is_empty_operations(self):
        """Test is_empty method in various scenarios"""
        stack = Stack()
        assert stack.is_empty() is True

        stack.push(1)
        assert stack.is_empty() is False

        stack.pop()
        assert stack.is_empty() is True

        # Add multiple items
        for i in range(5):
            stack.push(i)
        assert stack.is_empty() is False

        # Remove all items
        for i in range(5):
            stack.pop()
        assert stack.is_empty() is True


class TestStackAdvancedOperations:
    """Test advanced stack operations"""

    def test_get_stack_items_returns_copy(self):
        """Test that get_stack_items returns a copy, not reference"""
        stack = Stack()
        items = [1, 2, 3]
        for item in items:
            stack.push(item)

        stack_items = stack.get_stack_items()
        stack_items.append(999)  # Modify the returned list

        # Original stack should be unchanged
        assert stack.get_stack_items() == [1, 2, 3]

    def test_size_method(self):
        """Test size method with various operations"""
        stack = Stack()
        assert stack.size() == 0

        # Add items
        for i in range(10):
            stack.push(i)
            assert stack.size() == i + 1

        # Remove items
        for i in range(10):
            assert stack.size() == 10 - i
            stack.pop()

        assert stack.size() == 0

    def test_create_copy_of_stack(self):
        """Test creating a copy of stack"""
        original = Stack()
        items = [1, 2, 3, 4, 5]
        for item in items:
            original.push(item)

        copy = original.create_copy_of_stack()

        # Copy should have same items in same order
        assert copy.get_stack_items() == original.get_stack_items()
        assert copy.size() == original.size()

        # But should be different objects
        assert copy is not original

        # Modifying copy shouldn't affect original
        copy.push(999)
        assert original.size() == 5
        assert copy.size() == 6

    def test_create_copy_empty_stack(self):
        """Test creating copy of empty stack"""
        original = Stack()
        copy = original.create_copy_of_stack()

        assert copy.is_empty() is True
        assert copy.size() == 0

    def test_reverse_stack(self):
        """Test reversing stack"""
        stack = Stack()
        items = [1, 2, 3, 4, 5]
        for item in items:
            stack.push(item)

        stack.reverse()
        assert stack.get_stack_items() == [5, 4, 3, 2, 1]

    def test_reverse_empty_stack(self):
        """Test reversing empty stack"""
        stack = Stack()
        stack.reverse()
        assert stack.is_empty() is True

    def test_reverse_single_item(self):
        """Test reversing stack with single item"""
        stack = Stack()
        stack.push(42)
        stack.reverse()
        assert stack.get_stack_items() == [42]


class TestDivideOddEven:
    """Test divide_odd_even functionality"""

    def test_divide_odd_even_basic(self):
        """Test basic odd/even division"""
        stack = Stack()
        odd_stack = Stack()
        even_stack = Stack()

        numbers = [1, 2, 3, 4, 5, 6]
        for num in numbers:
            stack.push(num)

        stack.divide_odd_even(odd_stack, even_stack)

        # Original stack should be empty
        assert stack.is_empty() is True

        # Check odd stack (order will be reversed due to stack nature)
        odd_items = []
        while not odd_stack.is_empty():
            odd_items.append(odd_stack.pop())
        assert set(odd_items) == {1, 3, 5}

        # Check even stack
        even_items = []
        while not even_stack.is_empty():
            even_items.append(even_stack.pop())
        assert set(even_items) == {2, 4, 6}

    def test_divide_odd_even_all_odd(self):
        """Test with all odd numbers"""
        stack = Stack()
        odd_stack = Stack()
        even_stack = Stack()

        odd_numbers = [1, 3, 5, 7, 9]
        for num in odd_numbers:
            stack.push(num)

        stack.divide_odd_even(odd_stack, even_stack)

        assert even_stack.is_empty() is True
        assert odd_stack.size() == 5

    def test_divide_odd_even_all_even(self):
        """Test with all even numbers"""
        stack = Stack()
        odd_stack = Stack()
        even_stack = Stack()

        even_numbers = [2, 4, 6, 8, 10]
        for num in even_numbers:
            stack.push(num)

        stack.divide_odd_even(odd_stack, even_stack)

        assert odd_stack.is_empty() is True
        assert even_stack.size() == 5

    def test_divide_odd_even_empty_stack(self):
        """Test with empty stack"""
        stack = Stack()
        odd_stack = Stack()
        even_stack = Stack()

        stack.divide_odd_even(odd_stack, even_stack)

        assert stack.is_empty() is True
        assert odd_stack.is_empty() is True
        assert even_stack.is_empty() is True

    def test_divide_odd_even_non_numeric(self):
        """Test with non-numeric values"""
        stack = Stack()
        odd_stack = Stack()
        even_stack = Stack()

        items = ["hello", [1, 2], {"key": "value"}, None]
        for item in items:
            stack.push(item)

        stack.divide_odd_even(odd_stack, even_stack)

        # Non-numeric items should go to odd_stack
        assert odd_stack.size() == 4
        assert even_stack.is_empty() is True

    def test_divide_odd_even_mixed_types(self):
        """Test with mixed numeric and non-numeric values"""
        stack = Stack()
        odd_stack = Stack()
        even_stack = Stack()

        items = [1, "hello", 2, 3, [1, 2], 4]
        for item in items:
            stack.push(item)

        stack.divide_odd_even(odd_stack, even_stack)

        # Should have some items in both stacks
        assert not odd_stack.is_empty()
        assert not even_stack.is_empty()

    def test_divide_odd_even_invalid_arguments(self):
        """Test with invalid arguments"""
        stack = Stack()
        stack.push(1)

        with pytest.raises(TypeError, match="Arguments must be Stack instances"):
            stack.divide_odd_even("not_a_stack", Stack())

        with pytest.raises(TypeError, match="Arguments must be Stack instances"):
            stack.divide_odd_even(Stack(), "not_a_stack")


class TestRemoveValue:
    """Test remove_value_from_stack functionality"""

    def test_remove_value_basic(self):
        """Test basic value removal"""
        stack = Stack()
        items = [1, 2, 3, 2, 4, 2, 5]
        for item in items:
            stack.push(item)

        clean_stack, removed_count = stack.remove_value_from_stack(2)

        assert removed_count == 3
        clean_items = clean_stack.get_stack_items()
        assert 2 not in clean_items
        assert set(clean_items) == {1, 3, 4, 5}

    def test_remove_value_not_found(self):
        """Test removing value that doesn't exist"""
        stack = Stack()
        items = [1, 3, 5, 7]
        for item in items:
            stack.push(item)

        clean_stack, removed_count = stack.remove_value_from_stack(2)

        assert removed_count == 0
        assert clean_stack.get_stack_items() == items

    def test_remove_value_empty_stack(self):
        """Test removing from empty stack"""
        stack = Stack()
        clean_stack, removed_count = stack.remove_value_from_stack(5)

        assert removed_count == 0
        assert clean_stack.is_empty() is True

    def test_remove_all_values(self):
        """Test removing all values from stack"""
        stack = Stack()
        items = [2, 2, 2, 2]
        for item in items:
            stack.push(item)

        clean_stack, removed_count = stack.remove_value_from_stack(2)

        assert removed_count == 4
        assert clean_stack.is_empty() is True

    def test_remove_value_different_types(self):
        """Test removing different data types"""
        stack = Stack()
        items = [1, "hello", 2, "hello", 3]
        for item in items:
            stack.push(item)

        clean_stack, removed_count = stack.remove_value_from_stack("hello")

        assert removed_count == 2
        clean_items = clean_stack.get_stack_items()
        assert "hello" not in clean_items
        assert set(clean_items) == {1, 2, 3}


class TestBinaryConversion:
    """Test convert_to_binary static method"""

    def test_convert_zero(self):
        """Test converting zero"""
        result = Stack.convert_to_binary(0)
        assert result == "0"

    def test_convert_small_numbers(self):
        """Test converting small numbers"""
        test_cases = {1: "1", 2: "10", 3: "11", 4: "100", 5: "101", 8: "1000", 15: "1111", 16: "10000"}

        for number, expected in test_cases.items():
            result = Stack.convert_to_binary(number)
            assert result == expected, f"Failed for {number}: got {result}, expected {expected}"

    def test_convert_large_numbers(self):
        """Test converting large numbers"""
        test_cases = {255: "11111111", 256: "100000000", 1023: "1111111111", 1024: "10000000000"}

        for number, expected in test_cases.items():
            result = Stack.convert_to_binary(number)
            assert result == expected

    def test_convert_negative_number(self):
        """Test converting negative number raises error"""
        with pytest.raises(ValueError, match="Input must be a non-negative integer"):
            Stack.convert_to_binary(-1)

    def test_convert_non_integer(self):
        """Test converting non-integer raises error"""
        with pytest.raises(ValueError, match="Input must be a non-negative integer"):
            Stack.convert_to_binary(3.14)

        with pytest.raises(ValueError, match="Input must be a non-negative integer"):
            Stack.convert_to_binary("5")


class TestSeparateEvenOdd:
    """Test separate_even_odd functionality"""

    def test_separate_even_odd_basic(self):
        """Test basic even/odd separation"""
        stack = Stack()
        odd_stack = Stack()

        numbers = [1, 2, 3, 4, 5, 6]
        for num in numbers:
            stack.push(num)

        even_stack, odd_stack = stack.separate_even_odd(odd_stack)

        # Original stack should be empty
        assert stack.is_empty() is True

        # Collect items from both stacks
        even_items = []
        while not even_stack.is_empty():
            even_items.append(even_stack.pop())

        odd_items = []
        while not odd_stack.is_empty():
            odd_items.append(odd_stack.pop())

        # Check separation
        for item in even_items:
            assert item % 2 == 0

        for item in odd_items:
            assert item % 2 == 1

    def test_separate_even_odd_invalid_argument(self):
        """Test with invalid argument"""
        stack = Stack()
        stack.push(1)

        with pytest.raises(TypeError, match="Argument must be a Stack instance"):
            stack.separate_even_odd("not_a_stack")


class TestStackComparison:
    """Test stack comparison and string representation"""

    def test_equality(self):
        """Test stack equality comparison"""
        stack1 = Stack()
        stack2 = Stack()

        # Empty stacks should be equal
        assert stack1 == stack2

        # Add same items to both
        items = [1, 2, 3]
        for item in items:
            stack1.push(item)
            stack2.push(item)

        assert stack1 == stack2

        # Different stacks should not be equal
        stack2.push(4)
        assert stack1 != stack2

        # Compare with non-stack object
        assert stack1 != [1, 2, 3]

    def test_string_representation(self):
        """Test string representation"""
        stack = Stack()
        items = [1, 2, 3]
        for item in items:
            stack.push(item)

        str_repr = str(stack)
        assert "Stack" in str_repr
        assert "1" in str_repr and "2" in str_repr and "3" in str_repr

        repr_str = repr(stack)
        assert "Stack" in repr_str
        assert "items" in repr_str


class TestEdgeCases:
    """Test various edge cases"""

    def test_large_stack(self):
        """Test with large number of items"""
        stack = Stack()
        large_number = 10000

        # Push many items
        for i in range(large_number):
            stack.push(i)

        assert stack.size() == large_number
        assert not stack.is_empty()

        # Pop all items and verify order
        for i in range(large_number - 1, -1, -1):
            assert stack.pop() == i

        assert stack.is_empty()

    def test_alternating_operations(self):
        """Test alternating push/pop operations"""
        stack = Stack()

        for i in range(100):
            stack.push(i)  # Push i
            if i > 0:  # Don't pop from empty stack
                popped = stack.pop()  # Pop the item we just pushed
                assert popped == i

        # Stack should have one item (0)
        assert stack.size() == 1
        assert stack.peek() == 0


class TestErrorHandling:
    """Test error handling scenarios"""

    def test_multiple_pops_on_empty(self):
        """Test multiple pop attempts on empty stack"""
        stack = Stack()

        # Multiple attempts should all raise errors
        for _ in range(3):
            with pytest.raises(IndexError):
                stack.pop()

    def test_multiple_peeks_on_empty(self):
        """Test multiple peek attempts on empty stack"""
        stack = Stack()

        # Multiple attempts should all raise errors
        for _ in range(3):
            with pytest.raises(IndexError):
                stack.peek()

    def test_operations_after_error(self):
        """Test that stack works normally after error"""
        stack = Stack()

        # Cause an error
        with pytest.raises(IndexError):
            stack.pop()

        # Stack should still work normally
        stack.push(42)
        assert stack.peek() == 42
        assert stack.pop() == 42
        assert stack.is_empty() is True


# Pytest fixtures for common test data
@pytest.fixture
def empty_stack():
    """Fixture providing an empty stack"""
    return Stack()


@pytest.fixture
def populated_stack():
    """Fixture providing a stack with some data"""
    stack = Stack()
    for i in [1, 2, 3, 4, 5]:
        stack.push(i)
    return stack


@pytest.fixture
def mixed_type_stack():
    """Fixture providing a stack with mixed data types"""
    stack = Stack()
    items = [1, "hello", [1, 2], {"key": "value"}, None, True, 3.14]
    for item in items:
        stack.push(item)
    return stack


# Integration tests using fixtures
class TestWithFixtures:
    """Test using pytest fixtures"""

    def test_empty_stack_fixture(self, empty_stack):
        """Test empty stack fixture"""
        assert empty_stack.is_empty() is True
        assert empty_stack.size() == 0

    def test_populated_stack_fixture(self, populated_stack):
        """Test populated stack fixture"""
        assert not populated_stack.is_empty()
        assert populated_stack.size() == 5
        assert populated_stack.peek() == 5

    def test_mixed_type_stack_fixture(self, mixed_type_stack):
        """Test mixed type stack fixture"""
        assert mixed_type_stack.size() == 7
        assert not mixed_type_stack.is_empty()

    def test_copy_preserves_original(self, populated_stack):
        """Test that copying preserves original stack"""
        original_size = populated_stack.size()
        copy = populated_stack.create_copy_of_stack()

        # Modify copy
        copy.push(999)

        # Original should be unchanged
        assert populated_stack.size() == original_size


if __name__ == "__main__":
    pytest.main([__file__])
