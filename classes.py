#Mobs
class Skeleton():
    def __init__(self, name, health, damage, weapon):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon
    def __str__(self):
        return f"{self.name}, {self.health}, {self.damage}, {self.weapon}"
    
WitherSkeleton = Skeleton("Wither Skeleton", 20, 20, "Stone Sword")

#User Class Selection
class ClassSelection():
    def __init__(self):
        self.ClassSelection = True
    
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
