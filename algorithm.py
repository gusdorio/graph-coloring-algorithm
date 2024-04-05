# Function to get the matrix of adjacency for each node
import networkx as nx


class Clicks:
    adjacency = {}
    clicks = {}

    def __init__(self, graph: 'nx.Graph'):
        self.graph = graph  # is expected a nx object...
        self.adjacency_add(self.graph)

    def adjacency_add(self, graph):
        # Add the adjacency of each node
        for n in graph.nodes():
            neighbors = list(graph.neighbors(n))
            self.adjacency[n] = neighbors

    # Function to define clicks
    # def clicks(dic):
    #   count = 0
    #   for i in dic[count]:
    #     for n in range(dic[count]):


# x = Clicks(nx.gnp_random_graph(10, .3))
# print(x.adjacency)
