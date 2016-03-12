from ggame import App, Sprite, CircleAsset, Line, Color, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

black = Color(0)
thinline = Line(0, 1)

class Player(Sprite):
    
    asset = CircleAsset(10, black, thinline)
    
    def __init__(self, position):
        super().__init__(Player.asset, position)

class SpaceWar(App):
    
    def __init__(self):
        super().__init__()
        self.playerRot = 0
        Player((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

app = SpaceWar()
app.run()