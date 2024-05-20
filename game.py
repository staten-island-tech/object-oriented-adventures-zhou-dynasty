import time
import os
from storyline import storyline
from classes import ClassSelection, WitherSkeleton
Player = []

def storylinetime():
    p = storyline
    for x in Player:
        if x['Class'] == "ARCHER":
            p.archerstoryline.archer()
        elif x['Class'] == "MAGE": 
            p.magestoryline.mage()

    
#menu 
def game():
    os.system('cls')
    menuChoices = ["START", "QUIT"]
    print("Disclaimer: Your data does not save, it resets everytime you play.")
    menu = input("Start | Quit: ").upper()

    while menu not in menuChoices:
        os.system('cls')
        print("Disclaimer: Your data does not save, it resets everytime you play.")
        menu = input("Start | Quit: ").upper()

    if menu == "QUIT": 
        os.system('cls')
        print("Game over...")
        os.abort()
    elif menu == "START":
        os.system('cls')
        print("Hello player, welcome!")
        time.sleep(1)
        username = input("What will your username be? ")
        a = ClassSelection(username=username)
        print(f"Hello {username}, welcome to Zhou Dynasty!")
        time.sleep(2)
        os.system('cls')

        while True:
            os.system('cls')
            x = input("Would you like to learn about the game? Y/N: ").upper()
            if x == "Y":
                os.system('cls')
                print("What would you like to know about?")
                y = input("Mobs | Roles | Quit: ").upper()
                if y == "MOBS":
                    os.system('cls')
                    print("Skeleton - HP: 20 | Weapon: Wooden Sword")
                    print("Wither Skeleton - HP: 50 | Weapon: Stone Sword")
                    print("Wither - HP: ??? | Weapon: ???")
                    x = input("Type to continue ")
                elif y.upper() == "ROLES":
                    os.system('cls')
                    print("Archer - HP: 20 | DAMAGE: 20 | Weapon: Short Bow")
                    print("Mage - HP: 15 | DAMAGE: 30 | Weapon: Magic Wand")
                    x = input("Type to continue ")
                elif y == "QUIT":
                    break
            elif x == "N":
                break

        a.SelectAClass()

        start = input("Are you ready to begin your adventure? Y/N: ")
        os.system('cls')
        print("It didn't matter what you picked.")
        time.sleep(1)

        
    
        for x in Player:
            if x['health'] <= 0:
                break



















