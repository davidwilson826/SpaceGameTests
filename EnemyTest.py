from ggame import App, Sprite, ImageAsset, Frame
from math import sin, cos, sqrt, pi
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_DIAG = sqrt(SCREEN_WIDTH**2+SCREEN_HEIGHT**2)

def velcalc (rotation, speed, velx, vely):
    velx = -1*speed*sin(rotation)
    vely = -1*speed*cos(rotation)

class StarBack(Sprite):
    
    asset = ImageAsset("images/starfield.jpg", Frame(0,0,SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    
    def __init__(self, position):
        super().__init__(StarBack.asset, position)
        self.scale = 2

class Enemy(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        self.speed = 1
        self.rotation = randint(0,1000)/500*pi
#        self.velx = self.speed*sin(self.rotation)
#        self.vely = self.speed*cos(self.rotation)
        self.velx = 0
        self.vely = 0
        velcalc(self.rotation, 5, self.velx, self.vely)
        self.fxcenter = self.fycenter = 0.5
        self.dist = 0
        self.frame = 0

    def changeDirec(self):
        self.rotation = randint(0,1000)/500*pi
#        self.velx = self.speed*sin(self.rotation)
#        self.vely = self.speed*cos(self.rotation)
        velcalc(self.rotation, 5, self.velx, self.vely)
        self.dist = 0
        if self.frame == 3:
            self.frame = 0
        else:
            self.frame += 1
        self.setImage(self.frame)
        
    def step(self):
        if self.x > SCREEN_WIDTH or self.x < 0 or self.y > SCREEN_HEIGHT or self.y < 0:
            self.rotation += pi
        elif self.dist > SCREEN_DIAG/5 and randint(0,20) == 0:
            self.changeDirec()
        self.x += self.velx
        self.y += self.vely
        self.dist += self.speed
        
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
