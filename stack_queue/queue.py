class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, item):
        '''adds an item to the queue'''
        self.size = self.size + 1
        return self.items.append(item)

    def dequeue(self):
        '''removes and returns the first(right)item from the queue'''
        if not self.is_empty():
            self.size = self.size - 1
            return self.items.pop(0)

    def is_empty(self):
        '''returns true if the queue is empty, false otherwise'''
        return len(self.items) == 0

    def first(self):
        '''same sa dequeue except it doesnt remove the item'''
        if not self.is_empty():
            return self.items[0]

    def get_queue(self):
        '''returns the items in the queue'''
        return self.items

    def __len__(self):
        '''returns the size of the queue'''
        return self.size


q = Queue()
print(q.is_empty())
q.enqueue("Wake up")
q.enqueue("Have coffee")
q.enqueue("Have a shower")
q.enqueue("Get dress")
q.enqueue("Go to breakfast")
q.enqueue("Go to faculty")

print(q.get_queue())

print(q.dequeue())
print(q.first())
