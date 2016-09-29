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

        for i in range(len(neighbours)):
            if i % 2 == 0:
                self.__addNeighbour( neighbours[i],int(neighbours[i+1]) )