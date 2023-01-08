import networkx as nx
class BaselineAlgo:
  name='Naive algorithm'
  def __call__(self, graph:nx.Graph):
    return list(nx.approximation.min_weighted_vertex_cover(graph))