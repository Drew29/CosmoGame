import json

import readchar
import time

from management.game_manager import GameManager
from management.music_manager import MusicManager

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
    music = MusicManager("music/Battle.wav")

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

    with open("story_data/intro.json", "r") as file:
        data = json.load(file)
        for key in data.keys():
            if "battle" in key:
                slow_print(data[key][0])
                time.sleep(.5)
                exp = game_manager.battle_begin(data[key][1:], music)
                game_manager.battle_end(music, exp)
                if exp == 0:
                    break
                continue
            for line in data[key]:
                slow_print(line.replace("${name}", game_manager.player.name))
                readchar.readkey()

    if not game_manager.player.is_dead:
        print("You Win!")
    else:
        print("Game Over")

if __name__ == "__main__":
    main()