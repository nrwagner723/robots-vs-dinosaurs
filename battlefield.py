from robot import Robot
from dinosaur import Dinosaur

class Battlefield():

    def __init__(self):
        self.robot = Robot('robot')
        self.dinosaur = Dinosaur('dino', 70)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print('Welcome to the battle')

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
            if self.dinosaur.health == 0:
                print('dino wins')
            else:
                print('robot wins')

    def display_winner(self):
        pass

