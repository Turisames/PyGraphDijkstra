import  GraphClass as gc

def if __name__ == '__main__':

def ask_file():
    print("Give the name of the file that has the graph you want to inspect.")
    filename = input()
    try:
        file = open(filename)
        file.close()
    except FileNotFoundError:
        print("That file does not exist.")
        print("Try another one.")
    except EOFError:
        print("No data could be read from the file.")

    file.close()
    return filename

def print_graph( Graph = gc.Graph ):
    print(Graph)

def ask_destination():
    print("Which part of the graph would you like to start at?")
    start  = input()
    print("Where would you like to go on the graph?")
    finish = input()

    return start, finish

if __name__ == '__main__':
    graph = gc.Graph()
    fileName = ask_file()
    graph.__createNodesFromFile__(fileName)

    Start, Finish = ask_destination()

    graph.__figureRoute__(Start, Finish)