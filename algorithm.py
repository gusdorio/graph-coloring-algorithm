# Function to get the matrix of the adjacency for each node
def adjacency(graph):
  dic = {}
  for n in graph.nodes():
    neighbors = list(graph.neighbors(n))
    dic[n] = neighbors
  return dic


# Function to define clicks
# def clicks(dic):
#   count = 0
#   for i in dic[count]:
#     for n in range(dic[count]):


