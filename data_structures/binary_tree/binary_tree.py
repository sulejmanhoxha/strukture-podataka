# # some_file.py
# import sys
# sys.path.append('/home/manoh/Visual Studio Code Projects/Strukture_Podataka_I_Algoritmi/strukture_podataka/stack_queue')
# # sys.path.insert(
# #     1, '/home/manoh/Visual Studio Code Projects/Strukture_Podataka_I_Algoritmi/strukture_podataka/stack_queue')

# import queue
# # from Strukture_Podataka_I_Algoritmi.strukture_podataka.stack_queue.queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.value:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.value:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("Data is already in the tree")

    def find(self, data):
        is_found = False
        if self.root:
            is_found = self._find(data, self.root)
            return bool(is_found)
        else:
            return None

    def _find(self, data, current_node):
        if data == current_node.value:
            return True
        if data > current_node.value and current_node.right:
            return self._find(data, current_node.right)
        elif data < current_node.value and current_node.left:
            return self._find(data, current_node.left)

    # prej bt_zadaci, mbahet se funkcionen vetem ke detyra me dictioneries

    def _insert1(self, value, current_node):
        if value["zarada"] > current_node.value["zarada"]:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        elif value["zarada"] < current_node.value["zarada"]:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        else:
            print("Vrijednost koju pokusavate da dodate vec postoji.")

    # prej bt_zadaci
    def najveca_zarada(self, current):
        while current.right:
            current = current.right
        return current.value['ime']

    # nedelja 6
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root, "")
        else:
            return "Invalid traversal type!"

    def preorder_print(self, start, traversal):
        # parent -> left -> right  [↙ ↙ ↙ ↙]
        if start:
            traversal = traversal + (str(start.value) + " -> ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        # left -> parent -> right:    [↗ ↗ ↗ ↗]
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = traversal + (str(start.value) + " -> ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        # left , right, parent : [  ↘ ↖  ]
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal = traversal + (str(start.value) + " -> ")
        return traversal

    def levelorder_print(self, start, traversal):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "->"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    def prebroji_cvororva(self, start):
        if start is None:
            return 0
        return 1 + self.prebroji_cvororva(start.left) + self.prebroji_cvororva(start.right)

    def prebroji_cvororva_koji_su_veci_od(self, start, broj):
        if start is None:
            return 0

        if start.value > broj:
            return 1 + self.prebroji_cvororva_koji_su_veci_od(start.left, broj) + self.prebroji_cvororva_koji_su_veci_od(start.right, broj)
        else:
            return self.prebroji_cvororva_koji_su_veci_od(start.left, broj) + self.prebroji_cvororva_koji_su_veci_od(start.right, broj)

    def prebroji_cvororva_koji_su_veci_od_i_manji_od(self, start, broj1, broj2):
        if start is None:
            return 0

        if start.value > broj1 and start.value < broj2:
            return 1 + self.prebroji_cvororva_koji_su_veci_od_i_manji_od(start.left, broj1, broj2) + self.prebroji_cvororva_koji_su_veci_od_i_manji_od(start.right, broj1, broj2)
        else:
            return self.prebroji_cvororva_koji_su_veci_od_i_manji_od(start.left, broj1, broj2) + self.prebroji_cvororva_koji_su_veci_od_i_manji_od(start.right, broj1, broj2)

    # kja funkcija nelt profi
    def range_count(self, current, low, high):
        if current == None:
            return 0
        if current.value < high and current.value > low:
            return (1 + self.range_count(current.left, low, high) + self.range_count(current.left, low, high))
        elif current.value < low:
            return self.range_count(current.right, low, high)
        else:
            return self.range_count(current.left, low, high)

    def _prebroji(self, current, traversal, low=3, high=9):
        def prebroji(self, current, traversal, low=3, high=9):
            # ktu lypet mi kriju nji global ke klasa ma nelt mbahet ??
            global sum

            if current:
                traversal = self.prebroji(current.left, traversal, low, high)
                if current.value > low and current.value < high:
                    suma = suma + 1
                traversal = self.prebroji(current.right, traversal, low, high)
            return suma

    # un
    def preorder_print_2(self, start):
        # parent -> left -> right  [↙ ↙ ↙ ↙]
        if start is None:
            return ""

        # traversal = traversal + (str(start.value) + " -> ")
        return str(start.value) + " -> " + str(self.preorder_print_2(start.left)) + str(self.preorder_print_2(start.right))

    # un prov
    def sum_of_values(self, start):
        if start is None:
            return 0
        return start.value + self.sum_of_values(start.left) + self.sum_of_values(start.right)

    def min_val_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def min(self):
        if self.root:
            return self.min_val_node(self.root)

    def delete_node(self, current, data):
        if current is None:
            return current
        if data < current.value:
            current.left = self.delete_node(current.left, data)
        elif data > current.value:
            current.right = self.delete_node(current.right, data)
        else:
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp

            temp = self.min_val_node(current.right)
            current.value = temp.value
            current.right = self.delete_node(current.right, temp.value)
        return current

    def _size(self, current):
        if current is None:
            return 0
        else:
            return self._size(current.left) + self._size(current.right) + 1

    def size(self):
        return self._size(self.root)

    def get_num_of_leaf(self):
        return self._get_num_of_leaf(self.root)

    def _get_num_of_leaf(self, current):
        if not current:
            return 0
        else:
            if not current.left and not current.right:
                return 1
            else:
                return self._get_num_of_leaf(current.left) + self._get_num_of_leaf(current.right)

    def num_not_leaf():
        pass


# DFS
# inorder : 1.left, 2.parent, right: shken ke ma i majti (left.left.left .....) masanej [↗ ↗ ↗ ↗]
# preorder: 1.root ,left, right : kja qysh me root fillen me [↙ ↙ ↙ ↙] dmth. root edhe [↙ ↙ ↙ ↙]
# postorder: 1. left , right, parent :   shken ke leaf ma i majti qi isht(left.left.left ......)   masanej [  ↘ ↖  ]
# (\  \  \  \) . shken si \ vetem se fillen prej nelt posht, e njitet ke \ tjeter par prej posht nelt
# BFS - LevelOrder shken rresht per rresht, prej majtas djathtas dmth komplet horizontal
bin_tree = BinaryTree(6)

bin_tree.insert(3)
bin_tree.insert(7)
bin_tree.insert(2)
bin_tree.insert(5)
bin_tree.insert(9)

print(bin_tree.print_tree("preorder"))
print(bin_tree.print_tree("postorder"))
print(bin_tree.print_tree("inorder"))
# print(bin_tree.print_tree("levelorder"))
print(bin_tree.find(10))
print(bin_tree.min().value)

bin_tree.delete_node(bin_tree.root, 7)
print(bin_tree.print_tree("preorder"))
print(bin_tree.size())
print(bin_tree.get_num_of_leaf())


# print(bin_tree.preorder_print_2(bin_tree.root))

# print(bin_tree.prebroji_cvororva(bin_tree.root))
# print(bin_tree.sum_of_values(bin_tree.root))


# print(bin_tree.prebroji_cvororva_koji_su_veci_od(bin_tree.root, 4))
# print(bin_tree.prebroji_cvororva_koji_su_veci_od_i_manji_od(bin_tree.root, 4, 8))
# print(bin_tree.range_count(bin_tree.root, 4, 8))
