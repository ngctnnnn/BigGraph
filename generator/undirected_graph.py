import os
import copy
from typing import List
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util.ColorManager import StringColor
from generator.directed_graph import DirectedGraph
import time

class UndirectedGraph(DirectedGraph):
    def __init__(self, copy_graph: nx.Graph() = None, graph_data_file: str = None):
        """
        Constructor 
        """
        super().__init__(copy_graph, graph_data_file)
        self.graph = self.graph.copy().to_undirected()
        if copy_graph is not None:
            self.graph = copy.deepcopy(copy_graph)
            self.edge_list: list = []
            self.graph_data_file = None
    
    def getAdjacencyList(self) -> dict:
        print("[Result] Adjacency list of the graph: ")
        for node in self.graph.adj:
            print(f"{node}", end = '')
            for adj_node in self.graph.neighbors(node):
                print(f",{adj_node}", end = '')
            print()
    
    def getSubgraph(self, nodes_to_retrieve: List[str]) -> nx.Graph():
        """
        Function to get subgraph from the big graph with a node to retrieve

        Args:
        nodes_to_retrieve (list) -- List of node to get subgraph from
        """
        return self.graph.subgraph(nodes_to_retrieve)