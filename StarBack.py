from ggame import App, Sprite, ImageAsset, Frame, Color

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

class StarBack(Sprite):
    
    asset = ImageAsset("images/starfield.jpg", Frame(0,0,512,512*(SCREEN_HEIGHT/SCREEN_WIDTH)))
    
    def __init__(self, position):
        super().__init__(StarBack.asset, position)
        
class Test(App):
  StarBack((0,0))

Test().run()