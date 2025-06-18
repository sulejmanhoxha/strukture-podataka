# Kreirati  jednostruko  olancanu  listu  gdje  svaki  čvor predstavlja
# studenta. Data dio svakog čvora sadrži 2 podatka: ime i prosjek
# studenta.  Napisati  funkciju koja računa prosječni prosjek svih
# studenata u listi, kao i posebnu funkciju koja vraća listu studenata
# koji imaju veći prosjek od prosječnog.


class UceniciNode:
    def __init__(self, ime, prosj):
        self.ucenici = {"ime": ime, "prosj": prosj}


class LinkedListUcenici:
    def __init__(self, head=None):
        self.head = head

    def print(self):
        current = self.head
        while current:
            print(current.ucenici)
            current = current.next

    def append(self, new_element):
        current = self.head
        if not current:
            self.head = new_element
            new_element.next = None
        else:
            while current.next:

                current = current.next
            current.next = new_element
            new_element.next = None

    def prosjek(self):
        current = self.head
        count = 0
        sum_rate = 0
        while current:
            count = count + 1
            sum_rate = sum_rate + current.ucenici["prosj"]

            current = current.next
        if count != 0:
            return sum_rate / count
        else:
            return None

    def prosjek_veci(self, prosjek):
        current = self.head
        while current:
            if current.ucenici["prosj"] > prosjek:
                print(current.ucenici)
            current = current.next


n1 = UceniciNode("Tamara Pavlovic", 4.2)
n2 = UceniciNode("Dejan Babic", 4.9)
n3 = UceniciNode("Ivan Jovovic", 4.7)
n4 = UceniciNode("Sanel Nisic", 3.2)
n5 = UceniciNode("Benjamin Dobardzic", 4.1)

ucenici_list = LinkedListUcenici()
ucenici_list.append(n1)
ucenici_list.append(n2)
ucenici_list.append(n3)
ucenici_list.append(n4)
ucenici_list.append(n5)

ucenici_list.print()
print("*****************")
print(ucenici_list.prosjek())
print("*****************")
ucenici_list.prosjek_veci(ucenici_list.prosjek())
