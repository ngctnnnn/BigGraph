import os
import copy
from typing import List
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from util.ColorManager import StringColor
import time

class DirectedGraph:
    def __init__(self, copy_graph: nx.DiGraph() = None, graph_data_file: str = None):
        """
        Constructor 
        """
        self.graph_data_file: str = graph_data_file
        self.edge_list: list = []
        if self.graph_data_file is not None:
            start = time.time()
            self.graph = nx.DiGraph(); self.readGraphFromFile()
            end = time.time()
            print(StringColor.CYAN + f"[Status] Read graph in {end - start} seconds" + StringColor.END)
        if copy_graph is not None:
            self.graph = copy.deepcopy(copy_graph)
            self.edge_list: list = []
            self.graph_data_file = None 
    
    def __str__(self):
        """
        Get property of the current graph
        """
        num_nodes = f"Number of nodes: {self.graph.number_of_nodes()}\n" 
        num_edges = f"Number of edges: {self.graph.number_of_edges()}\n"
        num_selfloops = f"Number of self-loops: {nx.number_of_selfloops(self.graph)}\n"
        
        node_list= f"List of nodes in graph: "
        cnt = 1
        sorted_graph_adj = sorted(self.graph.adj)
        for node in sorted_graph_adj:
            if cnt == len(self.graph.adj):
                node_list += node + '\n'
            else:
                node_list += node + ', '
                cnt += 1
        
        edge_list = f"Edge list of graph: \n"
        sorted_graph_edges = sorted(self.graph.edges(data=False))
        for u, v in sorted_graph_edges:
            edge_list += '(' + u + ', ' + v + ')\n'
        
        degree_list = f"List of nodes with respective degrees:\n"
        for node in sorted_graph_adj:
            degree_list += f"Node {node} has a degree of {self.getNodeDegree(node)}\n" 
        
        return num_nodes + num_edges + num_selfloops + node_list + edge_list + degree_list
        
    def addEdge(self, source_node: str, *linked_node) -> None:
        """
        Function to add adjacency nodes to the current node
        
        Args:
        source_node (str) -- the current node
        linked_node (*args) -- node(s) that is/are adjacent to the current node
        
        Returns:
        self.edge_list after being added adjacency nodes
        """
        for node in linked_node:
            self.edge_list.append((source_node, node))
        
    def readGraphFromFile(self) -> None:
        """
        Function to generate graph from adjacency list file
        """
        assert self.graph_data_file != None, StringColor.BOLD + StringColor.RED + f"[Error] Data for graph construction is missing!" + StringColor.END
        if not os.path.exists(self.graph_data_file):
            print(StringColor.BOLD + StringColor.RED + f"[Error] Json graph file is not found." + StringColor.END)

        f = open(self.graph_data_file, "r")
        for line in f.readlines():
            line = line.replace(' ', '') # Remove all spare `space` character
            adj_list = line.strip().split(',')
            source_node = adj_list[0]
            if isinstance((adj_list[1:]), list):
                args = adj_list[1:]
                for adj_node in args:
                    self.addEdge(source_node, adj_node)
            else:
                self.addEdge(source_node, adj_list[source_node])
        f.close()
        self.graph.add_edges_from(self.edge_list)

    def removeNode(self, node_to_remove: str) -> None:
        """
        Function to remove one node from the super graph
        
        Args:
        node_to_remove (str) -- Node that are about to be removed 
        
        Returns:
        self.graph after being prunned one node
        """
        self.graph.remove_node(node_to_remove)
    
    def removeEdge(self, u: str, v: str) -> None:
        """
        Function to remove one edge from the super graph
        
        Args:
        u, v (str, str) -- Edge-to-remove constructed by node `u` and `v`

        Returns:
        self.graph after being removed one edge
        """
        self.graph.remove_edge(u, v)
    
    def printNodes(self) -> None:
        """
        Function to print all nodes from graph
        """
        print(self.graph.nodes(data=False))
    
    def printEdges(self) -> None:
        """
        Function to print all edges from graph
        """
        print(self.graph.edges(data=False))
    
    def getNodeDegree(self, node: str) -> int:
        """
        Function to get degree of a node
        """
        return self.graph.degree(node)
       
    def getAdjacencyList(self) -> dict:
        """
        Function to get graph as an adjacency list
        """
        print("[Result] Adjacency of this graph:")
        graph_adjlist: dict = {}
        for node_edge in nx.generate_adjlist(self.graph):
            current_list = node_edge.split(' ')
            graph_adjlist[current_list[0]] = [current_list[_] for _ in range(1, len(current_list)) if current_list[_] != ' ']
        return graph_adjlist
    
    def getSubgraph(self, nodes_to_retrieve: List[str]) -> nx.DiGraph():
        """
        Function to get subgraph from the big graph with a node to retrieve

        Args:
        nodes_to_retrieve (list) -- List of node to get subgraph from
        """
        return self.graph.subgraph(nodes_to_retrieve)
    
    def visualization(self, figsize_h: float = 6.4, figsize_w: float = 4.8, scale_coefficient:float = 1, save_path: str = None, verbose: bool = 1) -> None:
        """
        Function to visualize graph
        
        Args:
        save_path (str) -- Path to save visualized graph image
        verbose (int)  -- If verbose is 1, then show graph image to screen
        """
        plt.clf() # Clear plt canvas
        plt.figure(figsize=(figsize_h, figsize_w))
        nx.draw_networkx(self.graph, node_size=300 * scale_coefficient, pos=nx.spring_layout(self.graph, scale=scale_coefficient))
        if save_path is not None:
            plt.savefig(save_path)
        if verbose:
            plt.show()
