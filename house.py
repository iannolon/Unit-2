#SwollenNolon
#2/2/18
#house.py

from ggame import *

red = Color(0xFF0000,1) #this is color red
green = Color(0x00FF00,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

blackOutline = LineStyle(1,black)

houseBody = RectangleAsset(300,260,blackOutline,green) #width, height, outline, fill
roof = PolygonAsset([(400,400),(700,400),(550,250)], blackOutline, red) #endpoints, outline, fill
door = RectangleAsset(70,130,blackOutline,black) #width, height, outline, fill
window1 = RectangleAsset(60,60,blackOutline,white) #width, height, outline, fill
window2 = RectangleAsset(60,60,blackOutline,white) #width, height, outline, fill

Sprite(houseBody,(350,220))
Sprite(roof,(350,70))
Sprite(door,(450,350))
Sprite(window1,(380,260))
Sprite(window2,(530,260))
App().run()
