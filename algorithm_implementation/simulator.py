import pandas as pd
import numpy as np
import networkx as nx
import time 
from tqdm.notebook import tqdm

def correctness_check(graph:nx.Graph, vertex_cover):
  if len(np.unique(vertex_cover)) != len(vertex_cover):
    return False
  supp_graph = graph.subgraph([node for node in graph.nodes if node not in vertex_cover])
  return supp_graph.number_of_edges() == 0

def weight(graph:nx.Graph, vertex_set):
  return sum([graph.nodes[node]['weight'] for node in vertex_set])

class Simulator:
  def simulate(self, algorithms, graphs, repetitions=1):
    results = []
    for graph in tqdm(graphs):
      graph_results = {'scenario_info':{'graph':graph, 'name':graph.name}}
      for algo in algorithms:
        answers = []
        # testing
        start = time.time()
        for _ in range(repetitions):
          answers.append(algo(graph))
        end = time.time()

        for answer in answers:
          assert correctness_check(graph, answer), "Output set isn't vertex cover"
        
        graph_results[algo.name] = {
          'time':(end - start) / repetitions, 
          'weight':weight(graph, answers[0])
        }
      results.append(graph_results)
    return results
  
  def simulate_and_parse(self, algorithms, graphs, repetitions=1):
    results = self.simulate(algorithms, graphs,repetitions=repetitions)
    df1_T = []
    for obj in results:
      df1_T.append({})
      for key_outer in obj.keys():
        for key_inner in obj[key_outer].keys():
          df1_T[-1][(key_outer, key_inner)] = obj[key_outer][key_inner]
    mi = pd.MultiIndex.from_tuples(df1_T[0].keys())
    return pd.DataFrame(df1_T, columns=mi)