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
