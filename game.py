import time
import os
from storyline import storyline
from classes import ClassSelection, Menu
Player = []
M = Menu

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

        M.menu()
        a.SelectAClass()

        while True:
            start = input("Are you ready to begin your adventure? Y/N: ").upper()
            os.system('cls')
            if start == "Y":
                break
            elif start == "N":
                AskOptions = ["GAME", "RESELECT", "QUIT"]
                M.message()
                Ask = input().upper()

                while Ask not in AskOptions: 
                    M.message
                    Ask = input().upper()

                if Ask == "GAME":
                    M.menu2()
                elif Ask == "RESELECT":
                    os.system('cls')
                    a.SelectAClass()
                elif Ask == "QUIT":
                    os.system('cls')
                    print("Game over...")
                    os.abort()

        os.system('cls')



        
game()
        




















