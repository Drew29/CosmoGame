from objects.enemy import Enemy

class UtahMascot(Enemy):
    def __init__(self):
        super().__init__(20, 2, 0, 10, {"Thunderbolt": [3, 1]}, ["Monster"], 300)
        #self.items = items
        self.name = "Utah Mascot"