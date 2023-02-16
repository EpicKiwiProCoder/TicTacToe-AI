from enum import Enum
import csv
from ticTacToe import Board, States, Move, getBestAiMove, miniMax
from drawBoard import *
# 19682 highest number inclusive
# board = Board([[States.AI, States.AI, States.EMPTY],[States.AI, States.PLAYER,States.EMPTY],[States.AI, States.PLAYER,States.EMPTY]])

# print(board.getSums())
# board.deserialize(100)
# board.display()

outcomes = {}
outList = []
counter = 0
for serialization in range(19683): # 683
    board = Board()
    board.deserialize(serialization)

    if board.isFull() or not board.evaluate() == 0: # if its not already finished
        continue
    ai, player = board.getSums()
    if ai == player or ai + 1 == player:
        xPos = counter % 80
        yPos = counter // 80
        bestMove = getBestAiMove(board, States.AI)
        board.makeMove(Move((bestMove.x, bestMove.y), States.TARGET))
        # outcomes[serialization] = board.serialize()
        drawPosition(xPos*60, yPos*60, board)
        counter += 1
print(counter)
saveImage()
# with open("Output/shortenedt.csv", "w+") as outFile:
#     for key in outcomes:
#         outFile.write(f"{key},{outcomes[key]}\n")
# print(outcomes)
