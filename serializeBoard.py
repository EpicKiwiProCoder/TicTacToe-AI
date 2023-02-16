from enum import Enum
import csv
from ticTacToe import Board, States, Move

def miniMax(isMaximizing):
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


# 19682 highest number inclusive
board = Board([[States.AI, States.AI, States.EMPTY],[States.AI, States.PLAYER,States.EMPTY],[States.AI, States.PLAYER,States.EMPTY]])

# print(board.getSums())
# board.deserialize(100)
# board.display()

outcomes = {}
for serialization in range(19683):
    # print("-----------------------")
    board.deserialize(serialization)
    # board.display()
    # print(board.serialize())
    if board.isFull() or not board.evaluate() == 0: # if its not already finished
        continue
    ai, player = board.getSums()
    if ai == player or ai + 1 == player:

    # board.display()
    # print(board.serialize())
        board.makeMove(getBestAiMove())
        outcomes[serialization] = board.serialize()

with open("shortened.csv", "w+") as outFile:
    for key in outcomes:
        outFile.write(f"{key},{outcomes[key]}\n")
# print(outcomes)
