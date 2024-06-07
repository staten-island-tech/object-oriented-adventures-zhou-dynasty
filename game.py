<<<<<<< HEAD
import time
import os
from newstorylinetest import *
from classes import *   
Player = []
M = Menu
=======
import time, random, os, sys
from newstoryline import *
import newstoryline as n
>>>>>>> 19e5e370d9f103cce61492d1d2a67ec713f52c31






def newstorylinetime():

    placeholder = input('pick a class (archer, mage): ').upper()
    if placeholder == "ARCHER":
            n.archer()
    elif placeholder == "MAGE": 
            n.mage()
    else:
        print('pick an option given')
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
<<<<<<< HEAD

        M.menu()
        a.SelectAClass()
        Player = a.Player

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
                    Player.clear()
                    a.SelectAClass()
                    Player.clear()
                    Player = a.Player
                elif Ask == "QUIT":
                    os.system('cls')
                    print("Game over...")
                    os.abort()

        os.system('cls')

        
        for x in Player:
            
            beginning()
            if x['Class'] == "ARCHER":
                archer()
            elif x['Class'] == "MAGE":
                mage()
            
       
        
game()
        

















=======
        beginning()
>>>>>>> 19e5e370d9f103cce61492d1d2a67ec713f52c31

