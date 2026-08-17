import json

import readchar
import time

from game_manager import GameManager
#from music_manager import MusicManager

def slow_print(text, delay=.025, new_line=True):
    for char in text:
        print(char, end="",flush=True)
        time.sleep(delay)
    if new_line:
        print("")

def slow_print_and_input(text, delay=.025):
    slow_print(text, delay, False)
    return input(" ")

def main():
    name = slow_print_and_input("What is your name?")
    game_manager = GameManager(name)
    #music = MusicManager("music/Battle.wav")

    slow_print(f"Welcome {name}! (Press any key to continue)")
    readchar.readkey()
    slow_print(f"You're in a secret locker room reserved only for Cosmos. Why? Because you applied to be Cosmo. I don't know why you did, honestly. I don't know if you even know why either... (press any key to continue)")
    readchar.readkey()
    slow_print("But, who knows what will happen?")
    readchar.readkey()
    slow_print("You're in your Cosmo suit, and you're ready for the interview!")
    readchar.readkey()
    slow_print("You walk through the door.")
    readchar.readkey()

    with open("intro.json", "r") as file:
        data = json.load(file)
        for key in data.keys():
            if "battle" in key:
                slow_print(data[key][0])
                time.sleep(.5)
                #exp = game_manager.battle_begin(data[key][1:], music)
                #game_manager.battle_end(music, exp)
                continue
            for line in data[key]:
                slow_print(line.replace("${name}", game_manager.player.name))
                readchar.readkey()
    #music.start_music()

    #planning
    #slow_print(f"Welcome {name}! You are now Cosmo. What do you want to do? (type 'help' for options or 'battle' to battle)")
    #game_manager.planning()


    #slow_print("A wild creature attacks!", .005)

    #time.sleep(.1)


    """battle1 = Battle(game_manager.player, [Pikachu()], music)
    battle1.battle()

    music.end_music()
    slow_print("The Pikachu is no more!", .1)
"""
    #time.sleep(2)

    #music.start_music()
    # slow_print("But two more want revenge!", .005)
    # time.sleep(.5)
    #
    # if not game_manager.player.is_dead:
    #     battle2 = Battle(game_manager.player, [Pikachu(), Pikachu()], music)
    #     battle2.battle()
    #
    # #music.end_music()
    # slow_print("The two of them didn't stand a chance.", .1)
    # time.sleep(1)
    # #music.start_music()
    # slow_print("But three of them are determined to take you down!", .005)
    # time.sleep(.5)
    #
    # if not game_manager.player.is_dead:
    #     battle3 = Battle(game_manager.player, [Pikachu(), Pikachu(), Pikachu()], music)
    #     battle3.battle()

    if not game_manager.player.is_dead:
        print("You Win!")
    else:
        print("Game Over")

if __name__ == "__main__":
    main()