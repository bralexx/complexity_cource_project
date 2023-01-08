import networkx as nx
import numpy as np

def remove_zero_degree_nodes(graph):
  nodes_to_remove = [node for node in graph.nodes if graph.degree(node) == 0]
  graph.remove_nodes_from(nodes_to_remove)

class GreedyAlgo:
  name = 'Greedy Algo'
  def __call__(self, graph:nx.Graph):
    graph = graph.copy()
    remove_zero_degree_nodes(graph)
    S = []
    while graph.number_of_nodes() > 0:
      # print(graph.number_of_nodes())
      c = min([graph.nodes[node]['weight'] / graph.degree(node) for node in graph.nodes])
      # print(c)
      nodes_to_S = []
      for node in graph.nodes:
        graph.nodes[node]['weight'] -= graph.degree(node) * c
        if np.abs(graph.nodes[node]['weight']) <= 1e-6:
          nodes_to_S.append(node)
      S += nodes_to_S
      graph.remove_nodes_from(nodes_to_S)
      remove_zero_degree_nodes(graph)
    return S