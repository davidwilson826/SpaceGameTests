from ggame import App, Sprite, LineStyle, Color, PolygonAsset, CircleAsset, RectangleAsset

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

class Thing(Sprite):
    
    #asset = PolygonAsset([(0,100), (25,0), (50,100)], thinline, black)
    asset = CircleAsset(25, thinline, black)
    #asset = RectangleAsset(50, 20, thinline, black)
    
    def __init__(self, position):
        super().__init__(Thing.asset, position)
        self.rotSpd = 0.1
        self.dist = 0
        self.gomove = 0
#        self.fxcenter = 0.5
#        self.fycenter = 0.5
        ThingMove.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        ThingMove.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        ThingMove.listenKeyEvent("keydown", "space", self.go)
        
    def rotateRight(self, event):
        self.rotation -= self.rotSpd
        
    def rotateLeft(self, event):
        self.rotation += self.rotSpd
        
    def go(self, event):
        self.gomove = 1
        
    def step(self):
        if self.dist < 50 and self.gomove == 1:
            self.x += 5
            self.y += 5
            self.dist += 5
        else:
            self.gomove = 0
            self.dist = 0
    
class ThingMove(App):
    
    def __init__(self):
        super().__init__()
        Thing((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.step()
        
    def step(self):
        for x in self.getSpritesbyClass(Thing):
            x.step()

app = ThingMove()
app.run()
