# Za izradu ovog zadatka iskoristiti već ranije implementirane funkcije:
# a. Kreirati binarno stablo sa bar 5 elemenata gdje je vrijednost
# svakog čvora broj. Štampati stablo kao inorder.
# b. Napisati metod max_node(self) koji vraća čvor sa najvećom
# vrijednošću u kreiranom binarnom stablu.
# c. Napisati metode number_of_not_leaves(self) koji vraća broj
# čvorova binarnog stabla koji nisu list (eng. leaf). (pomoć:
# broj_čvorova_drveta - broj_leaf_čvorova)

from data_structures.binary_tree.binary_tree import BinaryTree, Node


class BinaryTree2(BinaryTree):
    def max_recursive(self, current):
        if current and current.right:
            return self.max_recursive(current.right)
        else:
            return current.value

    def max_iterative(self, node):
        current = node
        while current.right:
            current = current.right
        return current

    def max(self, type="recursive"):
        if type == "recursive":
            return self.max_recursive(self.root)
        elif type == "iterative":
            return self.max_iterative(self.root)
        else:
            return "Invalid type!"

    def get_num_of_not_leaf(self):
        return self._get_num_of_not_leaf(self.root)

    def _get_num_of_not_leaf(self, current):
        if not current:
            return 0
        else:
            if current.left or current.right:
                return 1 + self._get_num_of_not_leaf(current.left) + self._get_num_of_not_leaf(current.right)
            else:
                return 0

    def number_of_not_leaves(self):
        if self.root:
            return self.number_of_not_leaves(self.root.left) + self.number_of_not_leaves(self.root.right) + 1
        else:
            return 0


btree = BinaryTree2(5)
btree.insert(3)
btree.insert(7)
btree.insert(2)
btree.insert(4)

#       5
#      / \
#     3   7
#    / \
#   2   4

print("Inorder traversal:")
print(btree.print_tree("inorder"))

print("Maximum node value:")
print(btree.max())

print("Number of not leaves:")
print(btree.get_num_of_not_leaf())  # brojimi i root, ako necemo root samo smanjimo sa -1
