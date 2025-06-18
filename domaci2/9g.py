# Tramvaj broj 8 koji kruži "u krugu osmice" ima N stajališta (N se zadaje
# na ulazu). Tramvaj sa početnog stajališta kreće bez putnika (prazan).
# Za svako stajalište se unose naziv (jedna riječ), ulaz (broj putnika koji
# ulaze – prirodan broj) i izlaz (broj putnika koji izlaze – prirodan broj).
# Napraviti kružnu povezanu listu, koja predstavlja trasu tramvaja broj 8,
# pri čemu putnici uvijek mogu da uđu u tramvaj, ali ukoliko se navede da
# na datom stajalištu izlazi više putnika nego što trenutno postoji u
# tramvaju, tada izlaze svi putnici. Svaki element liste odgovara jednom
# stajalištu i sadrži naziv stajališta i broj putnika u tramvaju u trenutku
# kada tramvaj kreće sa tog stajališta. Ispisati trasu tramvaja broj 8 sa
# podacima naziv stajališta i broj putnika. Tramvaj nastavlja da kruži, i
# za svako trenutno stajalište se ponovo unose samo brojevi putnika
# (bez naziva stajališta) koji ulaze i koji izlaze iz tramvaja. Tramvaj kruži
# bez prestanka sve dok ne ostane samo jedno stajalište na kom
# završava svoju smenu i svi putnici koji se nalaze u tom trenutku u
# tramvaju izlaze iz njega. Nakon svakog kruga (kad god tramvaj stigne
# do polaznog stajališta) ispisati trasu tramvaja. Smatra se da će tramvaj
# u nekom trenutku sigurno završiti smjenu.

from data_structures.linked_lists.circular_list import CircularLinkedList, Node


class TramStop:
    def __init__(self, name, passengers=0):
        self.name = name
        self.passengers = passengers

    def __str__(self):
        return f"{self.name}: {self.passengers} putnika"


class TramCircularList(CircularLinkedList):
    def append(self, new_node):
        current = self.head

        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_route(self):
        if not self.head:
            print("Nema stajališta.")
            return

        print("Trenutna trasa tramvaja:")
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break

    def remove_stop(self, stop_node):
        if not self.head:
            return

        if self.head.next == self.head:
            self.head = None
            return

        if stop_node == self.head:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            while current.next != stop_node:
                current = current.next
            current.next = stop_node.next


def main():
    n = int(input("Unesite broj stajališta: "))
    if n <= 0:
        print("Broj stajališta mora biti pozitivan broj.")
        return

    tram_route = TramCircularList()
    passengers = 0

    for i in range(n):
        name = input(f"Unesite naziv {i+1}. stajališta: ")
        entering = int(input(f"Broj putnika koji ulaze na {name}: "))
        exiting = int(input(f"Broj putnika koji izlaze na {name}: "))

        if exiting > passengers:
            passengers = 0
        else:
            passengers -= exiting
        passengers += entering

        stop = TramStop(name, passengers)
        tram_route.append(Node(stop))

    tram_route.print_route()

    completed_rounds = 0
    current_stop = tram_route.head
    while tram_route.head is not None:
        if current_stop.next == current_stop:
            print(f"\nTramvaj završava smenu na stajalištu {current_stop.data.name}.")
            print(f"Svi putnici ({current_stop.data.passengers}) izlaze.")
            break

        if current_stop == tram_route.head and completed_rounds > 0:
            print("\nTramvaj je završio krug!")
            tram_route.print_route()

        print(f"\nTramvaj je na stajalištu {current_stop.data.name}")
        entering = int(input("Broj putnika koji ulaze: "))
        exiting = int(input("Broj putnika koji izlaze: "))

        passengers = current_stop.data.passengers
        if exiting > passengers:
            passengers = 0
        else:
            passengers -= exiting
        passengers += entering

        next_stop = current_stop.next
        next_stop.data.passengers = passengers

        if entering == -1 and exiting == -1:
            tram_route.remove_stop(current_stop)
            if tram_route.head is None:
                break

        if next_stop == tram_route.head:
            completed_rounds += 1
        current_stop = next_stop


main()
