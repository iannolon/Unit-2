#SwollenNolon
#2/9/18
#germany.py

from ggame import *

red = Color(0xFF0000,1) #this is color red
#green = Color(0x00FF00,1)
#blue = Color(0x0000FF,1)
black = Color(0x000000,1)
#white = Color(0xFFFFFF,1)
yellow = Color(0xFFFF00,1)

blackOutline = LineStyle(1,black)
redOutline = LineStyle(1,red)
yellowOutline = LineStyle(1,yellow)

blackBar = RectangleAsset(420,110,blackOutline,black) #width, height, outline, fill
redBar = RectangleAsset(420,110,redOutline,red) #width, height, outline, fill
yellowBar = RectangleAsset(420,110,yellowOutline,yellow) #width, height, outline, fill
#blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
#greenEllipse = EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill
#blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
#roof = PolygonAsset([(400,400),(700,400),(550,250)], blackOutline, red) #endpoints, outline, fill
#text = TextAsset('Swollen Nolon', fill = black, style = 'bold 40pt Times') #text
#door = RectangleAsset(70,130,blackOutline,black) #width, height, outline, fill
#window1 = RectangleAsset(60,60,blackOutline,white) #width, height, outline, fill
#window2 = RectangleAsset(60,60,blackOutline,white) #width, height, outline, fill

Sprite(blackBar,(0,0))
Sprite(redBar,(0,110))
Sprite(yellowBar,(0,220))
App().run()
