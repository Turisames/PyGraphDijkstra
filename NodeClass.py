class Node:
    def __init__(self):
        self.__neighbours = []
        self.__name = ""
        self.__visited = False
        self.__distance = None
        self.__previous = None

    # Preconditions:
    # Neighbour is a string, distance is an integer.
    def __addNeighbour__(self, Neighbour, weight):
        self.__neighbours.append( (Neighbour, weight) )

    def __setFromString__(self, String):
        # Format:
        # Name;Neighbour1Name,Neighbour1Dist,...,NeighbourNName,NeighbourNDist
        name, neighbours = String.split(";")
        self.__name = name
        neighbours = neighbours.split(",")

        for i in range(len(neighbours)):
            if i % 2 == 0:
                self.__addNeighbour( neighbours[i],int(neighbours[i+1]) )

    def __setVisited__(self, newState):
        self.__visited = newState

    def __setDistance__(self, Distance):
        self.__distance = Distance

    def __distance__(self):
        return self.__distance

    def __visited__(self):
        return self.__visited

    def __neighbours__(self):
        return self.__neighbours

    def __name__(self):
        return self.__name

    def __str__(self):
        output = self.__name
        for node in self.__neighbours:
            output += "\n\t" + node.__name__()
        return output