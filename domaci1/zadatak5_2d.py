import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from linked_lists.linked_list import LinkedList, Node


def remove_every_third_element(linked_list):
    """
    Funkcija koja iz jednostruko olančane liste uklanja svaki treći element

    Args:
        linked_list (LinkedList): Jednostruko olančane liste

    Returns:
        LinkedList: Uklonjena jednostruko olančana lista
    """
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


l1 = LinkedList()
l1.append(Node(1))
l1.append(Node(2))
l1.append(Node(3))
l1.append(Node(4))
l1.append(Node(5))
l1.append(Node(6))
l1.append(Node(7))
l1.append(Node(8))
l1.append(Node(9))
l1.append(Node(10))

print("Original list:")
l1.print_list()

remove_every_third_element(l1)

print("After removing every third element:")
l1.print_list()
