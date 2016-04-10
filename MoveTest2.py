from ggame import App, Sprite, ImageAsset, Frame
from math import sin, cos

class Player(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,85,125))
        
    def __init__(self, position):
        super().__init__(Player.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.velocity = (0,0)
        self.rotSpd = 0.1
        self.magnitude = 0.25
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrust)
        
    def rotateRight(self, event):
        self.rotation -= self.rotSpd
        
    def rotateLeft(self, event):
        self.rotation += self.rotSpd
        
    def thrust(self, event):
        self.velocity[0] += -1*self.magnitude*sin(self.rotation)
        self.velocity[1] += -1*self.magnitude*cos(self.rotation)
        print(self.velocity)

    def step(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

class SpaceGame(App):
    
    def __init__(self):
        super().__init__()
        Player((500,300))
        
    def step(self):
        for x in self.getSpritesbyClass(Player):
            x.step()

SpaceGame().run()
