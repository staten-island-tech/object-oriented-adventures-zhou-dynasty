import os
#Mobs
class Mob():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def __str__(self):
        return f"{self.name}, {self.health}"

class Skeleton(Mob):
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
