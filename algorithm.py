# Function to get the matrix of adjacency for each node
import networkx as nx


class Clicks:
    adjacency = {}
    clicks = []

    def __init__(self, graph: 'nx.Graph'):
        self.graph = graph  # is expected a nx object...
        self.adjacency_add(self.graph)
        self.clicks_search(self.graph)

    def adjacency_add(self, graph):
        # Add the adjacency of each node
        for n in graph.nodes():
            neighbors = list(graph.neighbors(n))
            self.adjacency[n] = neighbors

    def clicks_search(self, adjacency):
        # Function to define clicks
        node = 0
        while node < 10:  # STEP 1 -> DEFINING PAIRS
            click = []
            for item in adjacency[node]:
                if [node, item] not in self.clicks:
                    if [item, node] not in self.clicks:
                        self.clicks.append([node, item])
            node += 1
    # STEP 2 -> DEFINING SETS (?)


x = Clicks(nx.gnp_random_graph(10, .3))
print(x.clicks)
