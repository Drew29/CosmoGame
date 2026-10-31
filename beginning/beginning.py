import os
import random
import time

health = 10
base_attack = 3
defense = 0

enemy_health = 5
enemy_base_attack = 1
enemy_defense = 1



while health > 0 and enemy_health > 0:
    os.system('clear')
    print(f"Your health is {health}. The enemies health is {enemy_health}")
    action = input("What will you do? ")
    if action == 'attack':
        attack_power = round(base_attack * random.random())
        damage_given = attack_power - enemy_defense
        print(f"You attack! The enemy loses {damage_given} hp!")
        enemy_health -= damage_given
        if enemy_health <= 0:
            break
    else:
        print(f"You {action}. Nothing happened!")

    time.sleep(1)

    enemy_attack_power = round(enemy_base_attack * random.random()*2)
    damage_taken = enemy_attack_power - defense
    print(f"The enemy attacks! You lose {damage_taken} hp!")
    health -= damage_taken

    time.sleep(1)

if health > 0:
    print("You win!")
else:
    print("You lose!")