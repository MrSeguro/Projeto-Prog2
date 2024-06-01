from Edge import Edge
from Node import Node

class ShortestPathFile(Node, Edge):
    """
    
    """
    def __init__(self, filename):
        self.graph = self.read_graph(filename)
    
    def read_graph(self, filename):
        graph = {}
        file = open(filename, 'r')
        for line in file:
            node1, node2, value = line.strip().split()
            if node1 not in graph:
                graph[node1] = []
            graph[node1].append((node2, int(value)))
            if node2 not in graph:
                graph[node2] = []
            graph[node2].append((node1, int(value)))
        file.close()
        return graph
    
    
    def results_to_file(self, start, destination, output_filename, paths):
        """
        Writes the 3 shortest paths in a file.
        """

        file = open(output_filename, 'w')
        if not paths:
            file.write("No path found from {} to {}\n".format(start, destination))
        else:
            for i, (cost, path) in enumerate(paths):
                file.write("Path {}: Weight={}, Path={}\n".format(i+1, cost, ' -> '.join(path)))

        file.close()



