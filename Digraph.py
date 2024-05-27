from Node import Node
from Edge import Edge

class Digraph(object):
    def __init__(self, nodes=[], edges=[]):
        self._nodes = []
        self._edges = {}
        for node in nodes:
            self.addNode(Node(node))
        for edge in edges:
            src, dest, value = edge
            self.addEdge(Edge(Node(src), Node(dest), value))

    def addNode(self, node):
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        self._edges[src].append(edge)

    def childrenOf(self, node):
        return [edge.getDestination() for edge in self._edges[node]]

    def getEdges(self, node):
        return self._edges[node]

    def hasNode(self, node):
        return node in self._nodes

    def __str__(self):
        result = ''
        for src in self._nodes:
            for edge in self._edges[src]:
                result += str(edge) + '\n'
        return result
