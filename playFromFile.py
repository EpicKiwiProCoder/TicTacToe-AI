from enum import Enum
import random, time
from ticTacToe import Board, Move, States

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

moveDatabase = open("Output/allMoves.txt", "r").readlines()

isPlayersTurn = False
while checkWinState():
    if isPlayersTurn:
        board.display()
        playerTurn()
    else:
        aiTurn()
    isPlayersTurn = not isPlayersTurn