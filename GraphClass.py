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

    def __setAllUnvisited__(self):
        for node in self.__nodes:
            node.__setVisited__( False )

    def __figureRoute__(self, Start = nc.Node, Finish = nc.Node):
        pass
        current = Start
        closest = None
        dist = 0
        '''For the current node, consider all of its unvisited neighbors
        and calculate their tentative distances.
        '''
        for neighbour in current.__neighbours__():
            '''Compare the newly calculated tentative distance to the current assigned value
            and assign the smaller one.
            For example, if the current node A is marked with a distance of 6,
            and the edge connecting it with a neighbor B has length 2,'''
            if closest == None or closest.__distance__() > neighbour.__distance__():
                closest = neighbour

            if neighbour[0].__distance__() > ( dist + neighbour[1] ):
                '''then the distance to B (through A) will be 6 + 2 = 8.
                If B was previously marked with a distance greater than 8
                then change it to 8.
                Otherwise, keep the current value.'''
                neighbour[0].__setDistance__( dist + neighbour[1] )

        '''When we are done considering all of the neighbors of the current node,
        mark the current node as visited and remove it from the unvisited set.
        A visited node will never be checked again.'''
        current.__setVisited__( True )