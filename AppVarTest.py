from ggame import App, Sprite, CircleAsset, LineStyle, Color, Frame, ImageAsset

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

class Player(Sprite):
    
    asset = CircleAsset(25, thinline, black)
    
    def __init__(self, position):
        super().__init__(Player.asset, position)
        
    def step(self):
        self.rotation = self.app.playerRot

class SpaceWar(App):
    
    def __init__(self):
        super().__init__()
        self.playerRot = 0
        self.rotSpd = 0.1
        Player((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        self.step()
        
    def rotateRight(self, event):
        self.playerRot -= self.rotSpd
    
    def rotateLeft(self, event):
        self.playerRot += self.rotSpd
        
    def step(self):
        for x in self.getSpritesbyClass(Player):
            x.step()

app = SpaceWar()
app.run()