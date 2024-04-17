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


hp = 100
ArcherDamage = 20
MageDamage = 15
SwordsmanDamage = 30
Class = input("Choose class (Archer, Mage, Swordsman): ")
if Class == "Archer": 
    s = User(username, Class, )

print('Your adventure begins now {username}.')
time.sleep(1)
print('You encounter a skeleton, a fierce battle begins.')