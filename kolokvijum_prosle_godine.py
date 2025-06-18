from data_structures.linked_lists.doubly_linked_list import DoublyLinkedList, Node
from data_structures.linked_lists.linked_list import LinkedList, Node


def nadi_veliko_slovo_poslednju(string: str):
    if len(string) == 0:
        return "Recenica nema veliko slovo"

    slovo = string[-1]

    if slovo.isupper():
        return slovo

    else:
        return nadi_veliko_slovo_poslednju(string[:-1])


# print(nadi_veliko_slovo_poslednju("Neka Ulazna Recenica"))

l1 = LinkedList()
l1.append(Node(2))
l1.append(Node(5))
l1.append(Node(8))
l1.append(Node(2))
l1.append(Node(13))
l1.append(Node(3))


def neparni_kvadrirani(l1: LinkedList):
    l2 = LinkedList()

    current = l1.head

    while current:
        if current.value % 2 == 0:
            l2.append(Node(current.value**2))

        current = current.next

    l2.print_list()


# l1.print_list()
# neparni_kvadrirani(l1)


def ukloni_svaki_drugi(l1: LinkedList):
    current = l1.head

    while current.next:
        if current.next.next is None:
            current.next = None
            break
        current.next = current.next.next
        current = current.next
    l1.print_list()


# ukloni_svaki_drugi(l1)


# 3. Kreirati dvostruko olančanu listu sa bar 5 elemenata, gdje svaki čvor sadrži 4
# podatka i to ime (string), prezime (string), godina (int), prosjek (float) studenta.
# a. Izračunati ukupan prosjek studenata za zadatu godinu (godina parametar
# funkcije). ​Pomoć​: samo sabrati sve vrijednosti prosjeka za zadatu godinu i
# to vrijednosti podijeliti sa brojem studenata na toj godini. Npr. ako imate tri
# studenta sa prve godine, a njihovi prosjeci su redom 7, 8 i 9, onda se
# razultat dobija na sledeći način: (7 + 8 + 9) / 3 = 8, pa je output 8
# b. Štampati sve elemente liste koji se pojavljuju prije zadatog indeksa.
# Pomoć​: imajte u vidu da je ovo dvostruko olančana lista, pa vrlo lako
# možete da štampate prethodne elemente koristeći prev pokazivač
# Input​: 2 - 4 - 6 - 8 - 10; 3                       ​Output​: 4 - 2


l2 = DoublyLinkedList()
l2.append(Node({"ime": "mano1", "prezime": "hoxha1", "godina": 2022, "prosjek": 7.0}))
l2.append(Node({"ime": "mano2", "prezime": "hoxha2", "godina": 2021, "prosjek": 5.6}))
l2.append(Node({"ime": "mano3", "prezime": "hoxha3", "godina": 2022, "prosjek": 8.0}))
l2.append(Node({"ime": "mano5", "prezime": "hoxha4", "godina": 2020, "prosjek": 8.6}))
l2.append(Node({"ime": "mano6", "prezime": "hoxha5", "godina": 2022, "prosjek": 9.0}))

l2.print_list()


def izracunaj_ukupan_prosjek_studenata_za_godinu(lista: DoublyLinkedList, godina):
    current = lista.head
    suma = 0
    counter = 0
    while current:
        if current.value["godina"] == godina:
            suma = suma + current.value["prosjek"]
            counter = counter + 1
        current = current.next

    return suma / counter


# print(izracunaj_ukupan_prosjek_studenata_za_godinu(l2, 2022))


def print_till_index(l1: DoublyLinkedList, index):
    current = l1.head
    counter = 1

    while current:
        if counter == index:
            break
        else:
            print(current.value)
            counter = counter + 1

        current = current.next


print_till_index(l1, 3)
