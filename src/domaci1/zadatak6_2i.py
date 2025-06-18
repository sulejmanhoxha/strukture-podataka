from src.data_structures.linked_lists.linked_list import LinkedList, Node

l1 = LinkedList()
l1.append(Node(5))
l1.append(Node(4))
l1.append(Node(3))
l1.append(Node(7))
l1.append(Node(5))
l1.append(Node(1))

print("Original list:")
l1.print_list()

l1.delete_node_with_min_value()

print("After removing the minimum value:")
l1.print_list()
