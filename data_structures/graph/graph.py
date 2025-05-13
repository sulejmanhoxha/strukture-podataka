class Graph:
    def __init__(self, num_nodes):
        self.adjacency_matrix = []
        for i in range(num_nodes):
            # kja ka me kriju nji list edhe secili element ka me qen 0
            self.adjacency_matrix.append([0 for i in range(num_nodes)])
        self.num_nodes = num_nodes

    def add_edge(self, start, end):
        self.adjacency_matrix[start][end] = 1

    def remove_edge(self, start, end):
        if self.adjacency_matrix[start][end] == 0:
            print(f"Grana izmedu cvorova {start} i {end} ne postoji.")
        else:
            self.adjacency_matrix[start][end] = 0

    def contains_edge(self, start, end):
        if self.adjacency_matrix[start][end] == 1:
            return True
        else:
            return False


graph = Graph(4)  # kreira graph sa 4 cvora, trenutno nema grana

graph.add_edge(0, 1)
graph.add_edge(0, 2)

graph.add_edge(1, 0)
graph.add_edge(1, 2)

graph.add_edge(2, 0)
graph.add_edge(2, 1)
graph.add_edge(2, 2)

graph.add_edge(3, 2)

print(graph.adjacency_matrix)
