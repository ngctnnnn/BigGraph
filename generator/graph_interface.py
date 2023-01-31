from generator.directed_graph import DirectedGraph
from generator.undirected_graph import UndirectedGraph

from util.ColorManager import StringColor

class Graph(UndirectedGraph): # Abstract graph interface
    def __init__(self, copy_graph = None, graph_data_file: str = None, is_directed: bool = None) -> None:
        """
        Constructor
        """
        if is_directed is None:
            assert NotImplementedError(StringColor.BOLD + StringColor.RED + f"[Error] This type of graph is not yet implemented or not correctly provided!" + StringColor.END)
        if is_directed:
            self.__dict__ = DirectedGraph(copy_graph, graph_data_file).__dict__.copy()
        else:
            self.__dict__ = UndirectedGraph(copy_graph, graph_data_file).__dict__.copy()