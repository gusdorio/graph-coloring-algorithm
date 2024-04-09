# Function to get the matrix of adjacency for each node
import networkx as nx


class Clicks:
    adjacency = {}
    clicks = []

    def __init__(self, graph: 'nx.Graph'):
        self.graph = graph  # is expected a nx object...
        self.adjacency_add(self.graph)
        self.size_2(self.graph)
        self.size_n(self.graph)

    def adjacency_add(self, graph):
        # Add the adjacency of each node
        for n in graph.nodes():
            neighbors = list(graph.neighbors(n))
            self.adjacency[n] = neighbors

    def size_2(self, adjacency):
        # Function to define clicks of size two
        node = 0
        while node < 10:  # STEP 1 -> DEFINING PAIRS
            click = []
            for item in adjacency[node]:
                if [node, item] not in self.clicks:
                    if [item, node] not in self.clicks:
                        self.clicks.append([node, item])
            node += 1

    def size_n(self, adjacency):
        # Define clicks of size > 2
        node = 0
        while node < 10:
            actual = adjacency[node]
            click = []
            if len(actual) > 1:
                for i in actual:
                    another = adjacency[i]
                    for n in another:
                        if i != n:
                            if n in actual and n not in click:
                                click.append(n)
                                if node not in click: click.append(node)
                if len(click) > 2 and click not in self.clicks:  # else, actually are inside the clicks...
                    self.clicks.append(click)
            node += 1


"""
For test purposes, you can see the return of a instance of Clicks class
"""
# x = Clicks(nx.gnp_random_graph(10, .3))
# print(x.adjacency)
# print(x.clicks)
