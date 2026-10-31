from objects.enemy import Enemy

class UtahFan(Enemy):
    def __init__(self):
        super().__init__(5, 1, 0, 5, {"Punch": [2, 1]}, ["Monster"], 50)
        #self.items = items
        self.name = "Utah Fan"