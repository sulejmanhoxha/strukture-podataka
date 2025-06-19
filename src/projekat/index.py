from src.data_structures.graph.graph import Graph


def je_boja_valjana(cvor_idx, boja, graf_adj, boje_cvorova):
    for sused in graf_adj[cvor_idx]:
        if boje_cvorova[sused] == boja:
            return False
    return True


def boji_graf(indeks_cvora, K, graf_adj, boje_cvorova):

    if indeks_cvora == len(graf_adj):
        return True

    for boja in range(1, K + 1):

        if je_boja_valjana(indeks_cvora, boja, graf_adj, boje_cvorova):

            boje_cvorova[indeks_cvora] = boja

            if boji_graf(indeks_cvora + 1, K, graf_adj, boje_cvorova):
                return True

            boje_cvorova[indeks_cvora] = 0

    return False


def backtracking_bojenje(graph, K):
    graf_adj = graph.to_adjacency_list()
    boje_cvorova = [0] * graph.num_nodes

    if boji_graf(0, K, graf_adj, boje_cvorova):
        return boje_cvorova
    else:
        return None


def pohlepno_boji_graf(graph):
    graf_adj = graph.to_adjacency_list()
    N = graph.num_nodes
    boje = [0] * N

    for i in range(N):
        K_max = N

        disponibilne = [True] * (K_max + 1)
        disponibilne[0] = False

        for s in graf_adj[i]:

            if boje[s] != 0:

                disponibilne[boje[s]] = False

        for c in range(1, K_max + 1):

            if disponibilne[c]:

                boje[i] = c
                break

    return boje


graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 0)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 1)
graph.add_edge(2, 2)
graph.add_edge(3, 2)

print("Matrica susedstva:")
for row in graph.adjacency_matrix:
    print(row)

print("\n=== BACKTRACKING ALGORITAM ===")
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
