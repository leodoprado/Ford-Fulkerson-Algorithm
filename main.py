class Graph:
    def __init__(self, graph):
        self.graph = graph  # grafo residual
        self.num_nodes = len(graph)
        self.node_labels = ['S', 'A', 'B', 'C', 'D', 'T']

    def BFS(self, source, sink, parent): # Caminho aumentado
        visited = [False] * self.num_nodes
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            current_node = queue.pop(0)
            for neighbor_index, capacity in enumerate(self.graph[current_node]):
                if not visited[neighbor_index] and capacity > 0:
                    queue.append(neighbor_index)
                    visited[neighbor_index] = True
                    parent[neighbor_index] = current_node
                    if neighbor_index == sink:
                        return True
        return False

    def FordFulkerson(self, source, sink):
        parent = [-1] * self.num_nodes 
        max_flow = 0

        while self.BFS(source, sink, parent): 
            path_flow = float("Inf")
            current_node = sink
            while current_node != source:
                # Utiliza o minimo para suportar o fluxo do caminho
                path_flow = min(path_flow, self.graph[parent[current_node]][current_node])
                current_node = parent[current_node]

            max_flow += path_flow

            current_node = sink
            while current_node != source:
                previous_node = parent[current_node]
                self.graph[previous_node][current_node] -= path_flow
                self.graph[current_node][previous_node] += path_flow
                current_node = parent[current_node]

        return max_flow

    def print_graph(self):
        for from_node in range(self.num_nodes):
            for to_node in range(self.num_nodes):
                if self.graph[from_node][to_node] > 0:
                    print(f"{self.node_labels[from_node]} -> {self.node_labels[to_node]}: {self.graph[from_node][to_node]}")

graph = [[0, 6, 12, 0, 0, 0],
         [0, 0, 0, 8, 0, 0],
         [0, 0, 0, 3, 5, 0],
         [0, 0, 0, 0, 0, 14],
         [0, 0, 0, 0, 0, 7],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

print("Capacidade residual do grafo:")
g.print_graph()
print("\nO fluxo máximo possível é: %d" % g.FordFulkerson(source, sink))