class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    # za listu koju hocemo da dodajemo i tail
    # def __init__(self, head=None, tail=None):
    #     self.head = head
    #     self.tail = tail

    def print_list_2(self):
        '''prints the list vertically'''
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def print_list(self):
        '''prints the list in one line'''
        current = self.head
        string = "[ "
        while current:
            if current.next is None:
                string = string + str(current.value) + " ]"
            else:
                string = string + str(current.value) + "   ⇄   "

            current = current.next
        print(string)

    def print_list_reversed_2(self):
        '''prints the list in reverse order vertically'''
        current = self.head
        while current.next:
            current = current.next
        print(current.value)
        while current.prev:
            print(current.prev.value)
            current = current.prev

    def print_list_reversed(self):
        '''print the list in reverse order in one line'''
        current = self.head
        while current.next:
            current = current.next
        string = 'Reversed list: [ '
        while current:
            if current.prev is None:
                string = string + str(current.value) + " ]"
            else:
                string = string + str(current.value) + "   ⇄   "

            current = current.prev
        print(string)

    def prepend(self, new_node):
        '''adds a node to the beginning of the list'''
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, new_node):
        '''adds a node to the end of the list'''
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
        '''deletes the first node'''
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None

        self.head = self.head.next
        self.prev = None

    def delete_last(self):
        '''deletes the last element of the list'''
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None

        current = self.head
        while current.next:
            current = current.next

        current.prev = None
        current.prev.next = None

    def get_middle_node(self):
        '''returns the middle node of the list'''
        current_1 = self.head
        current_2 = self.head

        while current_1.next:
            current_1 = current_1.next.next
            current_2 = current_2.next

        return current_2

    def __eq__(self, other):
        '''returns True if the lists are the same, False otherwise'''
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
        '''returns a new list with only the nodes that have the same value on both lists the called list and the argument list'''
        current_1 = self.head
        l3 = DoublyLinkedList()
        while current_1:
            current_2 = l2.head
            while current_2:
                if current_1.value == current_2.value:
                    l3.append(current_1)
                current_2 = current_2.next
            current_1 = current_1.next
        l3.print_list()

    def append_sort(self, n):
        '''works only for the knjigja example or if we have dictionaries with key cijena'''
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

#     1. U  dvostruko  povezanu  listu  smještaju  se  cjelobrojni  podaci.
# Napisati funkciju izbaciN (head, tail, N), head pokazivac na prvi,
# a tail pokazivac na poslednji element liste, N broj elemenata liste,
# koja će iz liste izbaciti zadnjih N elemenata. Ako u listi ima
# manje od N elemenata, funkcija ih treba izbaciti sve. Funkcija
# treba vratiti broj izbacenih elemenata

    # un
    # def izbaciN(head, tail, N):
    #     current = head
    #     counter = 0
    #     while counter < N and current != tail:
    #         counter = counter + 1
    #         current = current.next

    #     if counter != N:
    #         head = None
    #         print("Lista ima manje od N elemenata")
    #     else:
    #         current.next = tail
    # profi (dopt)
    def izbaci(self, N):
        p = 0
        if N >= self.duzina():
            while (self.head != None):
                temp = self.head
                self.head = self.head.next
                temp = None
                p = p+1
            return p
        else:
            n = 0
            while N != n:
                if self.head is None:
                    return
                if self.head.next is None:
                    self.head = None
                current = self.head
                while current.next:
                    current = current.next
                current.prev.next = None
                current.prev = None
                n = n+1

            return n

    def remove_duplicates(self):
        current_1 = self.head
        current_2 = self.head

        while current_1.next:
            while current_2.next:
                if current_2.next.value == current_1.value:
                    current_2.next = current_2.next.next
                else:
                    current_2 = current_2.next
            current_1 = current_1.next
            current_2 = current_1

    def remove_duplicates_une(self):
        values = {}

        current = self.head

        while current:
            if current.next is None:
                if current.value not in values:
                    return
                else:
                    current.prev.next = None
                return

            if current.value not in values:
                values[current.value] = current
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

            current = current.next


# knjige = DoublyLinkedList()

# knjige = DoublyLinkedList()
# knjiga1 = Node({"idk": 1, "nk": "Stranac", "ida": 5, "cijena": 5})
# knjiga2 = Node({"idk": 2, "nk": "Zlocin i kazna", "ida": 3, "cijena": 10})
# knjiga3 = Node({"idk": 3, "nk": "Ana Karenjina", "ida": 7, "cijena": 15})
# knjiga4 = Node({"idk": 4, "nk": "Zapisi iz podzemlja", "ida": 3, "cijena": 12})
# knjiga5 = Node({"idk": 5, "nk": "Humankind", "ida": 8, "cijena": 13})

# knjige.append_sort(knjiga1)
# knjige.append_sort(knjiga2)
# knjige.append_sort(knjiga3)
# knjige.append_sort(knjiga4)
# knjige.append_sort(knjiga5)
# knjige.print_list()

# l1 = DoublyLinkedList()
# l1.append(Node(1))
# l1.append(Node(2))
# l1.append(Node(3))
# l1.append(Node(5))
# l1.append(Node(5))
# l1.append(Node(6))
# l1.append(Node(7))
# l1.append(Node(8))


# l1.print_list()
# l1.print_list_reversed()
