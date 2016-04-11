from ggame import App, Sprite, ImageAsset, Frame
from math import sin, cos, pi, sqrt
from random import randint

class Enemy(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.velocity = (0,0)
        self.magnitude = 0.5
        
    def step(self):
        if randint(0,300) == 0:
            self.rotation = randint(0,1000)/500*pi
            self.velocity[0] += -1*self.magnitude*sin(self.rotation)
            self.velocity[1] += -1*self.magnitude*cos(self.rotation)
            if sqrt(self.velocity[0]**2 + self.velocity[1]**2) >= 1:
                print('hello')
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        
class SpaceGame(App):

    def __init__(self):
        super().__init__()
        Enemy((500,300))
        
    def step(self):    
        for x in self.getSpritesbyClass(Enemy):
            x.step()
        
SpaceGame().run()
