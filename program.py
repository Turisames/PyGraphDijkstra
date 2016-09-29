'''
In this program I simply exercise using graphs
and try to understand and master Dijkstra's algorithm.
'''

from random import randint
from NodeClass import *

def main():

    listOfNodes = []
    for i in range(randint(2,11)):
        listOfNodes.append( Node( i ) )

    currentNode = None
    initialNode = None
    finalNode = None

def getFileName():
    return input("Give the name of the file you want me to read. ")

def createNodesFromFile(fileName = None):
    if fileName == None:
        fileName = getFileName()


main()
