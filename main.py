from SudokuLibrary import *
import random

testBoard = Board()
#testBoard.displayBoard()

testBoard.fillValues()
testBoard.displayBoard()
print("\n*************************************\n")
testBoard.solveBackTracking()
testBoard.displayBoard()
print(testBoard.emptyCells)
