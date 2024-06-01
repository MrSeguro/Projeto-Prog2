from Graph import Graph
from WeightEdge import WeightEdge
from IDNode import IDNode

def getPathWeight(path, graph):
    """
    Requires:
    path is a list of Nodes and a graph a digraph
    Ensures:
    Returns the total weight of the path
    """
    weight = 0.0
    for i in range(len(path) - 1):
        for edge in graph.getEdges(path[i]):
            if edge.getDestination() == path[i + 1]:
                weight += edge.getWeight()
    return weight

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
        path_weight = getPathWeight(path, graph)
        paths.append((path, path_weight))
        paths.sort(key=lambda x: x[1])
        while len(paths) > maxPaths:
            paths.pop()
        return paths

    for node in graph.childrenOf(start):
        if node not in path:
            if len(paths) < maxPaths or getPathWeight(path, graph) < paths[-1][1]:
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
        result += str(path[i].getName())
        if i != len(path) - 1:
            result += '->'
    return result

def GraphCreator(filepath):
    """
    
    """
    graph = Graph()
    levadasList = []

    fp = open(filepath, encoding='utf-8')
    
    for line in fp.readlines():
        line = line.strip()
        line = line.split(', ', 2)

        if line != ['']:
            levadasList.append(line)

    levadasList.pop(0)
    for levada in levadasList:
        graph.addNode(IDNode(levada[0],levada[1]))

    for levada in levadasList:
        if len(levada) <= 3:
            edges = levada[2].strip('[]').split('), (')
            start_node = IDNode(levada[0], levada[1])

        for edge in edges:
            edge = edge.strip('()')
            edge_parts = edge.split(', ')
            dest_id = str(edge_parts[0]) 
            weight = int(edge_parts[1])

        

            dest_node = next((node for node in graph._nodes if node.getID() == dest_id), None)
            if not dest_node:
                dest_node = IDNode(dest_id, weight)
                graph.addNode(dest_node)

            graph.addEdge(WeightEdge(start_node, dest_node, weight))

    fp.close()

    return graph

def test_graph():
    filepath = 'myLevadasNetworkStor.txt'
    graph = GraphCreator(filepath)
    
    # Example of start and end nodes for testing purposes
    start_node = next(node for node in graph._nodes if node.getName() == 'M' and node.getID() == 0)
    end_node = next(node for node in graph._nodes if node.getName() == 'PR' and node.getID() == 5)
    
    # Find the shortest path
    sp = search(graph, start_node, end_node)
    
    # Print the results
    print('Shortest path(s) found by DFS:')
    for path, value in sp:
        print('Path:', printPath(path), 'Weight:', value)

# Execute the test function
test_graph()

# def testSP():
#     """
#     Function to test search in a graph with a specific example
#     """
    
#     nodes = []
    
#     for ID in range(7):  # Create 7 nodes
#         nodes.append(IDNode(str(ID), str(ID)))  # Agora passamos o ID para o construtor do IDNode
        
#     g = Digraph()

#     for n in nodes:
#         g.addNode(n)
        
#     g.addEdge(WeightEdge(nodes[0], nodes[1], 5))
#     g.addEdge(WeightEdge(nodes[1], nodes[2], 8))
#     g.addEdge(WeightEdge(nodes[2], nodes[3], 10))
#     g.addEdge(WeightEdge(nodes[2], nodes[4], 4))
#     g.addEdge(WeightEdge(nodes[3], nodes[1], 7))
#     g.addEdge(WeightEdge(nodes[3], nodes[4], 14))
#     g.addEdge(WeightEdge(nodes[3], nodes[5], 10))
#     g.addEdge(WeightEdge(nodes[0], nodes[2], 11))
#     g.addEdge(WeightEdge(nodes[1], nodes[0], 3))
#     g.addEdge(WeightEdge(nodes[3], nodes[6], 10))
#     g.addEdge(WeightEdge(nodes[4], nodes[0], 21))
#     g.addEdge(WeightEdge(nodes[4], nodes[5], 22))
#     g.addEdge(WeightEdge(nodes[4], nodes[6], 20))
#     g.addEdge(WeightEdge(nodes[6], nodes[5], 5))
    
#     sp = search(g, nodes[0], nodes[5])
    
#     print('Shortest path(s) found by DFS:', sp)
#     for path, weight in sp:
#         print('Path:', printPath(path), 'Weight:', weight)

# testSP()
