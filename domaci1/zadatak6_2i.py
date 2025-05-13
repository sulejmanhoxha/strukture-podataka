# Napisati funkciju koja uklanja najmanji element iz liste

import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.linked_lists.linked_list import LinkedList, Node

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
