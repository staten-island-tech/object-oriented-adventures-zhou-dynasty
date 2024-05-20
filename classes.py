import os
#Mobs
class Mobs():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def __str__(self):
        return f"{self.name}, {self.health}"
    
class Skeleton(Mobs):
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    def __str__(self):
        return f"{self.name}, {self.health}, {self.weapon}"
    
Skeleton1 = Skeleton("Skeleton", 30, "Wooden Sword")
WitherSkeleton = Skeleton("Wither Skeleton", 20, "Stone Sword")
Wither = Skeleton("Wither", 100, "???")

#Player
class User():
    def __init__(self, username, health, damage, Class, weapon):
        self.username = username
        self.health = health
        self.damage = damage
        self.Class = Class
        self.weapon = weapon
    def __str__(self):
        return f"{self.username}, {self.health}, {self.damage}, {self.Class}, {self.weapon}"

class ClassSelection:
    def __init__(self, username):
        self.username = username
        self.Player = None

    def SelectAClass(self):
        ClassChoices = ["ARCHER", "MAGE"]
        UserClassChoice = input("Choose your class (Archer, Mage): ").upper()

        while True:
            while UserClassChoice not in ClassChoices:
                os.system('cls')
                UserClassChoice = input("Choose your class (Archer, Mage): ").upper()

            confirmation = input(f"Are you sure you want to choose {UserClassChoice}? (Y/N): ").upper()
            if confirmation == 'Y':
                break
            else:
                os.system('cls')
                UserClassChoice = input("Choose your class (Archer, Mage): ").upper()

        if UserClassChoice == "ARCHER":
            self.Player = User(self.username, 20, 20, UserClassChoice, "Short Bow")
        elif UserClassChoice == "MAGE":
            self.Player = User(self.username, 15, 30, UserClassChoice, "Magic Wand")
