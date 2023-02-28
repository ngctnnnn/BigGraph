from VertexGraph import Vertex

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def main():
    g = Graph()             # Create an empty graph
    for i in range(6):      # Create a series of empty vertices with
        g.addVertex(i)      # simple keys (the numbers 0-5)
        
    g.addEdge(0,1,2)        # Start adding edges connecting the vertices
    g.addEdge(0,5,12)
    g.addEdge(1,2,1)
    g.addEdge(1,3,5)
    g.addEdge(3,2,7)
    g.addEdge(2,4,2)
    g.addEdge(4,3,4)
    g.addEdge(5,4,6)


    # Here's one way of printing out the Graph
    for v in g:     # This is possible because we implemented __iter__
        print(v)
    print("\n--------------\n")
    # Here's another way of printing out the graph
    for v in g:
        for w in v.getConnections():
            print("(%s, %s, %d)" % (v.getId(), w.getId(), v.getWeight(w)))

if __name__ == "__main__":
    main()
