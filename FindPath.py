class ShortestPathFinder:
    """
    Finds the 3 shortest paths (in terms of travel time) between stations using DFS.
    """
    def __init__(self, filename):
        self.graph = self.read_graph(filename)
    
    def read_graph(self, filename):
        graph = {}
        file = open(filename, 'r')
        for line in file:
            node1, node2, weight = line.strip().split()
            if node1 not in graph:
                graph[node1] = []
            graph[node1].append((node2, int(weight)))
            if node2 not in graph:
                graph[node2] = []
            graph[node2].append((node1, int(weight)))
        file.close()
        return graph
    
    def dephtFirstSearch (self, current, destination, path, cost, paths, visited):
        if current == destination and len(path) >= 3:
            paths.append((cost, path[:]))
            return
        
        for neighbor, weight in self.graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                self.dfs(neighbor, destination, path, cost + weight, paths, visited)
                path.pop()
                visited.remove(neighbor)
    
    def shortest_paths(self, start, destination, num_paths=3):
        """
        Finds the 3 shortest paths using DFS.
        """
        paths = []
        self.dfs(start, destination, [start], 0, paths, {start})
        paths.sort(key=lambda x: x[0])
        return paths[:num_paths]
    
    def shortest_paths_to_file(self, start, destination, output_filename, num_paths=3):
        """
        Writes the 3 shortest paths to a file.
        """
        paths = self.shortest_paths(start, destination, num_paths)
        
        with open(output_filename, 'w') as file:
            if not paths:
                file.write("No path found from {} to {}\n".format(start, destination))
            else:
                for i, (cost, path) in enumerate(paths):
                    file.write("Path {}: Cost={}, Path={}\n".format(i+1, cost, ' -> '.join(path)))
