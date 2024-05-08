import time
import random
import json
import os
from storyline import storyline
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

def classselction():
        Class = input("Choose class (Archer, Mage, Swordsman): ")
        if Class == "Archer": 
            user = User(username, 20, 20, Class, "Short Bow")
            Player.append(user.__dict__)
        elif Class == "Mage":
            user = User(username, 15, 30, Class, "Magic Wand")
            Player.append(user.__dict__)
        elif Class == "Swordsman":
            user = User(username, 30, 10, Class, "Wooden Sword")
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

def storylinetime():
    p = storyline
    if Player["Class"] == "Archer":
        p.archerstoryline()
    elif Player['Class'] == "Mage": 
        p.mage()
    elif Player["Class"] == "Swordsman":
        p.swordsman()

print("Hello player, welcome!")
time.sleep(1)
username = input("What will your username be? ")
print(f"Hello {username}, welcome to Zhou Dynasty!")
time.sleep(1)

identifyingclass()

start = input("Are you ready to begin your adventure? Y/N: ")
if start.upper() != "Y":
    print("It didn't matter what you picked.")

time.sleep(1)
storylinetime()


















