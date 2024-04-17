class Skeleton:
    def __init__(self, health, damage, weapon, drops):
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.drops = drops
    def __str__(self):
        return f"{self.health}, {self.damage}, {self.weapon}, {self.drops}"

class WitherSkeleton(Skeleton):
    def __init__(self, health, damage, weapon, drops):
        self.health = health
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.drops = drops
    def __str__(self):
        return f"{self.health}, {self.damage}, {self.weapon}, {self.drops}"

class SpiderJockey(Skeleton):
    def __init__(self, health, damage, weapon, drops):
        self.health = health
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.drops = drops
    def __str__(self):
        return f"{self.health}, {self.damage}, {self.weapon}, {self.drops}"
    
class SkeletonHorse(Skeleton): 
    def __init__(self, health, damage, weapon, drops):
        self.health = health
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.drops = drops
    def __str__(self):
        return f"{self.health}, {self.damage}, {self.weapon}, {self.drops}"
    
class Stray(Skeleton):
    def __init__(self, health, damage, weapon, drops):
        self.health = health
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.drops = drops
    def __str__(self):
        return f"{self.health}, {self.damage}, {self.weapon}, {self.drops}"
    
class User:
    def __init__(self, username, health, damage, Class, weapon):
        self.username = username
        self.health = health
        self.damage = damage
        self.Class = Class
        self.weapon = weapon
    def __str__(self):
        return f"{self.username}, {self. health}, {self.damage}, {self.Class}, {self.weapon}"