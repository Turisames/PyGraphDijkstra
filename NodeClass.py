class Node:
    def __init__(self, Name):
        self.__neighbours = []
        self.__name = Name
        self.__distance = None
        self.__previous = None