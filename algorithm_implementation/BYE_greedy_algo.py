import networkx as nx

class BYEGreedyAlgo:
  name='Bar-Yehuda and Even\'s Greedy Algorithm' 
  def __call__(self, graph:nx.Graph):
    graph = graph.copy()
    S = []
    while graph.number_of_edges() > 0:
      edge = list(graph.edges)[0]
      if graph.nodes[edge[0]]['weight'] > graph.nodes[edge[1]]['weight']:
        edge = (edge[1], edge[0])
      u, v = edge
      graph.nodes[v]['weight'] -= graph.nodes[u]['weight']
      S.append(u)
      graph.remove_node(u)
    return S