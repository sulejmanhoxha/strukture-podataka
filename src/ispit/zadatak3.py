from src.data_structures.binary_tree.binary_tree import BinaryTree, Node

class BinaryTreeKlubova(BinaryTree):

    def find_konferenciji(self, konferencija):
        if self is None or self.root is None:
            return None

        if data == self.root.value['konferencija']:
            print(data)
            
            if self.root.left:
                return self.root.left.find_konferenciji(konferencija)
            
            # if data > current_node.value and current_node.right:
            #     return self._find(data, current_node.right)
            # elif data < current_node.value and current_node.left:
            #     return self._find(data, current_node.left)
            # return bool(is_found)

    def _find(self, data, current_node):
        if data == current_node.value:
            print()
            return True
        if data > current_node.value and current_node.right:
            return self._find(data, current_node.right)
        elif data < current_node.value and current_node.left:
            return self._find(data, current_node.left)

    def najvise_pobjeda(self):
        while self.right:
            self = self.right
        return self.value


btree = BinaryTreeKlubova(Node({"naziv": "klub1","grad":"grad1", "broj_pobjeda": 1, "budzet": 7, "trener": "trener1", "konferencija": "istok","prosjecna_posjeta_publike": 31 }))

btree.append(Node({"naziv": "klub2","grad":"grad2", "broj_pobjeda": 5, "budzet": 5, "trener": "trener2", "konferencija": "zapad","prosjecna_posjeta_publike": 543}))
btree.append(Node({"naziv": "klub3","grad":"grad3", "broj_pobjeda": 3, "budzet": 8, "trener": "trener3", "konferencija": "istok","prosjecna_posjeta_publike": 65}))
btree.append(Node({"naziv": "klub4","grad":"grad4", "broj_pobjeda": 2, "budzet": 8, "trener": "trener4", "konferencija": "istok","prosjecna_posjeta_publike": 87}))
btree.append(Node({"naziv": "klub5","grad":"grad5", "broj_pobjeda": 8, "budzet": 9, "trener": "trener5", "konferencija": "zapad","prosjecna_posjeta_publike": 3244}))

btree.print_list()
print()
print()

print(btree.najveca_zarada())

