from src.data_structures.linked_lists.doubly_linked_list import DoublyLinkedList, Node

l1 = DoublyLinkedList()
l1.append(Node(5))
l1.append(Node(4))
l1.append(Node(3))
l1.append(Node(7))
l1.append(Node(5))
l1.append(Node(1))

print("Adding values at the end of the list with append function.")
l1.print_list()
