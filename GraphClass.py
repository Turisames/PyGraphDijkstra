import NodeClass as nc

class Graph:
    def __init__(self):
        self.__nodes = {}

    def __str__(self):
        output = ""
        # TODO: I could probably make the following part a little bit more efficient
        # TODO: So I don't have to remove the line break at the end.
        for piece in self.__nodes:
            node = self.__nodes[ piece ]
            output += str(node) + "\n"
        return output[:-1]

    def __createNodesFromFile__(self, fileName = ""):
        file = open(fileName, 'r', encoding="utf-8")
        for line in file:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                self.__nodes[ line.split(';')[0] ] = nc.Node().__createFromString__(line)
                #self.__nodes.append(nc.Node().__createFromString__(line))
        file.close()

    def __setAllUnvisited__(self):
        for node in self.__nodes:
            current = self.__nodes[ node ]
            current.__setVisited__( False )
            current.__setNext__( None )
            current.__setDistance__( None )

    def __checkNeighbours__(self, current, dist, closest, Finish):
        for neighbourTuple in current.__neighbours__():

            # The neighbours are stored as Tuple.
            # This line will draw out the node instance.
            neighbour = self.__nodes[ neighbourTuple[0] ]

            # A visited node will never be checked again.
            if not neighbour.__visited__():
                '''Compare the newly calculated tentative distance to the current assigned value
                and assign the smaller one.
                For example, if the current node A is marked with a distance of 6,
                and the edge connecting it with a neighbor B has length 2,'''

                if neighbour.__distance__() == None:
                    neighbour.__setDistance__( dist + neighbourTuple[1] )

                if closest == None or closest.__distance__() > neighbour.__distance__():
                    neighbour.__setDistance__( dist + neighbourTuple[1] )
                    closest = neighbour

                # If we can see the Finish now, move onto it right away!
                # Then again, as an optimizing procedure it's rather insignificant
                if neighbour.__name__() == Finish:
                    closest = neighbour
                    break

                # Otherwise, keep looking.
                if neighbour.__distance__() > ( dist + neighbourTuple[1] ):
                    '''then the distance to B (through A) will be 6 + 2 = 8.
                    If B was previously marked with a distance greater than 8
                    then change it to 8.
                    Otherwise, keep the current value.'''
                    neighbour.__setDistance__( dist + neighbourTuple[1] )
                print( neighbour.__name__(), neighbour.__distance__() )
        return current, dist, closest

    def __pickNextNode__(self, closest):
        # The actual following node should be the one closest to the source.
            for nodekey in self.__nodes:
                node = self.__nodes[ nodekey ]

                # The node has not been visited
                if not node.__visited__():
                    # The distance is not infinite and its distance is smaller
                    # than the one that's closest to the current node.
                    if node.__distance__() != None and \
                                    node.__distance__() < closest.__distance__():
                        closest = node
            return closest

    def __algo__(self, current, dist, Finish = nc.Node):
        '''For the current node, consider all of its unvisited neighbors
        and calculate their tentative distances.
        '''
        # This one only goes for the first call of this function, in practice.
        if type(current) is str:
            current = self.__nodes[ current ]
            current.__setDistance__( 0 ) # First round.

        ''' Initiating the variable "closest"
            At the start of the function, the variable closest means
            "closest to current node"
        '''
        closest = None

        current, dist, closest = self.__checkNeighbours__( current, dist, closest, Finish )

        '''When we are done considering all of the neighbors of the current node,
        mark the current node as visited and remove it from the unvisited set.'''
        current.__setVisited__( True )
        '''
        if self.__nodes[ Finish ].__visited__():
            # The algorithm was a success.
            return True
        '''
        # This is where we go to the next node.
        if closest != None:
            # -- as we move on to the next one.
            current.__setNext__( closest )

            ''' From this line on, closest refers to
            "closest to source"'''
            closest = self.__pickNextNode__( closest )

            # The search has to continue
            if not self.__nodes[ Finish ].__visited__():

                current = closest
                # The distance will change.
                dist = current.__distance__()
                return self.__algo__(current, dist, Finish)

            # We've reached the right one.
            elif self.__nodes[ Finish ].__visited__():
                return True
        # This is where we get to, if no reasonable route could be found.
        else:
            return False

    def __figureRoute__(self, Start = nc.Node, Finish = nc.Node):
        Result = False
        algorithm_can_be_done = True
        if Start not in self.__nodes:
            print("Start node \'" + Start + "\' does not exist.")
            algorithm_can_be_done = False
        if Finish not in self.__nodes:
            print("Finish node \'" + Finish + "\' does not exist.")
            algorithm_can_be_done = False
        if algorithm_can_be_done == True:
            current = Start
            dist = 0
            self.__setAllUnvisited__()
            Result = self.__algo__(current, dist, Finish)

        if Result == False:
            # The whole thing failed.
            print("No route could be found.\n")
        elif Result == True:
            current = self.__nodes[ Start ]
            print("The route is:")
            while current.__name__() != Finish:
                print( current.__name__() + " " + str(current.__distance__()) )
                current = current.__next__()
            print( current.__name__() + " " + str(current.__distance__()) )
            print("Done.")