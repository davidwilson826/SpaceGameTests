from ggame import App, Sprite, ImageAsset, Frame
from math import sin, cos, pi
from random import randint

class Enemy(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.velocity = (0,0)
        self.magnitude = 0.25
        
    def step(self):
        if randint(0,100) == 0:
            self.rotation = randint(0,1000)/500*pi
            self.velocity = (sum(x) for x in zip(self.velocity, (-1*self.magnitude*sin(self.rotation),
            -1*self.magnitude*cos(self.rotation))))
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        
class SpaceGame(App):

    def __init__(self):
        super().__init__()
        Enemy((500,300))
        
    for x in self.getSpritesbyClass(Enemy):
        x.step()
        
SpaceGame().run()
