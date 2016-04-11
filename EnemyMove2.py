from ggame import App, Sprite, ImageAsset, Frame
form math import sin, cos

class Enemy(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        self.fxcenter = self.fycenter = 0.5
        
class SpaceGame(App):

    def __init__(self):
        super().__init__()
        Enemy((500,300))
        
SpaceGame().run()
