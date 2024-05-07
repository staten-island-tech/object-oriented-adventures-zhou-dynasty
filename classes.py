class Skeleton:
    def __init__(self, health, damage, weapon):
        self.health = health
        self.damage = damage
        self.weapon = weapon
    def __str__(self):
        return f"{self.health}, {self.damage}, {self.weapon}"

    