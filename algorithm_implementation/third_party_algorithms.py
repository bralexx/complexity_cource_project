import networkx as nx

class NXBuildinAlgo:
  name = "Networkx implementation"
  def __call__(self, graph):
    return nx.approximation.min_weighted_vertex_cover(graph)