from Digraph import Digraph
from Edge import Edge

class Graph(Digraph):
    
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource(), edge.getValue())
        Digraph.addEdge(self, rev)
