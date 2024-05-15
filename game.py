import time
import os
from storyline import storyline
from classes import User
Player = []

def storylinetime():
    p = storyline
    for x in Player:
        if x['Class'] == "ARCHER":
            p.archerstoryline.archer()
        elif x['Class'] == "MAGE": 
            p.magestoryline.mage()
    

def classselction():
        while True:
            Class = input("Choose your class (Archer, Mage): ")
            if Class.upper() == "ARCHER": 
                user = User(username, 20, 20, Class.upper(), "Short Bow")
                Player.append(user.__dict__)
                break
            elif Class.upper() == "MAGE":
                user = User(username, 15, 30, Class.upper(), "Magic Wand")
                Player.append(user.__dict__)
                break
            else:
                print("Pick a class.")

    
    

def classconfirmation():
    while True:
        confirmation = input("Are you sure you want to select this class? Y/N: ")
        if confirmation.upper() != "Y":
            classselction()
        else: 
            break

def identifyingroles():
    classselction()
    classconfirmation()

    
#menu 
while True:
    os.system('cls')
    print("Disclaimer: Your data does not save, it resets everytime you play.")
    menu = input("Start | Quit: ")
    if menu.upper() == "QUIT": 
        os.system('cls')
        print("Game over")
        break
    elif menu.upper() == "START":
        os.system('cls')
        print("Hello player, welcome!")
        time.sleep(1)
        username = input("What will your username be? ")
        print(f"Hello {username}, welcome to Zhou Dynasty!")
        time.sleep(2)
        os.system('cls')
        identifyingroles()
    
        start = input("Are you ready to begin your adventure? Y/N: ")
        os.system('cls')
        print("It didn't matter what you picked.")
        time.sleep(1)

        storylinetime()
        
        for x in Player:
            if x['health'] <= 0:
                break




















