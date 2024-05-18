import time
import os
from storyline import storyline
from classes import User, Skeleton, WitherSkeleton
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
    menu = input("Start | Quit: ")
    while True:
        if menu.upper() == "QUIT": 
            break
        elif menu.upper() == "START":
            os.system('cls')
            print("Hello player, welcome!")
            time.sleep(1)
            username = input("What will your username be? ")
            print(f"Hello {username}, welcome to Zhou Dynasty!")
            time.sleep(2)
            os.system('cls')
        while True:
            x = input("Would you like to learn about the game? Y/N: ")
            if x.upper() == "Y":
                os.system('cls')
                print("What would you like to know about?")
                y = input("Mobs | Roles | Quit")
                if y.upper() == "MOBS":
                    print #print the mobs
                elif y.upper() == "ROLES":
                    print
                elif y.upper() == "QUIT":
                    break

        
    
        start = input("Are you ready to begin your adventure? Y/N: ")
        os.system('cls')
        print("It didn't matter what you picked.")
        time.sleep(1)

        storylinetime()
        
        for x in Player:
            if x['health'] <= 0:
                break


















