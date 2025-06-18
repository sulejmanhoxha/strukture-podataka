# Napišite funkciju parnepar(S1, S2) koja prima dva steka cijelih brojeva;
# po ulasku u funkciju pretpostavite da je S2 prazan. Funkcija treba da
# prerasporedi elemente steka S1 tako da se po izlasku iz nje u S1
# nalaze svi parni, a u S2 svi neparni elementi, u proizvoljnom poretku.
# Na primjer, ako su elementi u S1 bili (3, 1, 4, 1, 2, 6) onda nakon
# poziva funkcije treba biti S1=(4, 2, 6) i S2=(3, 1, 1)

from src.data_structures.stack_queue.stack import Stack

s1 = Stack()
s1.push(3)
s1.push(1)
s1.push(4)
s1.push(1)
s1.push(2)
s1.push(6)

print("Originalni stek:")
s1.print_stack()

s1, s2 = s1.parnepar(Stack())

s1.reverse()
s2.reverse()

print("S1:")
s1.print_stack()

print("S2:")
s2.print_stack()
