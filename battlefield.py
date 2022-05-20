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
        print(f'\nWelcome to the long awaited battle between Robot {self.robot.name} and Dinosaur {self.dinosaur.name}!')

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            if self.dinosaur.health == 0 or self.robot.health == 0:
                break
            self.robot.attack(self.dinosaur)
            print(f'\nRobot {self.robot.name} attacked {self.dinosaur.name} with {self.robot.active_weapon.name} and did {self.robot.active_weapon.attack_power} damage!\nDinosaur {self.dinosaur.name} now has {self.dinosaur.health} health left!')
            self.dinosaur.attack(self.robot)
            print(f'\nDinosaur {self.dinosaur.name} attacked {self.robot.name} and did {self.dinosaur.attack_power} damage!\nRobot {self.robot.name} now has {self.robot.health} health left!')
            
    def display_winner(self):
        self.battle_phase()
        if self.dinosaur.health == self.robot.health:
            print(f'\nRobot {self.robot.name} and Dinosaur {self.dinosaur.name} tied!\n')
        elif self.dinosaur.health <= 0:
            print(f'\nRobot {self.robot.name} wins! Well done!\n')
        elif self.robot.health <= 0:
            print(f'\nDinosaur {self.dinosaur.name} wins! Well done!\n')

