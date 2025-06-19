class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_list_2(self):
        """prints the list vertically"""
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def print_list(self):
        """prints the list in one line"""
        current = self.head
        string = "[ "
        while current:
            if current.next is None:
                string = string + str(current.value) + " ]"
            else:
                string = string + str(current.value) + "   ⇄   "
            current = current.next

        # Handle empty list case
        if self.head is None:
            string = string + "]"

        print(string)

    def print_list_reversed_2(self):
        """prints the list in reverse order vertically"""
        if self.head is None:
            return

        current = self.head
        while current.next:
            current = current.next
        print(current.value)
        while current.prev:
            print(current.prev.value)
            current = current.prev

    def print_list_reversed(self):
        """print the list in reverse order in one line"""
        if self.head is None:
            print("Reversed list: [ ]")
            return

        current = self.head
        while current.next:
            current = current.next
        string = "Reversed list: [ "
        while current:
            if current.prev is None:
                string = string + str(current.value) + " ]"
            else:
                string = string + str(current.value) + "   ⇄   "
            current = current.prev
        print(string)

    def prepend(self, new_node):
        """adds a node to the beginning of the list"""
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, new_node):
        """adds a node to the end of the list"""
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur
        new_node.next = None

    def delete_first(self):
        """deletes the first node"""
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        """deletes the last element of the list"""
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next:
            current = current.next

        # Fix: properly disconnect the last node
        current.prev.next = None

    def get_middle_node(self):
        """returns the middle node of the list"""
        if self.head is None:
            return None

        current_1 = self.head
        current_2 = self.head

        while current_1.next and current_1.next.next:
            current_1 = current_1.next.next
            current_2 = current_2.next

        return current_2

    def __eq__(self, other):
        """returns True if the lists are the same, False otherwise"""
        current_1 = self.head
        current_2 = other.head
        while current_1 and current_2:
            if current_1.value == current_2.value:
                current_1 = current_1.next
                current_2 = current_2.next
            else:
                return False

        if not current_1 and not current_2:
            return True
        else:
            return False

    def intersection(self, l2):
        """returns a new list with only the nodes that have the same value on both lists"""
        current_1 = self.head
        l3 = DoublyLinkedList()
        while current_1:
            current_2 = l2.head
            while current_2:
                if current_1.value == current_2.value:
                    l3.append(Node(current_1.value))
                    break
                current_2 = current_2.next
            current_1 = current_1.next
        return l3

    def append_sort(self, n):
        """works only for the knjigja example or if we have dictionaries with key cijena"""
        current = self.head
        if current == None or n.value["cijena"] < current.value["cijena"]:
            self.prepend(n)
            return
        while current.next:
            if current.value["cijena"] < n.value["cijena"] and current.next.value["cijena"] > n.value["cijena"]:
                tmp = current.next
                current.next = n
                n.next = tmp
                tmp.prev = n
                n.prev = current
                break
            current = current.next
        current.next = n
        n.prev = current

    def duzina(self):
        """helper method to get length of the list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def izbaci(self, N):
        """removes N nodes from the end of the list"""
        p = 0
        if N >= self.duzina():
            while self.head != None:
                temp = self.head
                self.head = self.head.next
                temp = None
                p = p + 1
            return p
        else:
            n = 0
            while N != n:
                if self.head is None:
                    return
                if self.head.next is None:
                    self.head = None
                    return n + 1
                current = self.head
                while current.next:
                    current = current.next
                current.prev.next = None
                n = n + 1
            return n

    def remove_duplicates(self):
        """removes duplicate values from the list"""
        if self.head is None:
            return

        current_1 = self.head

        while current_1 and current_1.next:
            current_2 = current_1

            while current_2.next:
                if current_2.next.value == current_1.value:
                    # Remove the duplicate node
                    duplicate = current_2.next
                    current_2.next = duplicate.next
                    if duplicate.next:
                        duplicate.next.prev = current_2
                else:
                    current_2 = current_2.next

            current_1 = current_1.next

    def remove_duplicates_une(self):
        """removes duplicate values using a dictionary to track seen values"""
        if self.head is None:
            return

        values = {}
        current = self.head

        while current:
            if current.value not in values:
                values[current.value] = current
                current = current.next
            else:
                # Remove duplicate node
                if current.prev:
                    current.prev.next = current.next
                else:
                    # Current is head
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                current = current.next
