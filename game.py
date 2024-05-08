import time
import random
import json
import os
from storyline import storyline

with open("player.json", "r") as player:
    data = json.load(player)

class User():
    def __init__(self, username, health, damage, Class, weapon):
        self.username = username
        self.health = health
        self.damage = damage
        self.Class = Class
        self.weapon = weapon
    def __str__(self):
        return f"{self.username}, {self.health}, {self.damage}, {self.Class}, {self.weapon}"

def classselction():
        Class = input("Choose class (Archer, Mage, Swordsman): ")
        if Class == "Archer": 
            user = User(username, 20, 20, Class, "Short Bow")
            data.append(user.__dict__)
        elif Class == "Mage":
            user = User(username, 15, 30, Class, "Magic Wand")
            data.append(user.__dict__)
        elif Class == "Swordsman":
            user = User(username, 30, 10, Class, "Wooden Sword")
            data.append(user.__dict__)
            
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(data)

            f.write(json_string)

            os.remove("player.json")
            os.rename(new_file, "player.json")

            
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
        p.archerstoryline()
    elif player['Class'] == "Mage": 
        p.mage()
    elif player["Class"] == "Swordsman":
        p.swordsman()

print("Hello player, welcome!")
time.sleep(1)
username = input("What will your username be? ")
print(f"Hello {username}, welcome to Zhou Dynasty!")
time.sleep(1)

identifyingclass()
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)

    f.write(json_string)

os.remove("player.json")
os.rename(new_file, "player.json")


start = input("Are you ready to begin your adventure? Y/N: ")
if start.upper() != "Y":
    print("It didn't matter what you picked.")

time.sleep(1)
storylinetime()


















