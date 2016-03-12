from ggame import App, Sprite, CircleAsset, LineStyle, Color, Frame, ImageAsset

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

class Player(Sprite):
    
    asset = CircleAsset(25, thinline, black)
    
    def __init__(self, position):
        super().__init__(Player.asset, position)

class SpaceWar(App):
    
    def __init__(self):
        super().__init__()
        self.playerRot = 0
        Player((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

app = SpaceWar()
app.run()