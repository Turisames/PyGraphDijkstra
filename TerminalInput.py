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

if __name__ == '__main__':
    graph = gc.Graph()
    fileName = ask_file()
    graph.__createNodesFromFile__(fileName)