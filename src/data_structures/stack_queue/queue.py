class Queue:
    def __init__(self, max_size=None):
        """Initialize queue with optional maximum size limit"""
        self.items = []
        self.size = 0
        self.max_size = max_size

    def enqueue(self, item):
        """Adds an item to the queue"""
        if self.max_size is not None and self.size >= self.max_size:
            raise OverflowError("Queue is full")
        self.size = self.size + 1
        return self.items.append(item)

    def dequeue(self):
        """Removes and returns the first item from the queue"""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        self.size = self.size - 1
        return self.items.pop(0)

    def is_empty(self):
        """Returns true if the queue is empty, false otherwise"""
        return len(self.items) == 0

    def first(self):
        """Returns the first item without removing it (peek)"""
        if self.is_empty():
            raise IndexError("Cannot peek at empty queue")
        return self.items[0]

    def get_queue(self):
        """Returns a copy of the items in the queue"""
        return self.items.copy()

    def __len__(self):
        """Returns the size of the queue"""
        return self.size

    def clear(self):
        """Removes all items from the queue"""
        self.items = []
        self.size = 0

    def is_full(self):
        """Returns true if queue has reached maximum capacity"""
        if self.max_size is None:
            return False
        return self.size >= self.max_size

    def remaining_capacity(self):
        """Returns remaining capacity (None if unlimited)"""
        if self.max_size is None:
            return None
        return self.max_size - self.size

    def contains(self, item):
        """Returns true if item is in the queue"""
        return item in self.items

    def __str__(self):
        """String representation of the queue"""
        return f"Queue({self.items})"

    def __repr__(self):
        """Detailed string representation"""
        return f"Queue(items={self.items}, size={self.size}, max_size={self.max_size})"

    def __eq__(self, other):
        """Equality comparison with another queue"""
        if not isinstance(other, Queue):
            return False
        return self.items == other.items and self.max_size == other.max_size
