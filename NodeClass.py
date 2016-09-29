class Node:
    def __init__(self, Name):
        self.__neighbours = []
        self.__name = Name
        self.__distance = None
        self.__previous = None

    # Preconditions:
    # Neighbour is a string, distance is an integer.
    def __addNeighbour(self, Neighbour, distance):
        self.__neighbours.append( (Neighbour, distance) )

    def __setFromString(self, String):
        # Format:
        # Name;Neighbour1Name,Neighbour1Dist,...,NeighbourNName,NeighbourNDist
        name, neighbours = String.split(";")
        self.__name = name
        neighbours = neighbours.split(",")

        for element in neighbours:
            add