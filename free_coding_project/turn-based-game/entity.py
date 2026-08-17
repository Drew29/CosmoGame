class Entity:
    def __init__(self, health, attack, defense, speed):
        self.STAT_HEALTH = health
        self.STAT_ATTACK = attack
        self.STAT_DEFENSE = defense
        self.STAT_SPEED = speed

        self.health = health
        self.max_health = self.STAT_HEALTH
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.status = None

        self.is_dead = False

    def hurt(self, attack_power):
        damage = attack_power - self.defense
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_dead = True
        return damage

    def die(self):
        print("This isn't supposed to happen!")

    def heal(self, amount):
        if self.health <= self.STAT_HEALTH - amount:
            self.health += amount
            return amount
        else:
            health_healed = self.STAT_HEALTH - self.health
            self.health = self.STAT_HEALTH
            return health_healed