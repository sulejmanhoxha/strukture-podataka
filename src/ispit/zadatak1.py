def koliko_puta_se_pojavljuje(n, broj):
    if n == 0:
        return 0


    return (1 if n % 10 == broj else 0) + koliko_puta_se_pojavljuje(n // 10, broj)

print("Za broj 413411, za 1 pojavljuje: " + str(koliko_puta_se_pojavljuje(413411, 1)))
print("Za broj 44356, za 4 pojavljuje: " + str(koliko_puta_se_pojavljuje(44356, 4)))
print("Za broj 89789, za 2 pojavljuje: " + str(koliko_puta_se_pojavljuje(89789, 2)))


# b)
def sve_podskupove(n:[], S:int, liste = [])-> []:
    if len(n) == 0:
        return 

    if sum(n) == S:
        liste.append([n])

    return sve_podskupove(n[:-1], S, liste)

combinacije = sve_podskupove([1,2,3,4], 5)
print("Za listu [1,2,3,4] za S = 5, dobijemo liste: ")
print(combinacije)
