from util.ColorManager import StringColor

from generator.graph_interface import Graph
from generator.directed_graph import DirectedGraph
from generator.undirected_graph import UndirectedGraph

from algorithms.path_finding import GraphSearch

G = Graph(graph_data_file='data/example_data1.txt', is_directed=True)
"""
Get properties of graph (including num_nodes, num_edges, num_self_loops, node_list, edge_list)
"""
print(StringColor.CYAN+ f"[Result] Properties of graph" + StringColor.END) 

print(G)



G.visualization(save_path="visualization/example1_graph.png", verbose=0, figsize_h=12, figsize_w=10)

"""
Subgraph
"""
print(StringColor.CYAN+ f"[Result] Properties of sub-graph" + StringColor.END) 
sub_graph = Graph(copy_graph=G.get_subgraph(['19', '192', '700', '1330', '30', '1412', '3352', '274', '5', '2']))
# print(sub_graph)
sub_graph.visualization(save_path='visualization/sub_graph_example1.png', verbose=0, figsize_h=16, figsize_w=10)