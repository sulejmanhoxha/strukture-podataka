class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def prepend(self, new_element):
        """adds a node to the beginning of the list"""
        new_element.next = self.head
        self.head = new_element

    def append(self, new_element):
        """adds a node to the end of the list"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def find_maximum_value(self):
        """returns the highest(maximum) value of the list"""
        if not self.head:
            return None
        current = self.head
        maksimum = current.value
        while current:
            if maksimum < current.value:
                maksimum = current.value
            current = current.next

        return maksimum

    def delete_node_with_max_value(self):
        """deletes the node with the highest value"""
        max_val = self.find_maximum_value()
        if max_val is not None:
            self.delete_value(max_val)

    def find_minimum_value(self):
        """returns the lowest(minimum) value of the list"""
        if not self.head:
            return None
        current = self.head
        minimum = current.value
        while current:
            if current.value < minimum:
                minimum = current.value
            current = current.next
        return minimum

    def delete_node_with_min_value(self):
        """deletes the node with the lowest(minimum) value"""
        min_val = self.find_minimum_value()
        if min_val is not None:
            self.delete_value(min_val)

    def square_every_value(self):
        """squares the value of every node in the list"""
        current = self.head
        while current:
            current.value = current.value * current.value
            current = current.next

    def delete_first(self):
        """deletes the first node of the list"""
        if not self.head:
            return None
        self.head = self.head.next

    def delete_last(self):
        """deletes the last node of the list"""
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def remove_every_third_element(linked_list):
        """deletes every third element of the list"""
        if not linked_list.head or not linked_list.head.next:
            return linked_list

        current = linked_list.head
        while current and current.next:
            if current.next.next is None or current.next.next.next is None:
                current.next = None
                break
            else:
                current.next = current.next.next.next
                current = current.next

    def get_value_from_position(self, position):
        """returns the node from the specified position"""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter = counter + 1
        return None

    def insert_on_position(self, new_element, position):
        """inserts a node in the specified position"""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter = counter + 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            return None

    def delete_value(self, value):
        """deletes a node if it's value is equal to the value parameter"""
        if not self.head:
            return

        current = self.head
        prev = None

        while current and current.value != value:
            prev = current
            current = current.next

        if current and current.value == value:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

    def delete_from_position(self, position):
        """deletes a value that is in the specified position"""
        if not self.head or position < 1:
            return None

        current = self.head
        prev = None
        counter = 1

        if position == 1:
            self.head = current.next
            current = None
            return

        while current and counter != position:
            prev = current
            current = current.next
            counter = counter + 1

        if current is None:
            return None

        prev.next = current.next
        current = None

    def length_iterative(self):
        """returns the length of the list. this is the iterative version"""
        count = 0
        current = self.head

        while current:
            current = current.next
            count = count + 1

        return count

    def length(self):
        """returns the length of the list. this is the recursive version"""
        return self.length_recursive(self.head)

    def length_recursive(self, node):
        """call the length function not this. otherwise give list head as the argument"""
        if not node:
            return 0
        else:
            return 1 + self.length_recursive(node.next)

    def print_list_2(self):
        """prints the list vertically"""
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def print_list(self):
        """prints the list as one line"""
        current = self.head
        string = "[ "
        while current:
            if current.next is None:
                string = string + str(current.value) + " ]"
            else:
                string = string + str(current.value) + "  ➝  "

            current = current.next
        print(string)

    def concat(self, other):
        """concatenates/joins two lists"""
        if not self.head:
            self.head = other.head
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = other.head

    def delete_every_second_node(self):
        """deletes every second node of the list. begins from the second node [5,3,4,9] - result: [5,4]"""
        if not self.head:
            return

        current = self.head
        while current and current.next:
            if current.next.next is None:
                current.next = None
                break
            current.next = current.next.next
            current = current.next

        self.print_list()

    def negatives_left_positives_right(self):
        """rearranges the current list with negative values on the left and positive values on the right. *THE LIST IS NOT SORTED*"""
        if not self.head:
            return

        # Create temporary lists for negatives, zero, and positives
        negatives = []
        positives = []
        has_zero = False

        # Collect values
        current = self.head
        while current:
            if current.value < 0:
                negatives.append(current.value)
            elif current.value > 0:
                positives.append(current.value)
            else:
                has_zero = True
            current = current.next

        # Rebuild the list
        self.head = None

        # Add negatives first
        for val in negatives:
            self.append(Node(val))

        # Add zero if it exists
        if has_zero:
            self.append(Node(0))

        # Add positives last
        for val in positives:
            self.append(Node(val))

    def check_if_exists(self, value):
        """returns true if a value is found on the list, returns false otherwise"""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def count_nodes_greater_than(self, num):
        """counts the number of nodes with values higher than the given argument"""
        current = self.head
        count = 0
        while current:
            if current.value > num:
                count = count + 1
            current = current.next
        return count

    def union(self, l2):
        """creates a new list, union(math) between the called list and the argument list"""
        current = self.head
        l3 = LinkedList()
        unique_values = set()

        while current:
            if not current.value in unique_values:
                l3.append(Node(current.value))
                unique_values.add(current.value)
            current = current.next

        current = l2.head
        while current:
            if not current.value in unique_values:
                l3.append(Node(current.value))
                unique_values.add(current.value)
            current = current.next

        l3.print_list()
        return l3

    def intersection(self, l2):
        """returns a new list with only the nodes that have the same value on both lists the called list and the argument list"""
        unique_values = set()
        l3 = LinkedList()
        current = self.head

        while current:
            unique_values.add(current.value)
            current = current.next

        current = l2.head
        while current:
            if current.value in unique_values:
                l3.append(Node(current.value))
            current = current.next

        l3.print_list()
        return l3

    def squares_even_values(self):
        """Returns a linked list made of only nodes that have odd numbers and then squares them, from the called list"""
        lista2 = LinkedList()
        current = self.head
        while current:
            if current.value % 2 == 1:  # odd numbers
                lista2.append(Node(current.value**2))
            current = current.next
        lista2.print_list()
        return lista2

    def square_every_second_node(self):
        """Returns a new list, containing every second squared node from the called list. Begins from the first node.

        [2, 5, 8, 3, 7] - [4, 64, 49]
        """
        lista2 = LinkedList()
        current = self.head
        while current:
            node = Node(current.value**2)
            lista2.append(node)
            if current.next:
                current = current.next.next
            else:
                break
        lista2.print_list()
        return lista2

    def reverse(self):
        """reverses a list"""
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def __eq__(self, l2):
        if self.length_iterative() != l2.length_iterative():
            return False
        else:
            c1 = self.head
            c2 = l2.head
            while c1 and c2:
                if c1.value != c2.value:
                    return False
                c1 = c1.next
                c2 = c2.next
            return True
