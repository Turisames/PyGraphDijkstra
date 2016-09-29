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

    def __figureRoute__(self, Start, Finish):
        pass
