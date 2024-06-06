import time
import os
from newstorylinetest import newstorylinetest
from classes import *   
Player = []


def newstorylinetime():
    p = newstorylinetest
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
        global Player
        os.system('cls')
        print("Hello player, welcome!")
        time.sleep(1)
        username = input("What will your username be? ")

        

        print(f"Hello {username}, welcome to Zhou Dynasty!")
        time.sleep(2)
        os.system('cls')

        storylinetime()
        



















