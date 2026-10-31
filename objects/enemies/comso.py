from objects.enemy import Enemy

class Cosmo(Enemy):
    def __init__(self):
        super().__init__(100, 4, 1, 10, {"Strike": [5, 1], "Combo": [2, 3]}, ["Monster"], 300)
        #self.items = items
        self.name = "Cosmo"