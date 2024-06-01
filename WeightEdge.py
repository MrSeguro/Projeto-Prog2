from Edge import Edge

class WeightEdge(Edge):
    """
    Class of Weighted Edges 
    """
    
    def __init__(self, src, dest, weight=1.0):
        """
        Constructs a Weighted Edge
        
        Requires:
        src and dest Edges
        Ensures:
        Weighted Edge such that src == self.getSource() and dest == self.getDestination()
        """
        super().__init__(src, dest)
        self._weight = weight
    
    def getWeight(self):
        """
        Gets the weight of the Edge
        """
        return self._weight
    
    def __eq__(self, other):
        """
        Compares two weighted edges by their characteristics

        Ensures:
        Returns True if the source, destination, and weight are equal, otherwise False
        """
        return super().__eq__(other) and self._weight == other._weight

    def __lt__(self, other):
        """
        Ensures:
        Returns True if the weight of this edge is less than the weight of the other edge
        """
        return self._weight < other._weight
    
    def __str__(self):
        """
        String representation
        """
        return self._src.getName() + '->' + self._dest.getName() + ', ' + self._weight.getWeight() 