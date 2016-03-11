class Enemy(SpaceShip):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125))
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        self.changeDirec
        
    def changeDirec(self):
        self.rotation = randint(0,1000)/500*pi
        self.velx = 5/sin(self.rotation)
        self.vely = 5/cos(self.rotation)
        self.dist = 0
        
    def step(self):
        if self.x > SCREEN_WIDTH or self.x < 0 or self.y > SCREEN_HEIGHT or self.y < 0:
            self.changeDirec
        elif self.dist > SCREEN_DIAG/5 and randint(0,20) == 0:
            self.changeDirec
        self.x += self.velx
        self.y += self.vely
        self.dist += 5
