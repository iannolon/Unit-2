#SwollenNolon
#2/2/18
#house.py

from ggame import *

red = Color(0xFF0000,1) #this is color red
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

houseBody = RectangleAsset(300,360,blackOutline,green) #width, height, outline, fill
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
greenEllipse = EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill
blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
redTriangle = PolygonAsset([(0,0),(120,180),(60,300)], blackOutline, red) #endpoints, outline, fill
text = TextAsset('Swollen Nolon', fill = black, style = 'bold 40pt Times') #text


Sprite(houseBody,(350,150))
#Sprite(redTriangle)
#Sprite(blueCircle,(50,50))
#Sprite(greenEllipse,(200,200))
#Sprite(blackLine)
#Sprite(text,(300,200))
App().run()
