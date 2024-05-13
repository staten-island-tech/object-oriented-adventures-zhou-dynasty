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


