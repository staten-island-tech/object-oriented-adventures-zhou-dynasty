import time
from storyline import storyline
from classes import ClassSelection
Player = []

class User():
    def __init__(self, username, health, damage, Class, weapon):
        self.username = username
        self.health = health
        self.damage = damage
        self.Class = Class
        self.weapon = weapon
    def __str__(self):
        return f"{self.username}, {self.health}, {self.damage}, {self.Class}, {self.weapon}"

def storylinetime():
    p = storyline
    for x in Player:
        if x['Class'] == "ARCHER":
            p.archerstoryline
        elif x['Class'] == "MAGE": 
            p.mage()
        elif x['Class'] == "SWORDSMAN":
            p.swordsman()

def classselction():
        Class = input("Choose class (Archer, Mage, Swordsman): ")
        if Class.upper() == "ARCHER": 
            user = User(username, 20, 20, Class.upper(), "Short Bow")
            Player.append(user.__dict__)
        elif Class.upper() == "MAGE":
            user = User(username, 15, 30, Class.upper(), "Magic Wand")
            Player.append(user.__dict__)
        elif Class.upper() == "SWORDSMAN":
            user = User(username, 30, 10, Class.upper(), "Wooden Sword")
            Player.append(user.__dict__)

def classconfirmation():
        while True:
            confirmation = input("Are you sure you want to select this class? Y/N: ")
            if confirmation.upper() != "Y":
                classselction()
            else: 
                break
    
def identifyingclass():
    classselction()
    classconfirmation()

#start
print("Hello player, welcome!")
time.sleep(1)
username = input("What will your username be? ")
print(f"Hello {username}, welcome to Zhou Dynasty!")
time.sleep(1)

identifyingclass()

start = input("Are you ready to begin your adventure? Y/N: ")
print("It didn't matter what you picked.")

time.sleep(1)

storylinetime()


















