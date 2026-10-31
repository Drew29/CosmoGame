import random

from entity import Entity

class Enemy(Entity):
    def __init__(self, health, attack, defense, speed, attack_list, items, experience, name="Bob"):
        super().__init__(health, attack, defense, speed)
        self.attack_list = attack_list
        self.items = items
        self.BASE_EXPERIENCE = experience
        self.name = name

    def damage(self, crit_chance=.1, crit_power=1.5):
        crit = 1
        if random.random() <= crit_chance:
            crit = crit_power

        attack_name = next(iter(self.attack_list))

        return [round(self.attack * self.attack_list[attack_name][0] * crit), attack_name]

    def die(self):
       # player.current_experience += self.BASE_EXPERIENCE
        print("HAHAHAHAHA")