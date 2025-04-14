# Pisao sam funkcije ovdje da ne morate da ih nadjete

import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from linked_lists.doubly_linked_list import DoublyLinkedList, Node


def ukupan_prosjek(studenti: DoublyLinkedList, godina: int) -> float:
    """
    Funkcija koja izračuna ukupan prosjek studenata za zadatu godinu.

    Args:
        studenti (DoublyLinkedList): Dvostruko olančanu listu, gdje svaki čvor predstavlja student.
        godina (int): Zadata godina

    Returns:
        float: Ukupan prosjek studenata za zadatu godinu
    """
    prosjek = 0
    count = 0
    current = studenti.head
    while current:
        if current.value["godina"] >= godina:
            prosjek = prosjek + current.value["prosjek"]
            count = count + 1
        current = current.next
    return prosjek / count


strudenti = DoublyLinkedList()

student1 = Node({"ime": "Ivan", "prezime": "Petrovic", "godina": 2000, "prosjek": 8.5})
student2 = Node({"ime": "Ana", "prezime": "Jovanovic", "godina": 2001, "prosjek": 9.0})
student3 = Node({"ime": "Marko", "prezime": "Milosevic", "godina": 2002, "prosjek": 8.0})
student4 = Node({"ime": "Jelena", "prezime": "Nikolic", "godina": 2003, "prosjek": 9.5})
student5 = Node({"ime": "Nemanja", "prezime": "Stojanovic", "godina": 2004, "prosjek": 8.8})
student6 = Node({"ime": "Sofija", "prezime": "Ristic", "godina": 2005, "prosjek": 9.2})
student7 = Node({"ime": "Luka", "prezime": "Djordjevic", "godina": 2006, "prosjek": 8.2})
student8 = Node({"ime": "Milica", "prezime": "Vasic", "godina": 2007, "prosjek": 9.8})
student9 = Node({"ime": "Stefan", "prezime": "Jankovic", "godina": 2008, "prosjek": 8.6})
student10 = Node({"ime": "Tamara", "prezime": "Pavlovic", "godina": 2009, "prosjek": 9.1})

strudenti.append(student1)
strudenti.append(student2)
strudenti.append(student3)
strudenti.append(student4)
strudenti.append(student5)
strudenti.append(student6)
strudenti.append(student7)
strudenti.append(student8)
strudenti.append(student9)
strudenti.append(student10)


print("Prosjek studenata za godinu vecu od 2008:")
print(ukupan_prosjek(strudenti, 2008))
