from Edge import Edge
from Node import Node
from IDNode import IDNode
from Search import Search

class ShortestPathFile:
    def __init__(self, myLevadasNetwork_file, myStations_file, myResults_file):
        self.graph = self.read_graph(myLevadasNetwork_file)
        self.nodes = self.read_nodes(myStations_file)
        self.output_file = myResults_file

    def read_graph(self, filename):
        graph = {}
        file = open(filename, 'r')
        for line in file:
            if not line.startswith('#') and line.strip() != '':
                info = line.split(', ')
                node_id = info[0].strip()
                node_name = info[1].strip()
                connections = info[2].strip()[1:-1].split('), (')
                if node_id not in graph:
                    graph[node_id] = []
                for connection in connections:
                    connections_id, weight = connection.split(', ')
                    connections_id = connections_id.strip('(').strip(')').strip("'")
                    weight = int(weight.strip('(').strip(')').strip())
                    graph[node_id].append((connections_id, weight))

        file.close()
        return graph
    
    def read_nodes(self, filename):
        pairs = []
        file = open(filename, 'r')
        for line in file:
            if '-' in line:
                start, end = line.strip().split('-')
                pairs.append((start.strip(), end.strip()))

        file.close()
        return pairs
    
    def getPathValue(self, path):
        value = 0
        for i in range(len(path) - 1):
            for edge in self.graph.get(path[i], []):
                if edge[0] == path[i + 1]:
                    value += edge[1]

        return value


    def formatOutput(self, paths, start, end):
        if not paths:
            return f"{start} and {end} do not communicate\n"

        output_lines = []
        for path, value in paths:
            formatted_path = ', '.join(path)
            output_lines.append(f"{int(value)}, {formatted_path}\n")

        return ''.join(output_lines)
    
    def results_to_file(self):
        output_file = open(self.output_file, 'w')
        for start_name, end_name in self.nodes:
            output_file.write(f"# {start_name} - {end_name}\n")
            if start_name in self.graph and end_name in self.graph:
                paths = self.search(self.graph, start_name, end_name, maxPaths=3)
                output_file.write(self.formatOutput(paths, start_name, end_name))
            else:
                output_file.write(f"{start_name or end_name} out of the network\n")
            output_file.write("\n")

        output_file.close()

