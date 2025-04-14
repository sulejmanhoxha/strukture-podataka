# Napisati funkciju koja uklanja najmanji element iz liste

import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from linked_lists.doubly_linked_list import DoublyLinkedList, Node

l1 = DoublyLinkedList()
l1.append(Node(5))
l1.append(Node(4))
l1.append(Node(3))
l1.append(Node(7))
l1.append(Node(5))
l1.append(Node(1))

print("Adding values at the end of the list with append function.")
l1.print_list()
