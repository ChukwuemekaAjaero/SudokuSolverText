import random
import copy

class Cell:
    def __init__(self, value = "", fixed = False, clicked = False):
        self.value = value
        self.fixed = fixed
        self.clicked = clicked

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

class Board:
    board = []
    originalBoard = []

    def __init__(self, diffifulty = 1):
        if diffifulty == 1:
            self.emptyCells = 20
        elif diffifulty == 2:
            self.emptyCells = 40
        else:
            self.emptyCells = 60

        for row in range(9):
            self.board.append([])
            for column in range(9):
                self.board[row].append(Cell('-', False))

    def emptyBoard(self):
        '''Board -> None
        This method sets all the values on the board to null'''
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j].value = '-'

    def resetBoard(self):
        '''Board -> None
        This method erases all the user inputs from the
        board'''
        self.board = self.originalBoard

    def displayBoard(self):
        '''Board -> None
        This method displays the contents of the board'''
        print("   ", end="")
        col = 0
        while col < len(self.board):
            if(col == 3 or col == 6):
                print('|', col, end = "  ")
            else:
                print(col, end="  ")
            col += 1
        print()
        row = 0
        while row < len(self.board):
            if(row == 3 or row == 6):
                print("---------------------------------")
            print(row, end="")
            col = 0
            while col < len(self.board[row]):
                if(col == 3 or col == 6):
                    print("  |", self.board[row][col], end="")
                else:
                    print(" ", self.board[row][col], end="")
                col += 1
            print()
            row += 1

    def displayOriginalBoard(self):
        '''Board -> None
        This method displays the contents of the board'''
        print("   ", end="")
        col = 0
        while col < len(self.originalBoard):
            if(col == 3 or col == 6):
                print('|', col, end = "  ")
            else:
                print(col, end="  ")
            col += 1
        print()
        row = 0
        while row < len(self.originalBoard):
            if(row == 3 or row == 6):
                print("---------------------------------")
            print(row, end="")
            col = 0
            while col < len(self.originalBoard[row]):
                if(col == 3 or col == 6):
                    print("  |", self.originalBoard[row][col], end="")
                else:
                    print(" ", self.originalBoard[row][col], end="")
                col += 1
            print()
            row += 1

    def checkBoard(self):
        '''Board -> Boolean
        This method checks if all the values in the board meet
        the constraints set by the game of Sudoku'''
        if(self.isComplete()):
            print()

    def checkRow(self, row):
        '''Board, int -> Boolean
        This method checks if the all the values in a
        given row meet all the constraints set by the
        game of Sudoku'''

        c1, c2, c3, c4, c5, c6, c7, c8, c9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        for i in self.board[row]:
            if i.value == 1: c1 += 1
            if i.value == 2: c2 += 1
            if i.value == 3: c3 += 1
            if i.value == 4: c4 += 1
            if i.value == 5: c5 += 1
            if i.value == 6: c6 += 1
            if i.value == 7: c7 += 1
            if i.value == 8: c8 += 1
            if i.value == 9: c9 += 1

        return c1 < 2 and c2 < 2 and c3 < 2 and c4 < 2 and c5 < 2 and c6 < 2 and c7 < 2 and c8 < 2 and c9 < 2

    def checkColumn(self, column):
        '''Board, int -> Boolean
        This method checks if the all the values in a
        given column meet all the constraints set by the
        game of Sudoku'''

        c1, c2, c3, c4, c5, c6, c7, c8, c9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        for i in range(len(self.board)):
            if self.board[i][column].value == 1: c1 +=1
            elif self.board[i][column].value == 2: c2 += 1
            elif self.board[i][column].value == 3: c3 += 1
            elif self.board[i][column].value == 4: c4 += 1
            elif self.board[i][column].value == 5: c5 += 1
            elif self.board[i][column].value == 6: c6 += 1
            elif self.board[i][column].value == 7: c7 += 1
            elif self.board[i][column].value == 8: c8 += 1
            elif self.board[i][column].value == 9: c9 += 1

        return c1 < 2 and c2 < 2 and c3 < 2 and c4 < 2 and c5 < 2 and c6 < 2 and c7 < 2 and c8 < 2 and c9 < 2

    def checkSquare(self, row, column):
        '''Board, int, int -> Boolean
        This method checks if the all the values in a
        values square meet all the constraints set by
        the game of Sudoku'''

        c1, c2, c3, c4, c5, c6, c7, c8, c9, rowStart, rowStop, colStart, colStop = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        if row <= 2:
            if column <= 2:
                rowStop, colStop = 2, 2
            elif column <= 5:
                rowStop, colStart, colStop = 2, 3, 5
            else:
                rowStop, colStart, colStop = 2, 6, 8
        elif row <= 5:
            if column <= 2:
                rowStart, rowStop, colStop = 3, 5, 2
            elif column <= 5:
                rowStart, rowStop, colStart, colStop = 3, 5, 3, 5
            else:
                rowStart, rowStop, colStart, colStop = 3, 5, 6, 8
        else:
            if column <= 2:
                rowStart, rowStop, colStop = 6, 8, 2
            elif column <= 5:
                rowStart, rowStop, colStart, colStop = 6, 8, 3, 5
            else:
                rowStart, rowStop, colStart, colStop= 6, 8, 6, 8

        for i in range(rowStart, rowStop+1):
            for j in range(colStart, colStop+1):
                if self.board[i][j].value == 1: c1 += 1
                elif self.board[i][j].value == 2: c2 += 1
                elif self.board[i][j].value == 3: c3 += 1
                elif self.board[i][j].value == 4: c4 += 1
                elif self.board[i][j].value == 5: c5 += 1
                elif self.board[i][j].value == 6: c6 += 1
                elif self.board[i][j].value == 7: c7 += 1
                elif self.board[i][j].value == 8: c8 += 1
                elif self.board[i][j].value == 9: c9 += 1

        return c1 < 2 and c2 < 2 and c3 < 2 and c4 < 2 and c5 < 2 and c6 < 2 and c7 < 2 and c8 < 2 and c9 < 2

    def findEmptyLocation(self, locationList):
        '''Board, list -> Boolean
        This function finds the next empty cell on the
        board. Once found, it places the index of that
        cell in the locationList and returns True.
        Otherwise it returns False'''

        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.board[row][column].value == '-':
                    locationList[0] = row
                    locationList[1] = column
                    return True
        return False

    def usedInRow(self, row, val):
        '''Board, int, int -> Boolean
        This method scans a specified row on the board
        and returns True if the specified value is in
        that row and False otherwise'''

        for column in range(len(self.board)):
            if(self.board[row][column].value == val):
                return True
        return False

    def usedInColumn(self, column, val):
        '''Board, int, int -> Boolean
        This method scans a specified column on the board
        and returns True if the specified value is in
        that row and False otherwise'''

        for row in range(len(self.board)):
            if(self.board[row][column].value == val):
                return True
        return False

    def usedInSquare(self, row, column, val):
        '''Board, int, int, int -> Boolean
        This method scans a specified square on the board
        and returns True if the specified value is in
        that square and False otherwise'''

        for i in range(3):
            for j in range(3):
                if(self.board[row+i][column+j].value == val):
                    return True
        return False

    def checkLocationSafe(self, row, column, val):
        '''Board, int, int, int -> Boolean
        This method checks if it is safe to insert
        the specified value at the given position'''
        a = not self.usedInRow(row, val)
        b = not self.usedInColumn(column, val)
        c = not self.usedInSquare(row - row%3, column - column%3, val) # mod3 is used to prevent indexOutOfBounds error

        return a and b and c

    def generateBoard(self, difficulty):
        '''Board, int -> None
        Precondition: difficulty is greater than or equal
        to 2

        Generated board isn't always valid. Keeping as a
        point of reference'''

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                dif = random.randint(1, difficulty)
                if (dif == 1):
                    self.board[i][j].value = random.randint(1,9)
                    while not (self.checkRow(i) and self.checkColumn(j) and self.checkSquare(i, j)):
                        self.board[i][j].value = random.randint(1, 9)
                    self.board[i][j].fixed = True

    def fillValues(self):
        self.fillDiagonal()
        self.fillRemaining(0, 3)
        self.removeDigits()
        self.originalBoard = copy.deepcopy(self.board)

    def fillDiagonal(self):
        for i in range(0,8,3):#Might need to change the step value
            self.fillSquare(i, i)

    def fillRemaining(self, i, j):
        N = len(self.board)
        if j >= N and i<N-1:
            i+=1
            j = 0

        if i>=N and j>=N:
            return True

        if i < 3:
            if j < 3:
                j = 3

        elif i < N-3:
            if j == ((int)(i/3))*3: #Play around with this do see if I can use // or just i
                j+=3

        else:
            if j == N - 3:
                i+=1
                j=0
                if i>=N:
                    return True

        for k in range(1, N+1):
            if self.checkLocationSafe(i, j, k):
                self.board[i][j].value = k
                self.board[i][j].fixed = True
                if self.fillRemaining(i, j+1):
                    return True
                self.board[i][j].value = '-'
                self.board[i][j].fixed = False

        return False

    def removeDigits(self):
        count = self.emptyCells
        while count != 0:
            row = random.randint(0,8)
            column = random.randint(0,8)

            if not self.board[row][column].value == '-':
                count-=1
                self.board[row][column].value = '-'
                self.board[row][column].fixed = False

    def fillSquare(self, row, column):
        for i in range(3):
            for j in range(3):
                val = random.randint(1,9)
                while self.usedInSquare(row, column, val):
                    val = random.randint(1, 9)
                self.board[row+i][column+j].value = val
                self.board[row + i][column + j].fixed = True

    def addValue(self, row, column, value):
        '''Board, int, int, int -> Boolean'''

        if row > 8 or row < 0 or column > 8 or column < 0 or value > 8 or value < 0:
            return False

        if self.board[row][column].fixed == False:
            if(self.checkLocationSafe(row, column, value)):
                self.board[row][column].value = value
                self.emptyCells-=1
                return True
            else:
                return False
        return False


    def removeValue(self, row, column):
        '''Board, int, int -> Boolean'''
        if row > 8 or row < 0 or column > 8 or column < 0:
            return False

        if self.board[row][column].fixed == False:
            self.board[row][column].value = '-'
            self.emptyCells+=1
            return True
        else:
            return False


    def isComplete(self):
        '''Board -> Boolean'''

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if (self.board[i][j].value == '-'):
                    return False
        return True

    def solveBackTracking(self):
        '''Board -> Boolean'''

        locationList = [0,0]

        if not self.findEmptyLocation(locationList):
            return True

        row = locationList[0]
        col = locationList[1]

        for val in range(1, 10):
            if(self.checkLocationSafe(row, col, val)):
                self.board[row][col].value = val
                if(self.solveBackTracking()):
                    return True
                self.board[row][col].value = '-'

        return False

    def solveStochasticSearch(self):
        '''Board -> None'''

    def solveConstraint(self):
        '''Board -> None'''

    def solveExactCover(self):
        '''Board -> None'''
