class Node(object):
    def __init__(self, name):
        """
        Requires:
        name: string representing the name of the node
        Ensures:
        Initializes a node with the given name
        """
        self.name = name

    def getName(self):
        """
        Ensures:
        Returns the name of the node
        """
        return self.name
    
    def __hash__(self):
        """
        Ensures:
        Returns a hash value based on the node's name
        """
        return hash(self.name)

    def __eq__(self, other):
        """
        Requires:
        a Node

        Ensures:
        Returns True if the names of the nodes are equal, otherwise False
        """
        return self.name == other.name

    def __lt__(self, other):
        """
        Requires:
        other: a Node
        Ensures:
        Returns True if the name of this node is less than the name of the other node
        """
        return self.name < other.name

    def __str__(self):
        """
        Ensures:
        Returns the name of the node as a string
        """
        return self.name