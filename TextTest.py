from ggame import Color, TextAsset, Sprite, App

white = Color(0xffffff, 1.0)

class WhiteText(TextAsset):
    
    def __init__(self, text):
        super().__init__(text)
        
class ToPrint(Sprite):
    
    asset = WhiteText('Hello')
    
    def __init__(self, position):
        super().__init__(ToPrint.asset, position)
        
class Print(App):
    
    def __init__(self):
        super().__init__()
        ToPrint((100,100))
        
Print().run()