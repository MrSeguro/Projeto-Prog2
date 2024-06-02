from Digraph import Digraph
from WeightEdge import WeightEdge

class Graph(Digraph):
    """
    
    """
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = WeightEdge(edge.getDestination(), edge.getSource(), edge.getWeight())
        Digraph.addEdge(self, rev)
