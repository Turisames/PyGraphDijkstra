import  GraphClass as gc

def ask_file():
    print("Give the name of the file that has the graph you want to inspect.")
    print("Empty space will abort this inquiry.")
    success = False
    while success == False:
        filename = input()
        if filename.strip() == "":
            print("Give an actual filename, with characters.")
            return False
        try:
            file = open(filename)
            file.close()
            break
        except FileNotFoundError:
            print("That file does not exist.")
            print("Try another one.")
            continue
        except EOFError:
            print("No data could be read from the file.")
            continue

    return filename

def ask_destination():
    print("Which part of the graph would you like to start at?")
    start  = input()
    print("Where would you like to go on the graph?")
    finish = input()

    return start, finish

def main():
    command = None
    graph = gc.Graph()
    while command != "":
        print("What would you like to do?")
        print("a) Read a file.")
        print("b) Find a route.")
        print("c) Print the whole graph.")
        print("Press enter to quit.")
        command = input()
        command = command.lower()

        # Clean up the input.
        command = command.strip()
        if len(command) > 1 and command[1] == ")":
            command = command[0]
        #
        if command == "a":
            fileName = ask_file()
            if fileName != False:
                graph.__createNodesFromFile__(fileName)
        elif command == "b":
            Start, Finish = ask_destination()
            graph.__figureRoute__(Start, Finish)
        elif command == "c":
            print(graph)
        # End program.
        elif command == "":
            break

main()