import time, random, os, sys
from newstorylinetest import *
import newstorylinetest as n






def newstorylinetime():
    placeholder = input('pick a class (archer, mage): ').upper()
    if placeholder == "ARCHER":
            n.archer()
    elif placeholder == "MAGE": 
            n.mage()
    else:
        print('pick an option given')
        newstorylinetime()
newstorylinetime()
    
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
        global Player
        os.system('cls')
        print("Hello player, welcome!")
        time.sleep(1)
        username = input("What will your username be? ")
        print(f"Hello {username}, welcome to Zhou Dynasty!")
        time.sleep(2)
        os.system('cls')
        beginning()




def newstorylinetime():

    for x in Player:
        if x['Class'] == "ARCHER":
            archer()
        elif x['Class'] == "MAGE": 
            mage()
newstorylinetime()
    
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
        global Player
        os.system('cls')
        print("Hello player, welcome!")
        time.sleep(1)
        username = input("What will your username be? ")
        print(f"Hello {username}, welcome to Zhou Dynasty!")
        time.sleep(2)
        os.system('cls')
        beginning()
game()