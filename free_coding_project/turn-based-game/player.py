import random

from entity import Entity


class Player(Entity):

    def __init__(self, name):
        super().__init__(10, 1, 1, 1)
        self.BADGE_POWER_STAT = 3
        self.ENDURANCE_POINTS_STAT = 5
        self.endurance_points = 5

        self.attack_list = {"Strike": [2, 1], "Combo": [1, 2]}
        self.special_list = {"Heal": 2, "Charge": 1}

        self.items = ["Cougar Tail"]
        self.current_experience = 0

        self.obtained_badges = {}
        self.equipped_badges = []

        self.name = name

    def damage(self, base_attack_power, modifier=1, crit_chance=.1, crit_power=1.5):
        crit = 1
        if random.random() <= crit_chance:
            crit = crit_power

        badge_power = 0
        if "Hail Mary" in self.equipped_badges and self.health <= self.max_health * .2:
            badge_power += 1


        return round((self.attack + badge_power)* base_attack_power * modifier * crit)

    def special(self, flower_power):
        if "College Student Budget" in self.equipped_badges:
            discount = 1
        self.endurance_points -= (flower_power - 1)

    def die(self):
        print("You died")

    def level_up(self):
        self.current_experience -= 100
        self.STAT_HEALTH += 5
        self.health = self.STAT_HEALTH
        self.STAT_ATTACK += 5
        self.load_badges()
        print("You leveled up and your health and attack went up!")

    def equip_badges(self, badge):
        if badge not in self.obtained_badges:
            return "You don't have this badge"

        if self.equipped_badges.count(badge) >= self.obtained_badges[badge][1]:
            return "You already have this badge equipped"

        if self.get_usable_bp() < self.obtained_badges[badge][0]:
            return "You don't have enough bp to equip this badge"

        self.equipped_badges.append(badge)
        self.load_badges()
        return f"You equipped {badge}!"

    def unequip_badges(self, badge):
        if badge not in self.equipped_badges:
            return f"{badge} not found!"
        self.equipped_badges.remove(badge)
        self.load_badges()
        return f"You unequipped {badge}!"

    def load_badges(self):
        self.attack = self.STAT_ATTACK
        self.max_health = self.STAT_HEALTH

        if "Attack Plus" in self.equipped_badges:
            self.attack += 1
        if "Health Plus" in self.equipped_badges:
            self.max_health += 5


    def display_obtained_badges(self):
        if not self.obtained_badges:
            return "no badges"

        badges = ""
        for key, value in self.obtained_badges.items():
            badges += f"{value[1]} {key}, cost {value[0]} bp; "

        return badges

    def display_equipped_badges(self):
        if not self.equipped_badges:
            return "no badges"

        badges = ""
        badges += self.equipped_badges[0]

        #print(self.equipped_badges)

        if len(self.equipped_badges) == 2:
            badges += f" and {self.equipped_badges[1]}"
        elif len(self.equipped_badges) > 2:
            for i in range(len(self.equipped_badges) - 1):
                badges += f", {self.equipped_badges[i]}"
            badges += f", and {self.equipped_badges[-1]}"

        return badges

    def get_usable_bp(self):
        bp = self.BADGE_POWER_STAT

        for badge in self.equipped_badges:
            bp -= self.obtained_badges[badge][0]

        return bp

    def hurt(self, attack_power):
        damage = attack_power - self.defense
        self.health -= damage
        if self.health <= 0:
            if "The Holy War" in self.equipped_badges:
                if random.random() > .25:
                    print("COSMO HELD ON WITH 1 HP!!")
                    self.health = 1
                    return damage
                print("so close...")
            self.health = 0
            self.is_dead = True
        return damage