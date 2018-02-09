#IanNolon
#2/9/18
#name.py

from ggame import *
#screen is 1000 px wide and 600 px down

name = input('What\'s your name?')
yourColor = input('Enter an RGB code.')
yourColor2 = Color(yourColor,1)
yourOutline = LineStyle(1,yourColor2)

background = RectangleAsset(1000,600,yourOutline,yourColor2) #width, height, outline, fill
text = TextAsset(name, fill = black, style = 'bold 40pt Times') #text

Sprite(background)
Sprite(text,(450,250))
App().run()
