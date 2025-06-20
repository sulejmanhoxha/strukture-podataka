from src.data_structures.linked_lists.doubly_linked_list import DoublyLinkedList, Node

class DoublyLinkedListPacijenta(DoublyLinkedList):

    def append_pacijent(self, pacijent):
        if self.head is None:
            self.append(pacijent)
            return
        if self.head.value['prioritet_prijema'] > pacijent.value['prioritet_prijema']:
            self.prepend(pacijent)
        else :
            self.append(pacijent)

    def brisi_pacijent(self, ime):
        if self.head is None:
            return

        curr = self.head

        if curr.value['ime_i_prezime'] == ime and curr.next is None:
            self.head = None
            return
        
        while curr and curr.next:
            if curr['ime_i_prezime'] == ime:
                curr.next.next.prev = curr
                curr.next = curr.next.next
        
            curr = curr.next

        return "Pacijent sa imenom ne postoji"


    def koliko_je_hospitalizovano(self, br_dana, doba):
        current = self.head

        godina_doba = 2025 - doba
        br = 0
        while current:
            broj_dana_hospitalizacije = current.value['broj_dana_hospitalizacije']
            godina = current.value['broj_dana_hospitalizacije']


            if broj_dana_hospitalizacije > br_dana and godina <godina_doba :
                br = br + 1

            current = current.next
        
        return br

    def najkraci_boravak(self):
        current = self.head

        min = current.value['broj_dana_hospitalizacije']
        pacijent = None

        while current:
            broj_dana_hospitalizacije = current.value['broj_dana_hospitalizacije'] 
            if min > broj_dana_hospitalizacije:
                min = broj_dana_hospitalizacije
                pacijent = Node(current.value)

            current = current.next
        
        print(f"Pacijent sa najkracim boravkom u bolnici je: {pacijent.value['ime_i_prezime']}, sa dijagnozom {pacijent.value['dijagnoza']}")

    def print_obrnuto(self):
        current = self.head
        while current.next:
            current = current.next
        string = "Reversed list: [ "
        while current:
            if current.prev is None:
                string = string + str(current.value) + " ]"
            else:
                string = string + str(current.value) + "   ⇄   "

            current = current.prev
        print(string)


l2 = DoublyLinkedListPacijenta()

l2.append_pacijent(Node({"ime_i_prezime": "mano1","godine":10, "dijagnoza": "rak1", "prioritet_prijema": 7, "broj_dana_hospitalizacije": 12}))
l2.append_pacijent(Node({"ime_i_prezime": "mano2","godine":11, "dijagnoza": "rak2", "prioritet_prijema": 5, "broj_dana_hospitalizacije": 2}))
l2.append_pacijent(Node({"ime_i_prezime": "mano3","godine":12, "dijagnoza": "rak3", "prioritet_prijema": 8, "broj_dana_hospitalizacije": 1}))
l2.append_pacijent(Node({"ime_i_prezime": "mano5","godine":13, "dijagnoza": "rak1", "prioritet_prijema": 8, "broj_dana_hospitalizacije": 3}))
l2.append_pacijent(Node({"ime_i_prezime": "mano6","godine":14, "dijagnoza": "rak2", "prioritet_prijema": 9, "broj_dana_hospitalizacije": 7}))

l2.print_list()
print()
print()

l2.najkraci_boravak()

print()
print()
l2.print_obrnuto()

