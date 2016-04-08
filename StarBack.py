from ggame import App, Sprite, ImageAsset, Frame, Color, CircleAsset, LineStyle

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

if SCREEN_WIDTH >= SCREEN_HEIGHT:
    LARGER_SIDE = SCREEN_WIDTH
    SMALLER_SIDE = SCREEN_HEIGHT
elif SCREEN_HEIGHT > SCREEN_WIDTH:
    LARGER_SIDE = SCREEN_HEIGHT
    SMALLER_SIDE = SCREEN_WIDTH

white = Color(0xffffff, 1.0)

line = LineStyle(1.0, white)

class StarBack(Sprite):
    
    asset = ImageAsset("images/starfield.jpg", Frame(0,0,512*(SMALLER_SIDE/LARGER_SIDE),512))
    
    def __init__(self, position):
        super().__init__(StarBack.asset, position)
        self.scale = LARGER_SIDE/512
        
class Test(App):
  StarBack((0,0))
  Sprite(CircleAsset(50, line, white), (SCREEN_WIDTH, SCREEN_HEIGHT))

Test().run()
