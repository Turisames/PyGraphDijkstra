class Node:
    def __init__(self):
        self.__neighbours = []
        self.__name = ""
        self.__distance = None
        self.__previous = None

    # Preconditions:
    # Neighbour is a string, distance is an integer.
    def __addNeighbour__(self, Neighbour, distance):
        self.__neighbours.append( (Neighbour, distance) )

    def __setFromString__(self, String):
        # Format:
        # Name;Neighbour1Name,Neighbour1Dist,...,NeighbourNName,NeighbourNDist
        name, neighbours = String.split(";")
        self.__name = name
        neighbours = neighbours.split(",")

        for i in range(len(neighbours)):
            if i % 2 == 0:
                self.__addNeighbour( neighbours[i],int(neighbours[i+1]) )