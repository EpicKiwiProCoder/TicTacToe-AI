from PIL import Image, ImageDraw
from ticTacToe import Board, States

img = Image.new('RGB', (4800,3420), color='white')
draw = ImageDraw.Draw(img)

red = (255,50,50)
green = (50,255,50)
blue = (50,50,255)
white = (255,255,255)
black = (50,50,50)

def drawPosition(xOff, yOff, board):
    draw.rectangle((xOff+4,yOff+20,xOff+55,yOff+21), fill=black)
    draw.rectangle((xOff+4,yOff+38,xOff+55,yOff+39), fill=black)
    draw.rectangle((xOff+20,yOff+4,xOff+21,yOff+55), fill=black)
    draw.rectangle((xOff+38,yOff+4,xOff+39,yOff+55), fill=black)

    for x, row in enumerate(board.currentBoard):
        for y, square in enumerate(row):
            if square == States.EMPTY:
                fillColor = white
            if square == States.AI:
                fillColor = blue
            if square == States.PLAYER:
                fillColor = red
            if square == States.TARGET:
                fillColor = green
            draw.ellipse((xOff+6+(18*x), yOff+6+(18*y), xOff+17+(18*x), yOff+17+(18*y)), fill=fillColor)

def saveImage():
    img.save("Output/image.png")