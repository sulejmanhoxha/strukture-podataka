from data_structures.graph.graph import Graph


def je_boja_valjana(cvor_idx, boja, graf_adj, boje_cvorova):
    for sused in graf_adj[cvor_idx]:
        if boje_cvorova[sused] == boja:
            return False
    return True


def boji_graf(indeks_cvora, K, graf_adj, boje_cvorova):
    # AKO indeks_čvora == BrojČvorova(Graf) ONDA
    if indeks_cvora == len(graf_adj):
        return True

    # ZA boju OD 1 DO K RADI
    for boja in range(1, K + 1):
        # AKO JeBojaValjana(indeks_čvora, boju, Graf, Boje_čvorova) ONDA
        if je_boja_valjana(indeks_cvora, boja, graf_adj, boje_cvorova):
            # Boje_čvorova[indeks_čvora] = boja
            boje_cvorova[indeks_cvora] = boja

            # AKO BojiGraf(indeks_čvora + 1, K, Graf, Boje_čvorova) ONDA
            if boji_graf(indeks_cvora + 1, K, graf_adj, boje_cvorova):
                return True

            # Boje_čvorova[indeks_čvora] = NEMA_BOJE
            boje_cvorova[indeks_cvora] = 0  # NEMA_BOJE = 0

    return False


def backtracking_bojenje(graph, K):
    graf_adj = graph.to_adjacency_list()
    boje_cvorova = [0] * graph.num_nodes  # 0 = NEMA_BOJE

    if boji_graf(0, K, graf_adj, boje_cvorova):
        return boje_cvorova
    else:
        return None


def pohlepno_boji_graf(graph):
    graf_adj = graph.to_adjacency_list()
    N = graph.num_nodes
    boje = [0] * N  # 0 = NEMA_BOJE

    # ZA i OD 0 DO N−1 RADI
    for i in range(N):
        K_max = N  # maksimalno N boja je potrebno

        # Disponibilne = niz veličine K_max+1, sve postavljeno na TAČNO
        disponibilne = [True] * (K_max + 1)
        disponibilne[0] = False  # boja 0 nije validna

        # ZA svaki susjed s U listi susjeda čvora i RADI
        for s in graf_adj[i]:
            # AKO Boje[s] != NEMA_BOJE ONDA
            if boje[s] != 0:
                # Disponibilne[Boje[s]] = NETAČNO
                disponibilne[boje[s]] = False

        # ZA c OD 1 DO K_max RADI
        for c in range(1, K_max + 1):
            # AKO Disponibilne[c] ONDA
            if disponibilne[c]:
                # Boje[i] = c
                boje[i] = c
                break

    return boje


# Kreiranje grafa
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 0)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 1)
graph.add_edge(2, 2)  # petlja
graph.add_edge(3, 2)

print("Matrica susedstva:")
for row in graph.adjacency_matrix:
    print(row)

print("\n=== BACKTRACKING ALGORITAM ===")
# Probaj sa različitim brojem boja
for K in range(1, 5):
    print(f"\nPokušavam sa {K} boja:")
    bt_result = backtracking_bojenje(graph, K)
    if bt_result:
        print(f"Uspešno! Boje čvorova: {bt_result}")
        break
    else:
        print("Nema rešenja")

print("\n=== POHLEPNI ALGORITAM ===")
greedy_result = pohlepno_boji_graf(graph)
print(f"Boje čvorova: {greedy_result}")
print(f"Ukupno korišćenih boja: {max(greedy_result)}")
