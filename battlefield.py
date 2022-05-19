from robot import Robot
from dinosaur import Dinosaur
import random

class Battlefield():

    def __init__(self):
        self.robot = Robot('Greg')
        self.dinosaur = Dinosaur('Ralph', random.randint(65, 85))

    def run_game(self):
        self.display_welcome()
        self.display_winner()

    def display_welcome(self):
        print(f'Welcome to the long awaited battle between Robot {self.robot.name} and Dinosaur {self.dinosaur.name}!')

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
            if self.dinosaur.health == 0 or self.robot.health == 0:
                break

    def display_winner(self):
        self.battle_phase()
        if self.dinosaur.health == 0:
            print(f'Dinosaur {self.dinosaur.name} wins! Well done!')
        else:
            print(f'Robot {self.robot.name} wins! Well done!')

