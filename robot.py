from weapon import Weapon
import random

class Robot():

    def __init__(self, name):
        self.name = name
        self.health = 350
        self.active_weapon = Weapon('Ole Betty', random.randint(65, 85))

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power

