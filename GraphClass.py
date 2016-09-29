
class Graph:
    def __init__(self):
        self.__nodes = []

    def __createNodesFromFile__(fileName = None):
        if fileName == None:
            fileName = getFileName()
        file = open(fileName, 'r', encoding="utf-8")
        lines = []
        for line in file
            line = line.strip()
            if line != "" or line[0] != "#":
                lines.append(line)
        file.close()