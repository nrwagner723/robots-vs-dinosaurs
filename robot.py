from weapon import Weapon

class Robot():

    def __init__(self, name):
        self.name = ''
        self.health = 0
        self.active_weapon = Weapon()

    def attack(self, dinosaur):
        pass