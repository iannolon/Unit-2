#IanNolon
#1/31/18
#coloredSquare.py

from ggame import *
from random import randint
red = Color(0xff0000,1)
redline = LineStyle(3,red)
blue = Color(0x0000ff,1)
blueline = LineStyle(3,blue)
green = Color(0x00cc00,1)
greenline = LineStyle(3,green)
yellow = Color(0xffff00,1)
yellowline = LineStyle(3,yellow)
rancol = randint(1,4)
if rancol == 1:
    rectangle = RectangleAsset(100,100,redline,red)
if rancol == 2:
    rectangle = RectangleAsset(100,100,blueline,blue)
if rancol == 3:
    rectangle = RectangleAsset(100,100,greenline,green)
if rancol == 4:
    rectangle = RectangleAsset(100,100,yellowline,yellow)

Sprite (rectangle)
myApp = App()
myApp.run()
