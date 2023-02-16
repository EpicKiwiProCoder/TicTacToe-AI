from enum import Enum
import csv
from ticTacToe import Board, States, Move, getBestAiMove, miniMax

# 19682 highest number inclusive
board = Board([[States.AI, States.AI, States.EMPTY],[States.AI, States.PLAYER,States.EMPTY],[States.AI, States.PLAYER,States.EMPTY]])

# print(board.getSums())
# board.deserialize(100)
# board.display()

outcomes = {}
for serialization in range(19683):
    board.deserialize(serialization)

    if board.isFull() or not board.evaluate() == 0: # if its not already finished
        continue
    ai, player = board.getSums()
    if ai == player or ai + 1 == player:
        board.makeMove(getBestAiMove(board))
        outcomes[serialization] = board.serialize()

with open("Output/shortened.csv", "w+") as outFile:
    for key in outcomes:
        outFile.write(f"{key},{outcomes[key]}\n")
# print(outcomes)
