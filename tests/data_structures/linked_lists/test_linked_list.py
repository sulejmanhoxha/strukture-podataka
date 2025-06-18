from src.data_structures.linked_lists.linked_list import LinkedList, Node


def test_append():
    l1 = LinkedList()
    l1.append(Node(1))
    l1.append(Node(2))
    l1.append(Node(3))
    l1.append(Node(4))
    l1.append(Node(5))

    assert l1.length_iterative() == 5
    assert l1.length_recursive(l1.head) == 5


def test_prepend():
    l1 = LinkedList()
    l1.prepend(Node(1))
    l1.prepend(Node(2))
    l1.prepend(Node(3))
    l1.prepend(Node(4))
    l1.prepend(Node(5))

    assert l1.length_iterative() == 5
    assert l1.length_recursive(l1.head) == 5


def test_find_maximum_value():
    l1 = LinkedList()
    l1.append(Node(1))
    l1.append(Node(2))
    l1.append(Node(3))
    l1.append(Node(4))
    l1.append(Node(5))

    assert l1.find_maximum_value() == 5
