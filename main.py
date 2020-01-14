from SudokuLibrary import *
import time

def formatTime(secs):
    hours = int(secs//3600)
    minutes = int((secs%3600)//60)
    seconds = int(((secs%3600)%60))

    return str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds."

def main():
    response = input("Start a game (Y or N): ")
    if response == 'y' or response == 'Y':
        level = input("Select a difficulty by typing 'E' for Easy, 'M' for Medium or 'H' for hard: ")
        while level != 'E' and level != 'M' and level != 'H':
            level = input("Select a difficulty by typing 'E' for Easy, 'M' for Medium or 'H' for hard: ")
        if level == 'E':
            grid = Board(1)
            grid.fillValues()
        elif level == 'M':
            grid = Board(2)
            grid.fillValues()
        else:
            grid = Board(3)
            grid.fillValues()
        startTime = time.time()
        grid.displayBoard()

        run = True
        while run:
            if grid.emptyCells == 0:
                endTime = formatTime(time.time() - startTime)
                print("You finished in " + endTime)
                run = False

            choice = input("Enter 'A' to add a value, 'R' to remove a value, 'S' to solve, 'O' to display the original board or 'Q' to quit: ")
            while choice != 'A' and choice != 'R' and choice != 'S' and choice != 'Q' and choice != 'O':
                choice = input("Enter 'A' to add a value, 'R' to remove a value, 'S' to solve, 'O' to display the original board or 'Q' to quit: ")
            if choice == 'Q':
                quitTime = formatTime(time.time() - startTime)
                print("You gave up in " + quitTime)
                run = False
            elif choice == 'A':
                add = input("Enter the row number, column number and value you wish to add separated by spaces: ").split()
                while not grid.addValue(int(add[0]), int(add[1]), int(add[2])):
                    print("Failure, your row, column and value combination is invalid.")
                    add = input(
                        "Enter the row number, column number and value you wish to add separated by spaces: ").split()
                print("Success")
                grid.displayBoard()
            elif choice == 'R':
                remove = input("Enter the row number and column number of the value you wish to remove: ").split()
                while not grid.removeValue(int(remove[0]), int(remove[1])):
                    print("Failure, your row and column combination is invalid.")
                    remove = input("Enter the row number and column number of the value you wish to remove: ").split()
                print("Success")
                grid.displayBoard()
            elif choice == 'S':
                grid.resetBoard()
                grid.solveBackTracking()
                grid.displayBoard()
                quitTime = formatTime(time.time() - startTime)
                print("You gave up in " + quitTime)
                return
            elif choice == 'O':
                grid.displayOriginalBoard()





main()


