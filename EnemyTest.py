from ggame import App, Sprite, ImageAsset, Frame
from math import sin, cos, sqrt, pi
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_DIAG = sqrt(SCREEN_WIDTH**2+SCREEN_HEIGHT**2)

class StarBack(Sprite):
    
    asset = ImageAsset("images/starfield.jpg", Frame(0,0,SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    
    def __init__(self, position):
        super().__init__(StarBack.asset, position)
        self.scale = 2

class Enemy(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125))
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
#        self.changeDirec
#        self.fxcenter = self.fycenter = 0.5
        self.velx = 5
        self.vely = 5
        
#    def changeDirec(self):
#        self.rotation = randint(0,1000)/500*pi
#        self.velx = 5#/sin(self.rotation)
#        self.vely = 5#/cos(self.rotation)
#        self.dist = 0
        
    def step(self):
#        if self.x > SCREEN_WIDTH or self.x < 0 or self.y > SCREEN_HEIGHT or self.y < 0:
#            self.changeDirec
#        elif self.dist > SCREEN_DIAG/5 and randint(0,20) == 0:
#            self.changeDirec
        self.x += self.velx
        self.y += self.vely
#        self.dist += 5
        
class SpaceGame(App):
        
    def __init__(self):
        super().__init__()
        StarBack((0,0))
        Enemy((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        self.step()
        
    def step(self):
        for x in self.getSpritesbyClass(Enemy):
            x.step()
        
myapp = SpaceGame()
myapp.run()