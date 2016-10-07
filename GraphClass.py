import NodeClass as nc

class Graph:
    def __init__(self):
        self.__nodes = []

    def __createNodesFromFile__(fileName = None):
        file = open(fileName, 'r', encoding="utf-8")
        lines = []
        for line in file
            line = line.strip()
            if line != "" or line[0] != "#":
                self.__nodes.append(nc.Node().__setFromString__(line))
        file.close()

    def __figureRoute__(self, Start = nc.Node, Finish = nc.Node):
        pass
        current = Start
        '''For the current node, consider all of its unvisited neighbors
        and calculate their tentative distances.
        Compare the newly calculated tentative distance to the current assigned value
        and assign the smaller one.
        For example, if the current node A is marked with a distance of 6,
        and the edge connecting it with a neighbor B has length 2,
        then the distance to B (through A) will be 6 + 2 = 8.
        If B was previously marked with a distance greater than 8
        then change it to 8.
        Otherwise, keep the current value.'''
        for neighbour in current.__neighbours__():
            neighbour[]

