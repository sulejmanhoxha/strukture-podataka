# Unit Tests
import pytest

from src.data_structures.stack_queue.queue import Queue


class TestQueue:

    def test_init_empty_queue(self):
        """Test queue initialization"""
        q = Queue()
        assert q.is_empty()
        assert len(q) == 0
        assert q.get_queue() == []
        assert q.max_size is None

    def test_init_with_max_size(self):
        """Test queue initialization with maximum size"""
        q = Queue(max_size=5)
        assert q.max_size == 5
        assert q.remaining_capacity() == 5
        assert not q.is_full()

    def test_enqueue_single_item(self):
        """Test enqueuing a single item"""
        q = Queue()
        q.enqueue("item1")
        assert not q.is_empty()
        assert len(q) == 1
        assert q.get_queue() == ["item1"]

    def test_enqueue_multiple_items(self):
        """Test enqueuing multiple items"""
        q = Queue()
        items = ["a", "b", "c", "d"]
        for item in items:
            q.enqueue(item)
        assert len(q) == 4
        assert q.get_queue() == items

    def test_enqueue_different_types(self):
        """Test enqueuing different data types"""
        q = Queue()
        items = [1, "string", [1, 2, 3], {"key": "value"}, None]
        for item in items:
            q.enqueue(item)
        assert q.get_queue() == items

    def test_enqueue_to_full_queue(self):
        """Test enqueuing to a full queue raises exception"""
        q = Queue(max_size=2)
        q.enqueue("item1")
        q.enqueue("item2")
        with pytest.raises(OverflowError, match="Queue is full"):
            q.enqueue("item3")

    def test_dequeue_single_item(self):
        """Test dequeuing a single item"""
        q = Queue()
        q.enqueue("item1")
        result = q.dequeue()
        assert result == "item1"
        assert q.is_empty()
        assert len(q) == 0

    def test_dequeue_fifo_order(self):
        """Test dequeue follows FIFO (First In, First Out) order"""
        q = Queue()
        items = ["first", "second", "third"]
        for item in items:
            q.enqueue(item)

        results = []
        while not q.is_empty():
            results.append(q.dequeue())

        assert results == items

    def test_dequeue_empty_queue(self):
        """Test dequeuing from empty queue raises exception"""
        q = Queue()
        with pytest.raises(IndexError, match="Cannot dequeue from empty queue"):
            q.dequeue()

    def test_first_peek(self):
        """Test first() method (peek without removing)"""
        q = Queue()
        q.enqueue("item1")
        q.enqueue("item2")

        # First item should be returned but not removed
        assert q.first() == "item1"
        assert len(q) == 2
        assert q.get_queue() == ["item1", "item2"]

    def test_first_empty_queue(self):
        """Test first() on empty queue raises exception"""
        q = Queue()
        with pytest.raises(IndexError, match="Cannot peek at empty queue"):
            q.first()

    def test_is_empty_various_states(self):
        """Test is_empty() in various queue states"""
        q = Queue()
        assert q.is_empty()

        q.enqueue("item")
        assert not q.is_empty()

        q.dequeue()
        assert q.is_empty()

    def test_len_consistency(self):
        """Test that len() stays consistent with actual queue size"""
        q = Queue()
        assert len(q) == 0

        # Add items
        for i in range(5):
            q.enqueue(f"item{i}")
            assert len(q) == i + 1

        # Remove items
        for i in range(5):
            q.dequeue()
            assert len(q) == 4 - i

    def test_get_queue_returns_copy(self):
        """Test that get_queue() returns a copy, not reference"""
        q = Queue()
        q.enqueue("item1")

        queue_copy = q.get_queue()
        queue_copy.append("item2")

        # Original queue should be unchanged
        assert q.get_queue() == ["item1"]
        assert len(q) == 1

    def test_clear(self):
        """Test clear() method"""
        q = Queue()
        q.enqueue("item1")
        q.enqueue("item2")
        q.enqueue("item3")

        q.clear()
        assert q.is_empty()
        assert len(q) == 0
        assert q.get_queue() == []

    def test_is_full_unlimited_queue(self):
        """Test is_full() on unlimited queue"""
        q = Queue()
        assert not q.is_full()

        # Add many items
        for i in range(1000):
            q.enqueue(i)

        assert not q.is_full()

    def test_is_full_limited_queue(self):
        """Test is_full() on limited queue"""
        q = Queue(max_size=3)
        assert not q.is_full()

        q.enqueue("item1")
        assert not q.is_full()

        q.enqueue("item2")
        assert not q.is_full()

        q.enqueue("item3")
        assert q.is_full()

    def test_remaining_capacity(self):
        """Test remaining_capacity() method"""
        q = Queue(max_size=5)
        assert q.remaining_capacity() == 5

        q.enqueue("item1")
        assert q.remaining_capacity() == 4

        q.enqueue("item2")
        q.enqueue("item3")
        assert q.remaining_capacity() == 2

        # Fill to capacity
        q.enqueue("item4")
        q.enqueue("item5")
        assert q.remaining_capacity() == 0

    def test_remaining_capacity_unlimited(self):
        """Test remaining_capacity() on unlimited queue"""
        q = Queue()
        assert q.remaining_capacity() is None

    def test_contains(self):
        """Test contains() method"""
        q = Queue()
        assert not q.contains("item1")

        q.enqueue("item1")
        q.enqueue("item2")

        assert q.contains("item1")
        assert q.contains("item2")
        assert not q.contains("item3")

        q.dequeue()  # Remove "item1"
        assert not q.contains("item1")
        assert q.contains("item2")

    def test_str_representation(self):
        """Test string representation"""
        q = Queue()
        assert str(q) == "Queue([])"

        q.enqueue("item1")
        q.enqueue("item2")
        assert str(q) == "Queue(['item1', 'item2'])"

    def test_repr_representation(self):
        """Test detailed representation"""
        q = Queue(max_size=10)
        q.enqueue("item1")

        repr_str = repr(q)
        assert "Queue(items=['item1']" in repr_str
        assert "size=1" in repr_str
        assert "max_size=10" in repr_str

    def test_equality_comparison(self):
        """Test equality comparison between queues"""
        q1 = Queue()
        q2 = Queue()

        # Empty queues should be equal
        assert q1 == q2

        # Add same items
        q1.enqueue("item1")
        q2.enqueue("item1")
        assert q1 == q2

        # Different items
        q1.enqueue("item2")
        q2.enqueue("item3")
        assert q1 != q2

        # Different max_size
        q3 = Queue(max_size=5)
        q4 = Queue(max_size=10)
        assert q3 != q4

    def test_equality_with_non_queue(self):
        """Test equality comparison with non-Queue objects"""
        q = Queue()
        assert q != []
        assert q != "not a queue"
        assert q != 42

    def test_mixed_operations(self):
        """Test mixed enqueue/dequeue operations"""
        q = Queue()

        # Add some items
        q.enqueue("a")
        q.enqueue("b")
        q.enqueue("c")

        # Remove one
        assert q.dequeue() == "a"

        # Add more
        q.enqueue("d")
        q.enqueue("e")

        # Check order is maintained
        assert q.dequeue() == "b"
        assert q.dequeue() == "c"
        assert q.dequeue() == "d"
        assert q.dequeue() == "e"
        assert q.is_empty()

    def test_stress_operations(self):
        """Test with large number of operations"""
        q = Queue()
        n = 1000

        # Enqueue large number of items
        for i in range(n):
            q.enqueue(i)

        assert len(q) == n

        # Dequeue all items and verify order
        for i in range(n):
            assert q.dequeue() == i

        assert q.is_empty()

    def test_edge_case_zero_max_size(self):
        """Test queue with zero maximum size"""
        q = Queue(max_size=0)
        assert q.is_full()
        assert q.remaining_capacity() == 0

        with pytest.raises(OverflowError):
            q.enqueue("item")

    def test_edge_case_negative_max_size(self):
        """Test queue with negative maximum size"""
        q = Queue(max_size=-1)
        assert q.is_full()  # Any size >= max_size means full

        with pytest.raises(OverflowError):
            q.enqueue("item")
