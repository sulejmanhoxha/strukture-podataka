class Graph:
    def __init__(self, num_nodes):
        self.adjacency_matrix = []
        for i in range(num_nodes):
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
        return self.adjacency_matrix[start][end] == 1

    def to_adjacency_list(self):
        adj_list = {i: [] for i in range(self.num_nodes)}
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if self.adjacency_matrix[i][j] == 1:
                    adj_list[i].append(j)
        return adj_list
