from Graph import Graph
from WeightEdge import WeightEdge
from IDNode import IDNode

def GraphCreator(filepath):
    """
    Function to create a graph from a given file.

    Requires:
    filepath: a string with the path to the file

    Ensures:
    Returns a graph object
    """
    graph = Graph()
    levadasList = []

    # Open and read the file
    fp = open(filepath, encoding='utf-8')
    for line in fp.readlines():
        line = line.strip()
        line = line.split(', ', 2)
        if line != ['']:
            levadasList.append(line)
    fp.close()

    # Remove the header
    if levadasList:
        levadasList.pop(0)

    added_nodes = {}
    # Add nodes
    for levada in levadasList:
        node_id, node_name, edges = levada[0], levada[1], levada[2]
        if node_id not in added_nodes:
            new_node = IDNode(node_id, node_name)
            graph.addNode(new_node)
            added_nodes[node_id] = new_node

    # Add edges
    for levada in levadasList:
        node_id, node_name, edges = levada[0], levada[1], levada[2]

        if edges == '[]':
            continue
        
        edges = edges.strip('[]').split('), (')
        for edge in edges:
            edge = edge.strip('()')
            if ', ' in edge:
                parts = edge.split(', ')
                if len(parts) == 2:
                    dest_id, weight = parts
                    weight = float(weight)
                    if dest_id in added_nodes:
                        source_node = added_nodes[node_id]
                        dest_node = added_nodes[dest_id]
                        graph.addEdge(WeightEdge(source_node, dest_node, weight))
    return graph


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

def testSP():
    """
    Function to test search in a graph with a specific example
    """
    graph = GraphCreator("myLevadasNetworkStor.txt")
    if graph:
        print(graph)
        nodes = list(graph.getNodes())
        if len(nodes) > 1:
            start_node = nodes[0]
            end_node = nodes[-1]
            paths = search(graph, start_node, end_node)
            for path, weight in paths:
                print(f"Path: {printPath(path)} with total weight: {weight}")
        else:
            print("Not enough nodes in the graph.")
    else:
        print("Failed to create the graph.")

testSP()
