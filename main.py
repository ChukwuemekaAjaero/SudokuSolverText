from SudokuLibrary import *
import time

def formatTime(secs):
    hours = int(secs//3600)
    minutes = int((secs%3600)//60)
    seconds = int(((secs%3600)%60))

    return str(hours) + " hours, " + str(minutes) + " and " + str(seconds) + " seconds."

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
            choice = input("Enter 'A' to add a value, 'R' to remove a value, 'S' to solve or 'Q' to quit: ")
            while choice != 'A' and choice != 'R' and choice != 'S' and choice != 'Q':
                choice = input("Enter 'A' to add a value, 'R' to remove a value, 'S' to solve or 'Q' to quit: ")
            if choice == 'Q':
                quitTime = formatTime(time.time() - startTime)
                print("You gave up in " + quitTime)
                break
            elif choice == 'A':
                add = input("Enter the row number, column number and value you wish to add separated by spaces: ").split()





main()
#print("\n*************************************\n")
#testBoard.solveBackTracking()
#testBoard.displayBoard()

