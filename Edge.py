class Edge(object):
    """
    Class of Edges
    """
    
    def __init__(self, src, dest):
        """
        Constructs an Edge
        
        Requires:
        src and dst Nodes
        Ensures:
        Edge such that src == self.getSource() and dest == self.getDestination() 
        """
        self._src = src
        self._dest = dest

        
    def getSource(self):
        """
        Gets the source Node
        """
        return self._src

    
    def getDestination(self):
        """
        Gets the destination Node
        """
        return self._dest

    def __eq__(self, other):
        """
        Compares two edges by their caracteristics

        Ensures:
        Returns True if the names of the nodes are equal, otherwise False 
        """
        return (self.src == other.src and 
                self.dest == other.dest)

    def __str__(self):
        """
        String representation
        """
        return self._src.getName() + '->' + self._dest.getName() 

