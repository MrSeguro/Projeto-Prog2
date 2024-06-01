from Node import Node

class IDNode(Node):
    """
    Creates the ID needed to identify the node
    """
    def __init__(self, name, ID):
        """
        Requires:
        name: string representing the name of the node
        ID: integer representing the ID of the node
        Ensures:
        Initializes a node with the given name and ID
        """
        super().__init__(name)
        self.ID = ID

    def getID(self):
        """
        Ensures:
        Returns the ID of the node
        """
        return self.ID

    def __str__(self):
        """
        Ensures:
        Returns the name and ID of the node as a string
        """
        return self.getID() + ', ' + self.getName() 