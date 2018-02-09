#SwollenNolon
#2/9/18
#yield.py

from ggame import *
#screen is 1000 px wide and 600 px down

red = Color(0xFF0000,1) #this is color red
white = Color(0xFFFFFF,1)
yellow = Color(0xFFFF00,1)

redOutline = LineStyle(1,red)
yellowOutline = LineStyle(1,yellow)
whiteOutline = LineStyle(1,white)

redTriangle = PolygonAsset([(380,380),(700,380),(550,650)], redOutline, red) #endpoints, outline, fill
whiteTriangle = PolygonAsset([(280,280),(500,280),(400,450)], whiteOutline, white) #endpoints, outline, fill
text = TextAsset('YIELD', fill = red, style = '35pt Times') #text

Sprite(redTriangle,(350,200))
Sprite(whiteTriangle,(400,240))
Sprite(text,(450,250))
App().run()
