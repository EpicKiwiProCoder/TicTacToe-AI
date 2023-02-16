from enum import Enum
import random

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

counter = 0

def miniMax(isMaximizing):
    counter += 1
    evaluation = board.evaluate()
    if evaluation == 1:
        return 1
    if evaluation == -1:
        return -1
    if board.isFull():
        return 0

    if isMaximizing:
        bestEvaluation = -100

        for possibleMove in board.getMoves(States.AI):
            board.makeMove(possibleMove)
            bestResponse = miniMax(not isMaximizing)
            bestEvaluation = max(bestResponse, bestEvaluation)
            board.unmakeMove(possibleMove)
    
    else:
        bestEvaluation = 100

        for possibleMove in board.getMoves(States.PLAYER):
            board.makeMove(possibleMove)
            bestResponse = miniMax(not isMaximizing)
            bestEvaluation = min(bestResponse, bestEvaluation)
            board.unmakeMove(possibleMove)

    return bestEvaluation

def getBestAiMove():
    bestScore = -100
    bestMove = None
    for possibleMove in board.getMoves(States.AI):
        board.makeMove(possibleMove)
        outcome = miniMax(False)
        if outcome > bestScore:
            bestMove = possibleMove
            bestScore = outcome
        board.unmakeMove(possibleMove)
    return bestMove

board = Board() # [[States.PLAYER, States.EMPTY, States.PLAYER],[States.AI,States.EMPTY,States.EMPTY],[States.AI,States.EMPTY,States.EMPTY]]
while True:
    board.makeMove(getBestAiMove())
    board.display()
    inputLocation = int(input(">"))-1
    suggestedMove = Move((inputLocation%3,inputLocation//3), States.PLAYER)
    if board.isMoveValid(suggestedMove):
        board.makeMove(suggestedMove)
        print(counter)
        board.display()
    else:
        print("Invalid Move")