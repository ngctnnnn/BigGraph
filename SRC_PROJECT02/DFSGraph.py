from VertexGraph import Graph


class DFSGraph(Graph):
    """Used to create a depth first forest. Inherits from the
    Graph class, but also adds a `time` variable used to track
    distances along the graph, as well as the two methods below.
    """
    
    def __init__(self):
        super().__init__()
        self.time = 0       # allows us to keep track of times when vertices
                            # are "discovered"
    
    def dfs(self):
        """Keeps track of time (ie. depth) across calls to dfsvisit
        for *all* nodes, not just a single node: we want to make sure
        that all nodes are considered, and that no vertices are left
        out of the forest.
        """
        for aVertex in self:            # iterate over all vertices
            aVertex.setColor('white')   # initial value of unexamined vertex
            aVertex.setPred(-1)         # no predecessor for first vertex
        for aVertex in self:            # now start working our way through
            if aVertex.getColor() == 'white':   # a depth-first exploration
                self.dfsvisit(aVertex)          # of the vertices
    
    def dfsvisit(self, startVertex):
        """Effectively uses a stack (by calling itself recursively) to
        explore down through the depth of the graph.
        """
        startVertex.setColor('gray')        # Gray color indicates that this
                                            # vertex is the one being explored
        self.time += 1                      # Increment the timer
        startVertex.setDiscovery(self.time) # Record the current time for this 
                                            # vertex's discovery
        for nextVertex in startVertex.getConnections(): # check all connections
            if nextVertex.getColor() == 'white':        # if we've touched this
                nextVertex.setPred(startVertex)         # reset pred to our start
                self.dfsvisit(nextVertex)               # continue depth search
        startVertex.setColor('black')       # After exploring all the way down
        self.time += 1                      # Last increment
        startVertex.setFinish(self.time)    # Stop "timing"



if __name__ == '__main__':

    g = DFSGraph()
    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')
    g.addVertex('F')
    g.addEdge('A', 'B', 1)
    g.addEdge('B', 'C', 1)
    g.addEdge('A', 'D', 1)
    g.addEdge('B', 'D', 1)
    g.addEdge('D', 'E', 1)
    g.addEdge('E', 'F', 1)
    g.addEdge('F', 'C', 1)
    g.addEdge('E', 'B', 1)
    g.dfs()
    
    for node in g:
        print(node.getId(), node.getDiscovery(), node.getFinish())


    # g = DFSGraph()
    # for i in range(6):
    #     g.addVertex(i)
    # # print(g.vertList)
    # g.addEdge(0, 1, 5)
    # g.addEdge(1, 2, 4)
    # g.addEdge(2, 3, 9)
    # g.addEdge(3, 4, 7)
    
    # g.addEdge(4, 0, 1)
    # g.addEdge(0, 5, 2)
    # g.addEdge(5, 4, 8)
    # g.addEdge(3, 5, 3)
    # g.addEdge(5, 2, 1)
    # g.dfs()