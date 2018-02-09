#SwollenNolon
#2/9/18
#yield.py

from ggame import *
#screen is 1000 px wide and 600 px down

red = Color(0xFF0000,1) #this is color red
#green = Color(0x00FF00,1)
#blue = Color(0x0000FF,1)
#black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
yellow = Color(0xFFFF00,1)

blackOutline = LineStyle(1,black)
redOutline = LineStyle(1,red)
yellowOutline = LineStyle(1,yellow)
whiteOutline = LineStyle(1,white)

#background = RectangleAsset(1000,600,yourOutline,yourColor2) #width, height, outline, fill
#redBar = RectangleAsset(420,110,redOutline,red) #width, height, outline, fill
#yellowBar = RectangleAsset(420,110,yellowOutline,yellow) #width, height, outline, fill
#blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
#greenEllipse = EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill
#blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
redTriangle = PolygonAsset([(380,380),(700,380),(550,650)], redOutline, red) #endpoints, outline, fill
whiteTriangle = PolygonAsset([(280,280),(500,280),(400,450)], whiteOutline, white) #endpoints, outline, fill
text = TextAsset('YIELD', fill = red, style = '35pt Times') #text
#door = RectangleAsset(70,130,blackOutline,black) #width, height, outline, fill
#window1 = RectangleAsset(60,60,blackOutline,white) #width, height, outline, fill
#window2 = RectangleAsset(60,60,blackOutline,white) #width, height, outline, fill


Sprite(redTriangle,(350,200))
Sprite(whiteTriangle,(400,240))
Sprite(text,(450,250))
App().run()
