from ggame import App, Sprite, LineStyle, Color, PolygonAsset

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

class Thing(Sprite):
    
    asset = PolygonAsset([(0,100), (25,0) (50,100)], thinline, black)
    
app = SpaceWar()
app.run()
