

class Symbol():

    def __init__(self, icon):
        self.icon = icon
        if icon in ["♥", "♦"]:
            self.color = "red"
        elif icon in ["♣", "♠"]:
            self.color = "black"



class Card(Symbol):
    
    def __init__(self, value: str):
        super().__init__()
        self.value = value