import os
#Entity
class entity():
    def __init__(self, name, hp, has_artisinal_bow = False, has_wither_bow = False, has_starlight_wand = False, has_hyperion = False):
        self.name = name
        self.hp = hp
        self.has_artisinal_bow = has_artisinal_bow
        self.has_wither_bow = has_wither_bow
        self.has_starlight_wand = has_starlight_wand
        self.has_hyperion = has_hyperion

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
        self.Player = []

    def SelectAClass(self):
        ClassChoices = ["ARCHER", "MAGE"]
        UserClassChoice = input("Choose your class (Archer, Mage): ").upper()
        self.Player.clear()

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
            self.Player.append(User(self.username, 20, 20, UserClassChoice, "Short Bow").__dict__)
        elif UserClassChoice == "MAGE":
            self.Player.append(User(self.username, 20, 20, UserClassChoice, "Magic Wand").__dict__)

#menu
class Menu:
    def __init__(self):
        self.Menu = True
        
    def menu():
        while True:
            os.system('cls')
            x = input("Would you like to learn about the game? Y/N: ").upper()
            if x == "Y":
                os.system('cls')
                print("What would you like to know about?")
                y = input("Mobs | Roles | Quit: ").upper()
                if y == "MOBS":
                    os.system('cls')
                    print("Skeleton - HP: 30 | Weapon: Wooden Sword")
                    print("Wither Skeleton - HP: 50 | Weapon: Stone Sword")
                    print("Wither - HP: ??? | Weapon: ???")
                    x = input("Type to continue ")
                elif y.upper() == "ROLES":
                    os.system('cls')
                    print("Archer - HP: 20 | DAMAGE: 20 | Weapon: Short Bow")
                    print("Mage - HP: 15 | DAMAGE: 30 | Weapon: Magic Wand")
                    x = input("Type to continue ")
                elif y == "QUIT":
                    break
            elif x == "N":
                break
        
    def menu2():
        while True:
            os.system('cls')
            x = input("Would you like to learn about the game? Y/N: ").upper()
            if x == "Y":
                os.system('cls')
                print("What would you like to know about?")
                y = input("Mobs | Roles: ").upper()
                if y == "MOBS":
                    os.system('cls')
                    print("Skeleton - HP: 20 | Weapon: Wooden Sword")
                    print("Wither Skeleton - HP: 50 | Weapon: Stone Sword")
                    print("Wither - HP: ??? | Weapon: ???")
                    x = input("Type to continue ")
                elif y.upper() == "ROLES":
                    os.system('cls')
                    print("Archer - HP: 20 | DAMAGE: 20 | Weapon: Short Bow")
                    print("Mage - HP: 20 | DAMAGE: 30 | Weapon: Magic Wand")
                    x = input("Type to continue ")
            elif x == "N":
                break
    
    def message():
        print("What would you like to do?")
        print("Game - Relearn about the game")
        print("Reselect - Reselect your class")
        print("Quit - Quit the game")

