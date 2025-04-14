# Pisao sam funkcije ovdje da ne morate da ih nadjete

import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from linked_lists.doubly_linked_list import DoublyLinkedList, Node


def prosjecna_ocjena(filmovi: DoublyLinkedList, godina: int) -> float:
    """
    Funkcija koja izračuna ukupanu prosječnu ocjenu svih filmova za zadatu godinu

    Args:
        film (DoublyLinkedList): Dvostruko olančanu listu, gdje svaki čvor predstavlja film.
        godina (int): Zadata godina

    Returns:
        float: Ukupna prosječna ocjena
    """
    prosjecna_ocjena = 0
    count = 0
    current = filmovi.head
    while current:
        if current.value["godina"] >= godina:
            print(current.value)
            prosjecna_ocjena = prosjecna_ocjena + current.value["ocjena"]
            count = count + 1
        current = current.next

    return prosjecna_ocjena / count


def godina_veca_ili_jednaka(filmovi: DoublyLinkedList, min_godina: int):
    """
    Funkcija koja štampa filmove čija je čija je godina veća ili jednaka zadatoj godini

    Args:
        filmovi (DoublyLinkedList): Dvostruko olančanu listu, gdje svaki čvor predstavlja film.
        min_godina (int): Zadata godina
    """

    current = filmovi.head
    while current:
        if current.value["godina"] >= min_godina:
            print(current.value)

        current = current.next


def koliko_ima_zanrova(filmovi: DoublyLinkedList, zanr: str) -> int:
    """
    Funkcija koja štampa koliko filmova ima zadat žanr

    Args:
        filmovi (DoublyLinkedList): Dvostruko olančanu listu, gdje svaki čvor predstavlja film.
        zanr (str): Zadata žanr

    Returns:
        int: Koliko filmova ima zadat žanr
    """

    current = filmovi.head
    count = 0

    while current:
        if current.value["zanr"] == zanr:
            count = count + 1
        current = current.next

    return count


filmovi = DoublyLinkedList()

film1 = Node({"naziv": "The Shawshank Redemption", "zanr": "Drama", "godina": 1994, "ocjena": 9.2})
film2 = Node({"naziv": "The Godfather", "zanr": "Crime", "godina": 1972, "ocjena": 9.2})
film3 = Node({"naziv": "The Dark Knight", "zanr": "Action", "godina": 2008, "ocjena": 9.0})
film4 = Node({"naziv": "12 Angry Men", "zanr": "Drama", "godina": 1957, "ocjena": 9.0})
film5 = Node({"naziv": "Schindler's List", "zanr": "Biography", "godina": 1993, "ocjena": 8.9})
film6 = Node({"naziv": "The Grand Budapest Hotel", "zanr": "Comedy", "godina": 2014, "ocjena": 8.1})
film7 = Node({"naziv": "The Princess Bride", "zanr": "Fantasy", "godina": 1987, "ocjena": 8.1})
film8 = Node({"naziv": "The Big Lebowski", "zanr": "Comedy", "godina": 1998, "ocjena": 8.1})
film9 = Node({"naziv": "Eternal Sunshine of the Spotless Mind", "zanr": "Romance", "godina": 2004, "ocjena": 8.3})
film10 = Node({"naziv": "The Prestige", "zanr": "Mystery", "godina": 2006, "ocjena": 8.1})

filmovi.append(film1)
filmovi.append(film2)
filmovi.append(film3)
filmovi.append(film4)
filmovi.append(film5)
filmovi.append(film6)
filmovi.append(film7)
filmovi.append(film8)
filmovi.append(film9)
filmovi.append(film10)

print("Prosječna ocjena za godinu 2008:")
print(prosjecna_ocjena(filmovi, 2008))

print("Filmovi čija je godina veća ili jednaka 2001:")
print(godina_veca_ili_jednaka(filmovi, 2001))

print("Koliko filmova ima zadat žanr drama:")
print(koliko_ima_zanrova(filmovi, "Drama"))
