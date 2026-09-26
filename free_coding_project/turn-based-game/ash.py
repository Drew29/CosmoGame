from enemy import Enemy

class Ash(Enemy):
    def __init__(self):
        super().__init__(100, 4, 1, 10, {"Close Combat": [5, 1], "Rage of the Gods": [2, 3]}, ["Monster"], 300)
        #self.items = items
        self.name = "Ash"