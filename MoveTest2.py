from ggame import App, Sprite, ImageAsset, Frame
from math import sin, cos

class Player(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,85,125))
        
    def __init__(self, position):
        super().__init__(Player.asset, position)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        
    def rotateRight(self, event):
        self.rotation -= self.rotSpd
        
    def rotateLeft(self, event):
        self.rotation += self.rotSpd

class SpaceGame(App):
    
    def __init__(self):
        super().__init__()
        Player((100,100))

SpaceGame().run()
