import sys

class Vertex(object):
    """Describes a vertex object in terms of a "key" and a
    dictionary that indicates edges to neighboring vertices with
    a specified weight.
    """
    def __init__(self, key):
        """Constructs a vertex with a key value (no payload in
        this example), and an empty dictionary in which we'll
        store other vertices to which this vertex is connected.
        """
        self.id = key
        self.connectedTo = {}   # empty dictionary for vertices
        self.color = 'white'
        self.distance = 0
        self.predecessor = None
        self.discovery = 0           # discovery time
        self.finish = 0            # finish time

    def addNeighbor(self, neighbor, weight=0):
        """Creates a new vertex entry in the dictionary, to which this
        vertex is connected by an edge. If a weight is not indicated,
        default weight is 0.
        """
        self.connectedTo[neighbor] = weight

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    def setPred(self, predecessor):
        self.predecessor = predecessor

    def getPred(self):
        return self.predecessor

    def setDiscovery(self, dtime):
        self.discovery = dtime

    def getDiscovery(self):
        return self.discovery

    def setFinish(self, ftime):
        self.finish = ftime

    def getFinish(self):
        return self.finish

    def getConnections(self):
        """Returns the id values of the vertices we're connected to
        """
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

    def __repr__(self):
        """Returns a representation of the graph, suitable for printing."""
        return "Vertex[id=" + str(self.id) + \
                     ',color=' + self.color + \
                     ",disc=" + str(self.discovery) + \
                     ",fin=" + str(self.finish) + \
                     ",dist=" + str(self.distance) + \
                     ",pred\t[" + str(self.predecessor) + \
                     "],neighbors=" + str([e.id for e in self.connectedTo]) + "]\n"