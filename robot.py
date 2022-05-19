from weapon import Weapon

class Robot():

    def __init__(self, name):
        self.name = name
        self.health = 350
        self.active_weapon = Weapon('Ole Betty', 70)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power

robot_one = Robot('Greg')
print(robot_one.active_weapon.name)