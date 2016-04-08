from ggame import App, Sprite, ImageAsset, Frame, Color

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class StarBack(Sprite):
    
    asset = ImageAsset("images/starfield.jpg", Frame(0,0,SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    
    def __init__(self, position):
        super().__init__(StarBack.asset, position)
        self.scale = 2
        
class Test(App):
  StarBack((0,0))
  
Test.run()
