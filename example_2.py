from util.ColorManager import StringColor

from generator.graph_interface import Graph
from generator.directed_graph import DirectedGraph
from generator.undirected_graph import UndirectedGraph

from algorithms.path_finding import GraphSearch

import networkx as nx

"""
Construct graph with directed or undirected graph and use adjacency file as a list
"""
G = Graph(graph_data_file='data/example_data2.txt', is_directed=False)

"""
Get properties of graph (including num_nodes, num_edges, num_self_loops, node_list, edge_list)
"""
print(StringColor.CYAN+ f"[Result] Properties of graph" + StringColor.END) 
print(G)
G.visualization(scale_coefficient=3.5, save_path="visualization/example2_graph.png", verbose=0, figsize_h=12, figsize_w=10)

"""
Subgraph
"""
print(StringColor.CYAN+ f"[Result] Properties of sub-graph" + StringColor.END) 
sub_graph = Graph(copy_graph=G.getSubgraph(['FOOD', 'FOOL', 'POLL', 'SAGE', 'PALE', 'PALM']))
print(sub_graph)
sub_graph.visualization(scale_coefficient=3.5, save_path='visualization/sub_graph_example2.png', verbose=0, figsize_h=12, figsize_w=10)

"""
Get adjacency list of graph
"""
print(G.getAdjacencyList())
