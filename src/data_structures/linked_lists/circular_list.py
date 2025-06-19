class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head
        if head:
            head.next = head

    def append(self, new_node):
        """adds a node to the end of the list"""
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, new_node):
        """adds a node to the beginning of the list"""
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def find_maximum_value(self):
        """returns the highest(maximum) value of the list"""
        if not self.head:
            return None
        current = self.head
        maximum = current.data
        current = current.next
        while current != self.head:
            if current.data > maximum:
                maximum = current.data
            current = current.next
        return maximum

    def find_minimum_value(self):
        """returns the lowest(minimum) value of the list"""
        if not self.head:
            return None
        current = self.head
        minimum = current.data
        current = current.next
        while current != self.head:
            if current.data < minimum:
                minimum = current.data
            current = current.next
        return minimum

    def delete_node_with_max_value(self):
        """deletes the node with the highest value"""
        max_val = self.find_maximum_value()
        if max_val is not None:
            self.delete_value(max_val)

    def delete_node_with_min_value(self):
        """deletes the node with the lowest(minimum) value"""
        min_val = self.find_minimum_value()
        if min_val is not None:
            self.delete_value(min_val)

    def square_every_value(self):
        """squares the value of every node in the list"""
        if not self.head:
            return
        current = self.head
        current.data = current.data * current.data
        current = current.next
        while current != self.head:
            current.data = current.data * current.data
            current = current.next

    def delete_first(self):
        """deletes the first node of the list"""
        if not self.head:
            return None
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def delete_last(self):
        """deletes the last node of the list"""
        if not self.head:
            return None
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = self.head

    def get_value_from_position(self, position):
        """returns the node from the specified position (1-indexed)"""
        if not self.head or position < 1:
            return None
        current = self.head
        counter = 1
        while counter < position:
            current = current.next
            counter += 1
            if current == self.head:
                return None
        return current

    def insert_on_position(self, new_node, position):
        """inserts a node in the specified position (1-indexed)"""
        if position < 1:
            return None
        if position == 1:
            self.prepend(new_node)
            return
        if not self.head:
            if position == 1:
                self.head = new_node
                new_node.next = new_node
            return
        current = self.head
        counter = 1
        while counter < position - 1:
            current = current.next
            counter += 1
            if current == self.head:
                return None
        new_node.next = current.next
        current.next = new_node

    def delete_value(self, value):
        """deletes a node if its value is equal to the value parameter"""
        if not self.head:
            return
        if self.head.next == self.head:
            if self.head.data == value:
                self.head = None
            return
        if self.head.data == value:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        current = self.head
        while current.next != self.head:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def delete_from_position(self, position):
        """deletes a value that is in the specified position (1-indexed)"""
        if not self.head or position < 1:
            return None
        if position == 1:
            self.delete_first()
            return
        current = self.head
        counter = 1
        while counter < position - 1:
            current = current.next
            counter += 1
            if current.next == self.head:
                return None
        if current.next == self.head:
            return None
        current.next = current.next.next

    def length_iterative(self):
        """returns the length of the list. this is the iterative version"""
        if not self.head:
            return 0
        count = 1
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next
        return count

    def length(self):
        """returns the length of the list. this is the recursive version"""
        if not self.head:
            return 0
        return self.length_recursive(self.head.next, 1)

    def length_recursive(self, node, count):
        """helper for recursive length calculation"""
        if node == self.head:
            return count
        else:
            return self.length_recursive(node.next, count + 1)

    def print_list(self):
        """prints the list as one line"""
        if not self.head:
            print("[ ]")
            return
        current = self.head
        string = "[ "
        string += str(current.data)
        current = current.next
        while current != self.head:
            string += "  ➝  " + str(current.data)
            current = current.next
        string += " ] (circular)"
        print(string)

    def print_list_2(self):
        """prints the list vertically"""
        if not self.head:
            return
        current = self.head
        print(current.data)
        current = current.next
        while current != self.head:
            print(current.data)
            current = current.next

    def check_if_exists(self, value):
        """returns true if a value is found on the list, returns false otherwise"""
        if not self.head:
            return False
        current = self.head
        if current.data == value:
            return True
        current = current.next
        while current != self.head:
            if current.data == value:
                return True
            current = current.next
        return False

    def count_nodes_greater_than(self, num):
        """counts the number of nodes with values higher than the given argument"""
        if not self.head:
            return 0
        count = 0
        current = self.head
        if current.data > num:
            count += 1
        current = current.next
        while current != self.head:
            if current.data > num:
                count += 1
            current = current.next
        return count

    def delete_every_second_node(self):
        """deletes every second node of the list. begins from the second node"""
        if not self.head or self.head.next == self.head:
            return
        current = self.head
        while current.next != self.head and current.next.next != self.head:
            current.next = current.next.next
            current = current.next

    def reverse(self):
        """reverses a circular list"""
        if not self.head or self.head.next == self.head:
            return

        # Find the last node
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next

        # Break the circular connection temporarily
        last_node.next = None

        # Reverse the linear list
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Update head to the new first node (which was the last node)
        self.head = prev

        # Restore circular connection: original head (now last) points to new head
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = self.head

    def concat(self, other):
        """concatenates/joins two circular lists"""
        if not self.head:
            self.head = other.head
            return
        if not other.head:
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        other_last = other.head
        while other_last.next != other.head:
            other_last = other_last.next
        current.next = other.head
        other_last.next = self.head

    def __eq__(self, other):
        """checks if two circular lists are equal"""
        if self.length_iterative() != other.length_iterative():
            return False
        if not self.head and not other.head:
            return True
        if not self.head or not other.head:
            return False
        c1 = self.head
        c2 = other.head
        if c1.data != c2.data:
            return False
        c1 = c1.next
        c2 = c2.next
        while c1 != self.head and c2 != other.head:
            if c1.data != c2.data:
                return False
            c1 = c1.next
            c2 = c2.next
        return c1 == self.head and c2 == other.head
