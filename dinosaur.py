class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 350
        self.attack_power = attack_power

    def attack(self, robot):
        robot.health -= self.attack_power