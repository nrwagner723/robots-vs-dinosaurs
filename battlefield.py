from robot import Robot
from dinosaur import Dinosaur

class Battlefield():

    def __init__(self):
        self.robot = Robot('Greg')
        self.dinosaur = Dinosaur('Ralph', 70)

    def run_game(self):
        self.display_welcome()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to the long-awaited battle between the Robot and the Dinosaur!')

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
            if self.dinosaur.health == 0 or self.robot.health == 0:
                break

    def display_winner(self):
        self.battle_phase()
        if self.dinosaur.health == 0:
            print(f'{self.dinosaur.name} wins! Well done!')
        else:
            print(f'{self.robot.name} wins! Well done!')

