from ggame import App, Sprite, LineStyle, Color, PolygonAsset

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

class Thing(Sprite):
    
    asset = PolygonAsset([(0,100), (25,0), (50,100)], thinline, black)
    
    def __init__(self, position):
        super().__init__(Thing.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.rotSpd = 0.1
        ThingMove.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        ThingMove.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        
    def rotateRight(self, event):
        self.rotation -= self.rotSpd
        
    def rotateLeft(self, event):
        self.rotation += self.rotSpd
    
class ThingMove(App):
    
    def __init__(self):
        super().__init__()
        Thing((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

app = ThingMove()
app.run()
