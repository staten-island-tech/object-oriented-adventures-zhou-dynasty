import time
import os
from storyline import storyline
from classes import ClassSelection
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
    print("Disclaimer: Your data does not save, it resets everytime you play.")
    menu = input("Start | Quit: ").upper()
    while True:
        if menu == "QUIT": 
            break
        elif menu == "START":
            os.system('cls')
            print("Hello player, welcome!")
            time.sleep(1)
            username = input("What will your username be? ")
            SelectionClassInstance = ClassSelection(username=username)
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
                    print("HEllo1")
                    x = input("Type to continue ")
                elif y.upper() == "ROLES":
                    print("Hello")
                    x = input("Type to continue ")
                elif y == "QUIT":
                    break
            elif x == "N":
                break

        SelectionClassInstance.SelectAClass()

        start = input("Are you ready to begin your adventure? Y/N: ")
        os.system('cls')
        print("It didn't matter what you picked.")
        time.sleep(1)

        
    
        for x in Player:
            if x['health'] <= 0:
                break
game()

















