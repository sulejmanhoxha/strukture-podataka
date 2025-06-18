# Kreirati dvostruko olančanu listu, gdje svaki čvor predstavlja
# film. Data dio svakog čvora sadrži 4 podatka i to naziv (string),
# zanr (string), godina (int), ocjena (float) filma.

# a. Izračunati ukupanu prosječnu ocjenu svih filmova za zadatu
# godinu (godina parametar funkcije).

# b. Štampati one filmove čija je čija je godina veća ili jednaka
# zadatoj godini (parametar funkcije min_godina)
# Input: 2000 - 1993 - 2011 - 2007; 2007 Output: 2011 - 2007

# c.  Štampati  koliko  filmova  zadati  žanr(zanr  se  zadaje  kao
# parametar funkcije)
# Input: drama - komedija - triler - drama; drama Output: 2

# d. Sve funkcije je potrebno pozvati i testirati za bar 5 filmova.


class MoivieNode:
    def __init__(self, name, genre, year, rating):
        self.movie = {"name": name, "genre": genre, "year": year, "rating": rating}


class LinkedListFilms:
    def __init__(self, head=None):
        self.head = head

    def print_values(self):
        current = self.head
        while current:
            print(current.movie)
            current = current.next

    def append(self, new_element):
        current = self.head
        if not current:
            self.head = new_element
            new_element.next = None
        else:
            while current.next:
                #                 print(current.value)
                current = current.next
            current.next = new_element
            new_element.next = None

    def avg_rate_per_year(self, year):
        current = self.head
        count = 0
        sum_rate = 0
        while current:
            if current.movie["year"] == year:
                count = count + 1
                sum_rate = sum_rate + current.movie["rating"]
            #                 print(current.movie)
            current = current.next
        if count != 0:
            return sum_rate / count
        else:
            return None

    def print_movies_greater_than(self, min_year):
        current = self.head
        while current:
            if current.movie["year"] >= min_year:
                print(current.movie)
            current = current.next

    def genre_count(self, genre):
        current = self.head
        count = 0
        while current:
            if current.movie["genre"] == genre:
                #                 print(current.movie)
                count = count + 1
            current = current.next
        return count


n1 = MoivieNode("The Batman", "drama", 2022, 8.1)
n2 = MoivieNode("Joker", "drama", 2019, 8.4)
n3 = MoivieNode("Dune", "action", 2021, 8.1)
n4 = MoivieNode("The Shawshank Redemption", "drama", 1994, 9.3)
n5 = MoivieNode("39. Don't Look Up", "comedy", 2021, 7.2)
n6 = MoivieNode("Once Upon a Time... In Hollywood ", "comedy", 2019, 7.6)

movies_list = LinkedListFilms()
movies_list.append(n1)
movies_list.append(n2)
movies_list.append(n3)
movies_list.append(n4)
movies_list.append(n5)
movies_list.append(n6)

movies_list.print_values()
print("**********")
# A)
print(movies_list.avg_rate_per_year(2021))
print("**********")
# B)
movies_list.print_movies_greater_than(2005)
print("**********")
# C)
print(movies_list.genre_count("drama"))
