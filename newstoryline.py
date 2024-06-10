import time, random, os, sys
from classes import entity

def wait(duration):
    time.sleep(duration)


def beginning():
    print("Your adventure begins now.")
    print('You look around, confused, you decide to wander around.')
    print('You search for answers, none to be found.')
    print('Until.')
    wait(duration)
    print('You encounter a skeleton!')
    wait(duration)
    print('It seemed agitated?')
    wait(duration)
    print('It charges at you.')
    print('A battle of the ages begin.')
    wait(duration)
    os.system("cls")

def archer():
    fight_archer(skeleton)
    fight_archer(wither_skeleton)
    fight_archer(wither)

def mage():
    fight_mage(skeleton)
    fight_mage(wither_skeleton)
    fight_mage(wither)


player = entity("Player", 20)
skeleton = entity("Skeleton", 30)
wither_skeleton = entity("Wither Skeleton", 50)
wither = entity("Wither", 200)

def fight_archer(enemy):
    while player.hp > 0 and enemy.hp > 0:
        wait(duration)
        os.system("cls")
        move = input('Pick your first/next move (Shoot, Defend, Run): ').lower()
        if move == 'shoot':
            print('You fired off an arrow.')
            damage = 20
            damage1 = 2
            if player.has_artisinal_bow:
                damage += 5
            if player.has_wither_bow:
                damage += 30
            enemy.hp -= damage
            player.hp -= damage1
            print(f"You have {player.hp} hp left!")
            print(f"The mob has {enemy.hp} hp left.")
        elif move == 'defend':
            print('You defended, nice job big back!.')
            print(f"You have {player.hp} hp left!")            
            player.hp -= 1
        elif move == 'run':
            print('You attempted to vent to a different location.')
            wait(duration)
            print(f'{enemy.name} found you and threw you into the backrooms.')
            player.hp -= 4
            print(f"You have {player.hp} hp left!")
        else:
            print('Please pick a valid move.')
            fight_archer()
    if player.hp > 0:
        wait(duration)
        print(f"You defeated the {enemy.name}!")
        if enemy.name == 'Skeleton':
            os.system('cls')
            print('good job, you beat the first mob')
            print('onwards.')
            wait(duration)
            print('You decide to adventure because you have no choice because i said so.')
            wait(duration)
            print('you discovered a black coal mob.')

        if enemy.name == 'Wither Skeleton':
            print('Good job, you have done well ngl')
            wait(duration)
            print('you still cooked anyways bruh')
            print('well gl')
        if enemy.name == "Wither":
            print('Wow, you won, you probably got lucky ngl.')
            wait(duration)
            print('But good job anyways.')
            print('bye')
            sys.exit()
        if random.randint(1,2) == 1 and enemy.name == "Skeleton":
            print("You got an artisinal shortbow.")
            wait(duration)
            print("Nice!")
            player.has_artisinal_bow = True
            time.sleep(5)
            print('jefferson sucks....')
        elif random.randint(1, 10) == 1 and enemy.name == "Wither Skeleton":
            print("You got a wither bow.")
            wait(duration)
            print("Nice!")
            player.has_wither_bow = True
        else:
            print("No drop! Too bad, too sad.")
        if player.hp <= 0:
            os.system('cls')
            print('damn you must suck at this horribly made game')
            print('trash')
            sys.exit()
    else:
        print("You died L")


def fight_mage(enemy):
    while player.hp > 0 and enemy.hp > 0:
        wait(duration)
        os.system("cls")
        move = input('Pick your first/next move (Shoot, Defend, Run): ').lower()
        if move == 'shoot':
            print('You fired off an arrow.')
            damage = 20
            damage1 = 2
            if player.has_starlight_wand:
                damage += 5
            if player.has_hyperion:
                damage += 30
            enemy.hp -= damage
            player.hp -= damage1
            print(f"You have {player.hp} hp left!")
            print(f"The mob has {enemy.hp} hp left.")
        elif move == 'defend':
            print('You defended, nice job big man!.')
            print(f"You have {player.hp} hp left!")
            player.hp -= 1
        elif move == 'run':
            print('You attempted to vent to a different location.')
            wait(duration)
            print(f'{enemy.name} found you and threw you into the backrooms.')
            player.hp -= 4
            print(f"You have {player.hp} left!")
        else:
            print('Please pick a valid move.')
    if player.hp > 0:
        print(f"You defeated the {enemy.name}!")
        if enemy.name == 'Skeleton':
            os.system('cls')
            print('good job, you beat the first mob')
            print('onwards.')
        if enemy.name == 'Wither Skeleton':
            print('Good job, you have done well ngl')
            wait(duration)
            print('you still cooked anyways bruh')
            print('well gl')
        if enemy.name == "Wither":
            print('Wow, you won, you probably got lucky ngl.')
            wait(duration)
            print('But good job anyways.')
            print('bye')
        if random.randint(1,2) == 1 and enemy.name == "Skeleton":
            print("You got a starlight wand.")
            wait(duration)
            print("Nice!")
            player.has_starlight_wand = True
        elif random.randint(1, 10) == 1 and enemy.name == "Wither Skeleton":
            print("You got a hyperion.")
            wait(duration)
            print("Nice!")
            player.has_hyperion = True
        else:
            print("No drop! Too bad, too sad.")
            print("You can't win, AHAHAHAHAHA.")
        if player.hp <= 0:
            os.system('cls')
            print('damn you must suck at this horribly made game')
            print('trash')
            sys.exit()
      
os.system('cls')
try:

    duration = int(input("Enter delay duration in seconds (default 2): "))
except ValueError:
    print("Invalid Input! Your delay durtion will be 2 seconds")
    duration = 2