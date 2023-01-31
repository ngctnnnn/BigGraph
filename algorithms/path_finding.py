from collections import deque

from util.ColorManager import StringColor

class GraphSearch:
    def __init__(self, adjacency_graph: dict = None):
        assert adjacency_graph is not None, StringColor.BOLD + StringColor.RED + f"[Error] Graph is not provided!" + StringColor.END    
        self.graph = adjacency_graph
    
    def DFS(self):
        node_stack = [next(iter(self.graph))]
        visited = set()
        while node_stack:
            node_to_visit = node_stack.pop()
            if node_to_visit in visited:
                continue 
            visited.add(node_to_visit)
            for neighbor_node in self.graph[node_to_visit]:
                print(neighbor_node, end = ' ')
                node_stack.append(neighbor_node)
    
    def BFS(self):
        node_queue = deque([next(iter(self.graph))])
        visited = set()
        while node_queue:
            node_to_visit = node_queue.popleft()
            if node_to_visit in visited:
                continue 
            visited.add(node_to_visit)
            for neighbor_node in self.graph[node_to_visit]:
                print(neighbor_node, end = ' ')
                node_queue.append(neighbor_node)
    
    def search(self, algorithm_name: str = None):
        assert algorithm_name is not None, StringColor.BOLD + StringColor.RED + f"[Error] Graph search algorithm name is missing!" + StringColor.END
        if algorithm_name == 'dfs': 
            self.DFS()
        elif algorithm_name == 'bfs':
            self.BFS()
        else:
            raise NotImplementedError("This algorithm is not implemented yet! Currently support for 'dfs' and 'bfs' only.")