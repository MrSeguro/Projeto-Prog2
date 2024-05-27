from Digraph import Digraph
from Edge import Edge
from Node import Node

def getPathValue(path, graph):
    """
    Requires:
    path: a list of Nodes
    graph: a Digraph
    Ensures:
    Returns the total weight of the path
    """
    value = 0.0
    for i in range(len(path) - 1):
        for edge in graph.getEdges(path[i]):
            if edge.getDestination() == path[i + 1]:
                value += edge.getValue()
    return value

def DFS(graph, start, end, path, paths, maxPaths=3):
    """
    Depth first search in a directed graph

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """

    path = path + [start]
    print('Current DFS path:', path)

    if start == end:
        path_value = getPathValue(path, graph)
        paths.append((path, path_value))
        paths.sort(key=lambda x: x[1])
        while len(paths) > maxPaths:
            paths.pop()
        return paths

    for node in graph.childrenOf(start):
        if node not in path:
            if len(paths) < maxPaths or getPathValue(path, graph) < paths[-1][1]:
                newPaths = DFS(graph, node, end, path, paths, maxPaths)
                if newPaths:
                    paths = newPaths
    return paths

def search(graph, start, end, maxPaths=3):
    """
    Wrapper function to initialize DFS function

    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """

    return DFS(graph, start, end, [], [], maxPaths)

def printPath(path):
    """
    Requires:
    path: a list of Nodes
    Ensures:
    Returns a string representation of the path
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def testSP():
    """
    Function to test search in a graph with a specific example
    """
    
    nodes = []
    
    for name in range(7):  # Create 7 nodes
        nodes.append(Node(str(name)))
        
    g = Digraph()
    
    for n in nodes:
        g.addNode(n)
        
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[6]))
    g.addEdge(Edge(nodes[4], nodes[0]))
    g.addEdge(Edge(nodes[4], nodes[5]))
    g.addEdge(Edge(nodes[4], nodes[6]))
    g.addEdge(Edge(nodes[6], nodes[5]))
    
    sp = search(g, nodes[0], nodes[5])
    
    print('Shortest path(s) found by DFS:', sp)
    for path, value in sp:
        print('Path:', printPath(path), 'Value:', value)

testSP()
