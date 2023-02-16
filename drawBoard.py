from PIL import Image, ImageDraw

img = Image.new('RGB', (120,120), color='white')
draw = ImageDraw.Draw(img)

def drawPosition(xOff, yOff):
    draw.rectangle((xOff+4,yOff+20,xOff+55,yOff+21), fill='black')
    draw.rectangle((xOff+4,yOff+38,xOff+55,yOff+39), fill='black')
    draw.rectangle((xOff+20,yOff+4,xOff+21,yOff+55), fill='black')
    draw.rectangle((xOff+38,yOff+4,xOff+39,yOff+55), fill='black')
drawPosition(0,0)
drawPosition(0,60)
drawPosition(60,0)
drawPosition(60,60)

img.save("im.png")