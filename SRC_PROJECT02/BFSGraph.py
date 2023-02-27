from VertexGraph import Graph, Vertex
from Queue import Queue

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        # print(line[-1])
        # last char is '\n'
        word = line[:-1]
        # print(word)
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

# implementation of BFS
def bfs(g, start):
    """Performs a BFS on Graph `g` beginning at vertex `start`
    Once we're done, the graph will have identified a series of
    predecessor links that can be followed to a given solution.
    """
    start.setDistance(0)        # this first vertex is 0 away from itself ;)
    start.setPred(None)         # and there's nothing before this vertex
    q = Queue() 
    q.enqueue(start)            # place start vertex in the queue
    while q.size() > 0:
        current_vertex = q.dequeue()    # Get next item in line
        for neighbor in current_vertex.getConnections():
            if neighbor.getColor() == "white":      # first time seeing it
                neighbor.setColor("gray")
                neighbor.setDistance(current_vertex.getDistance() + 1)
                neighbor.setPred(current_vertex)
                q.enqueue(neighbor)
            # once we've explored all the neighbors...
        current_vertex.setColor("black")

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

if __name__ == '__main__':
    wordgraph = buildGraph("fourletterwords.txt")
    bfs(wordgraph, wordgraph.getVertex('FOOL'))
    traverse(wordgraph.getVertex('SAGE'))



