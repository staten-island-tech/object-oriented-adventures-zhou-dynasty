import time
import random

class User:
    def __init__(self, username, health, damage, Class, weapon):
        self.username = username
        self.health = health
        self.damage = damage
        self.Class = Class
        self.weapon = weapon
    def __str__(self):
        return f"{self.username}, {self. health}, {self.damage}, {self.Class}, {self.weapon}"


print("Hello player, welcome!")
time.sleep(1)
username = input("What will your username be? ")
print(f"Hello {username}, welcome to Zhou Dynasty!")
Guide = input("Would you like a tutorial? Y/N: ")
if Guide.upper() == "Y":
    print("")

def classselction():
    Class = input("Choose class (Archer, Mage, Swordsman): ")
    if Class == "Archer": 
        s = User(username, 20, 20, Class, "Short Bow")
    elif Class == "Mage":
        s = User(username, 15, 30, Class, "Magic Wand")
    elif Class == "Swordsman":
        s = User(username, 30, 10, Class, "Wooden Sword")

def classconfirmation():
    confirm = input("Are you sure you want to pick this class? Y/N: ")
    if confirm.upper() != "Y":
        classselction()



