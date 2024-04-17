import time
import random
from classes import User

print("Hello player, welcome!")
time.sleep(1)
username = input("What will your username be? ")
time.sleep(2)
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

hp = 100
ArcherDamage = 20
MageDamage = 15
SwordsmanDamage = 30
Class = input("Choose class (Archer, Mage, Swordsman): ")
if Class == "Archer": 
    s = User(username, Class, )

