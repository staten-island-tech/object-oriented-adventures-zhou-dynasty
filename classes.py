import os
#Mobs
class Mobs():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def __str__(self):
        return f"{self.name}, {self.health}"
    
class Skeleton(Mobs):
    def __init__(self, name, health, damage, weapon):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon
    def __str__(self):
        return f"{self.name}, {self.health}, {self.damage}, {self.weapon}"
    
WitherSkeleton = Skeleton("Wither Skeleton", 20, 20, "Stone Sword")

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

class CLassSelection:
    def __init__(self, username):
        self.Player = []
        self.Username = username
        self.Class = None

    def SelectingAClass(self):
        ClassChoices = ["ARCHER", "MAIN"]
        ClassChoice = input("Choose your class (Archer, Mage): ").upper()

        while True:
            while ClassChoice not in ClassChoices:
                os.system('cls')
                ClassChoice = input("Choose your class (Archer, Mage): ").upper()

            confirmation = input(f"Are you sure you want to choose {ClassChoice}? (Y/N): ").upper()
            if confirmation == 'Y':
                break
            else:
                os.system('cls')
                UserClassChoice = input("Choose your class (Archer, Mage): ").upper()

    

