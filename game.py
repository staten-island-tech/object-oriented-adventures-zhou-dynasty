import time
import random
from storyline import storyline
player = []

class User:
    def __init__(self, username, health, damage, Class, weapon):
        self.username = username
        self.health = health
        self.damage = damage
        self.Class = Class
        self.weapon = weapon
    def __str__(self):
        return f"{self.username}, {self. health}, {self.damage}, {self.Class}, {self.weapon}"

def classselction():
        Class = input("Choose class (Archer, Mage, Swordsman): ")
        if Class == "Archer": 
            s = User(username, 20, 20, Class, "Short Bow")
            player.append(s.__dict__)
        elif Class == "Mage":
            s = User(username, 15, 30, Class, "Magic Wand")
            player.append(s.__dict__)
        elif Class == "Swordsman":
            s = User(username, 30, 10, Class, "Wooden Sword")
            player.append(s.__dict__)
            
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

def storylinetime():
    p = storyline
    if player["Class"] == "Archer":
        p.archer()
    elif player["Class"] == "Mage": 
        p.mage()
    elif player["Class"] == "Swordsman":
        p.swordsman()

print("Hello player, welcome!")
time.sleep(1)
username = input("What will your username be? ")
print(f"Hello {username}, welcome to Zhou Dynasty!")
time.sleep(1)
identifyingclass()


















