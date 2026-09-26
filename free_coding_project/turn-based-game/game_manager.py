import os
import time

from battle import Battle
from utah_fan import UtahFan
from pikachu import Pikachu
from ash import Ash
from player import Player

def slow_print(text, delay=.005, new_line=True):
    for i in range(len(text)):
        print(text[i], end="",flush=True)
        time.sleep(delay)
    if new_line:
        print("")

class GameManager:


    def __init__(self, name):
        self.player = Player(name)

        # key -> badge name ... value = ["description", badge cost]
        self.badges = {
            "True Blue": ["If Cosmo's health is below 20%, his attack power increases by 1", 1],
            "Hail Mary": ["If Cosmo's health is below 10%, his attack power increases by 2", 1],
            "The Holy War": ["If Cosmo is going to be knocked out, there is a 25% chance he remains with 1 hp", 2],
            "Parking Enforcement": ["After 5 turns in a battle, Cosmo's attack power increases by 1", 1],
            "The Honor Code": ["Gain an extra turn in battle", 5],
            #"Eagle Eye": ["Increases accuracy by "]
            "College Student Budget": ["Reduces the cost of all special moves by 1 point", 2],
            "Slam Dunk": ["Increases critical hit chance by 20%", 1],
            "Health Plus": ["Increases Cosmo's health by 5", 3],
            "Attack Plus": ["Increase Cosmo's attack by 1", 3],
            "Attack Up, Defense Down": ["Increase Cosmo's attack by 1, but decrease his defense by 1", 1]

        }
    def planning(self):
        planning = True
        while planning:
            slow_print(f"What do you want to do? (type 'help' for options or 'battle' to battle)")
            plan = input().lower()
            if plan == "help":
                slow_print(
                    "type 'b' for your badge menu, type 's' to see your current stats, or type 'i' to see your inventory")
            elif plan == "b":
                self.badge_manager()


            elif plan == "s":
                slow_print(
                    f"You have {self.player.health}/{self.player.STAT_HEALTH} hp, {self.player.attack} attack, {self.player.defense} defense, "
                    f"{self.player.endurance_points} energy points, and {self.player.current_experience} exp.")
            elif plan == 'battle':
                slow_print(f"Good luck!")
                break
            else:
                slow_print("Error! Invalid command.")


    def badge_manager(self):

        os.system('cls' if os.name == 'nt' else 'clear -x')
        print("Badge Menu")
        print("")
        slow_print(
            f"You have {self.player.BADGE_POWER_STAT} total badge points, and have {self.player.display_equipped_badges()} equipped")

        while True:
            slow_print(
                f"Type 'e' to equip a badge, 'u' to unequip, 'help' to get info on your badges, or anything else to exit the badge menu: ",
                new_line=False)
            entry = input()

            if entry == 'e':
                while True:
                    slow_print(
                        f"The badges you have are {self.player.display_obtained_badges()}. Type a badge name to equip it, or type 'cancel' to cancel: ")
                    badge = input()
                    if badge == "cancel":
                        break
                    slow_print(self.player.equip_badges(badge))
                    slow_print(f"You now have {self.player.get_usable_bp()} bp left")
                    if input("Equip another badge? (type 'y' to equip)").lower() != 'y':
                        break
            elif entry == 'u':
                while True:
                    slow_print(
                        f"The badges you have equipped are {self.player.display_equipped_badges()}. Type a badge name to unequip it, or type 'cancel' to cancel: ")
                    badge = input()
                    if badge == "cancel":
                        break
                    slow_print(self.player.unequip_badges(badge))
                    slow_print(f"You now have {self.player.get_usable_bp()} bp left")
                    if input("Unequip another badge? (type 'y' to continue)").lower() != 'y':
                        break
            elif entry == 'help':
                print()
                for badge in self.player.obtained_badges.keys():
                    print(f"{badge}: {self.badges[badge][0]}", end=";\t")
                print("")
                print()
                continue
            else:
                break

            os.system('cls' if os.name == 'nt' else 'clear -x')
            print("Badge Menu")
            print("")
            slow_print(
                f"You have {self.player.BADGE_POWER_STAT} total badge points, and have {self.player.display_equipped_badges()} equipped")


    def battle_begin(self, enemies, music):
        enemy_objects = []
        for enemy in enemies:
            if enemy == "Utah Fan":
                enemy_objects.append(UtahFan())
            if enemy == "Pikachu":
                enemy_objects.append(Pikachu())
            if enemy == "Ash":
                enemy_objects.append(Ash())

        music.start_music(loops=-1)
        battle = Battle(self.player, enemy_objects, music)
        return battle.battle()

    def obtain_badges(self, badge_name):
        current_cost, count = self.player.obtained_badges.get(badge_name, [self.badges[badge_name][1], 0])
        self.player.obtained_badges[badge_name] = [current_cost, count + 1]


    def battle_end(self, music, experience_points):
        #add experience points
        if experience_points > 0:
            print(f"You won! You got {experience_points} exp!")
            self.player.current_experience += experience_points
            if self.player.current_experience >= 100:
                self.player.level_up()
            music.end_music()
        else:
            print("You loser you died")