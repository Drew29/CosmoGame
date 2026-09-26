import os
import sys
import termios
import time

class Battle:

    def __init__(self, player, enemies, music_manager):
        self.enemies = enemies
        self.player = player
        self.battle_experience = 0

        self.player_attack_modifier = 1

        self.music_manager = music_manager

        self.console_text = [
            f"Your health is {self.player.health}. Your endurance points are {self.player.endurance_points}.", "",
            calculate_enemy_text(self), ""]



    def battle(self):
        while True:
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
            console_manager(self)
            a = input("What will you do? ")
            action = a.split(" ")
            self.console_text.append("What will you do? " + a)



            if not player_attack(self, action):
                continue

            self.console_text.append("")
            console_manager(self)

            if len(self.enemies) == 0:
                break

            for enemy in self.enemies:
                power = enemy.damage()[0]
                attack_name = enemy.damage()[1]
                damage = self.player.hurt(power)

                self.console_text.append(f"{enemy.name} uses {attack_name}! You lose {damage} hp!")
                console_manager(self)
                #print(f"{enemy.name} uses {attack_name}! You lose {damage} hp!")
                self.music_manager.sound_effect()
                time.sleep(1)

            # time.sleep(1)

            del self.console_text[4:]

            if self.player.is_dead:
                self.player.die()
                return 0

        return self.battle_experience

def player_attack(self, action):
    choice = verify_action(self, action)
    if not choice:
        return False

    if choice in self.player.attack_list:
        target = self.enemies[verify_target(self, action)]

        num_attacks = self.player.attack_list[choice][1]

        self.console_text.append("")

        while num_attacks > 0:
            power = self.player.damage(self.player.attack_list[choice][0], self.player_attack_modifier)
            damage = target.hurt(power)
            self.music_manager.sound_effect()

            self.console_text.append(f"{target.name} loses {damage} hp!")
            console_manager(self)

            num_attacks -= 1
            time.sleep(.4)

        time.sleep(1)

        self.player_attack_modifier = 1

        if target.is_dead:
            target.die()
            print(f"You gained {target.BASE_EXPERIENCE} experience!")
            self.battle_experience += target.BASE_EXPERIENCE
            self.enemies.remove(target)

    if choice in self.player.special_list:
        if choice == "Heal":
            self.player.special(self.player.special_list["Heal"])
            amount_healed = self.player.heal(self.player.STAT_HEALTH // 2)
            print(f"You healed {amount_healed} hp!")
        elif choice == "Charge":
            self.player.special(self.player.special_list["Charge"])
            self.player_attack_modifier += 1

    return True

def verify_action(self, action):
    if len(action) <= 0:
        print("Input something! Type 'help' for available actions")
        time.sleep(1)
        return ""

    choice = action[0]

    if choice == 'help':
        print(f"Available actions: {self.player.attack_list}, {self.player.special_list}")
        time.sleep(3)
        return ""

    if (not choice in self.player.attack_list) and (not choice in self.player.special_list):
        print("Invalid action")
        time.sleep(1)
        return ""

    return action[0]

def verify_target(self, action):
    if len(self.enemies) <= 1:
        return 0

    if len(action) == 1:
        t = input("Which enemy will you attack? ")
        while True:
            if not t.isdigit():
                t = input(f"Invalid target! Choose a number between 1 and {len(self.enemies)}!")
                continue
            t = int(t)
            if len(self.enemies) < t or t < 1:
                t = input(f"Invalid target! Choose a number between 1 and {len(self.enemies)}!")
                continue
            return int(t) - 1

    t = action[1]
    while True:
        if not t.isdigit():
            t = input(f"Invalid target! Choose a number between 1 and {len(self.enemies)}!")
            continue
        t = int(t)
        if len(self.enemies) < t or t < 1:
            t = input(f"Invalid target! Choose a number between 1 and {len(self.enemies)}!")
            continue
        return int(t) - 1
    #return int(t) - 1




def console_manager(self):
    os.system('clear -x')  # Clears macOS terminal

    self.console_text[0] = f"Your health is {self.player.health}. Your endurance points are {self.player.endurance_points}."

    self.console_text[2] = calculate_enemy_text(self)

    #print("")
    for line in self.console_text:
        print(line)

def calculate_enemy_text(self):
    enemy_line = ""
    if len(self.enemies) <= 0:
        return enemy_line

    for i in range(len(self.enemies) - 1):
        enemy = self.enemies[i]
        enemy_line += f"{enemy.name} has {enemy.health} hp, "
        # print(f"{enemy.name} has {enemy.health} hp", end=", ")
    enemy_line += f"{self.enemies[-1].name} has {self.enemies[-1].health} hp"
    return enemy_line