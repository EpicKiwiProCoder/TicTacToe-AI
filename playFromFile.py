from enum import Enum
import random, time

class States(Enum):
    EMPTY = 0
    AI = 1
    PLAYER = 2

class Move:
    x, y = None, None
    state = None
    def __init__(self, location, state):
        self.x = location[0]
        self.y = location[1]
        self.state = state

amountOfConsiderations = 0

class Board:
    currentBoard = []
    def __init__(self, initialBoard = [[States.EMPTY]*3]+[[States.EMPTY]*3]+[[States.EMPTY]*3]) -> None:
        self.currentBoard = initialBoard

    def isMoveValid(self, move) -> bool:
        return self.currentBoard[move.x][move.y] == States.EMPTY

    def isFull(self) -> bool:
        for row in self.currentBoard:
            for square in row:
                if square == States.EMPTY:
                    return False
        return True

    def serialize(self):
        multiplication = 1
        output = 0
        for row in self.currentBoard:
            for square in row:
                squareValue = 1 if square == States.AI else 0
                squareValue = 2 if square == States.PLAYER else squareValue
                output += squareValue * multiplication
                multiplication *= 3
        return output
    
    def deserialize(self, serialization):
        division = 1
        for x in range(3):
            for y in range(3):
                squareValue = serialization / division % 3
                
                if squareValue == 0:
                    self.currentBoard[x][y] = States.EMPTY
                if squareValue == 1:
                    self.currentBoard[x][y] = States.AI
                if squareValue == 2:
                    self.currentBoard[x][y] = States.PLAYER

                serialization -= squareValue * division
                division *= 3

    def getMoves(self, state) -> list:
        allMoves = []
        for x, col in enumerate(self.currentBoard):
            for y, square in enumerate(col):
                if square == States.EMPTY:
                    allMoves.append(Move((x, y), state))
        return allMoves
    
    def makeMove(self, move) -> None:
        self.currentBoard[move.x][move.y] = move.state
    
    def unmakeMove(self, move) -> None:
        self.currentBoard[move.x][move.y] = States.EMPTY

    def evaluate(self) -> int:
        b = self.currentBoard
        for row in range(3) :    
            if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :       
                if (b[row][0] == States.PLAYER) :
                    return -1
                elif (b[row][0] == States.AI) :
                    return 1
        for col in range(3) :
            if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
                if (b[0][col] == States.PLAYER) :
                    return -1
                elif (b[0][col] == States.AI) :
                    return 1
        if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
            if (b[0][0] == States.PLAYER) :
                return -1
            elif (b[0][0] == States.AI) :
                return 1
        if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
            if (b[0][2] == States.PLAYER) :
                return -1
            elif (b[0][2] == States.AI) :
                return 1
        return 0

    def display(self) -> None:
        for row in range(3):
            for column in range(3):
                position = self.currentBoard[column][row]
                if position == States.PLAYER:
                    print("  X", end="")
                elif position == States.AI:
                    print("  O", end="")
                elif position == States.EMPTY:
                    print("  .", end="")
            print("\n")

def aiTurn():
    targetBoard = moveDatabase[board.serialize()]
    board.deserialize(int(targetBoard))

def playerTurn():
    inputLocation = int(input("1-9 >"))-1
    suggestedMove = Move((inputLocation%3,inputLocation//3), States.PLAYER)
    if board.isMoveValid(suggestedMove):
        board.makeMove(suggestedMove)
    else:
        print("Invalid Move")
        playerTurn()

def checkWinState():
    boardEvaluation = board.evaluate()
    if boardEvaluation > 0:
        board.display()
        print("\nThe AI has won. Too bad, so sad, stay mad.\n")
        return False
    elif boardEvaluation < 0:
        board.display()
        print("\nYou have won. (this shouldn't be possible if the Ai is working correctly)\n")
        return False
    elif board.isFull():
        board.display()
        print("\nIt's a draw.\n")
        return False
    return True
    
board = Board() # [[States.PLAYER, States.EMPTY, States.PLAYER],[States.AI,States.EMPTY,States.EMPTY],[States.AI,States.EMPTY,States.EMPTY]]

moveDatabase = open("allMoves.txt", "r").readlines()

isPlayersTurn = True
while checkWinState():
    if isPlayersTurn:
        board.display()
        playerTurn()
    else:
        aiTurn()
    isPlayersTurn = not isPlayersTurn