from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.robofleet= Fleet().robots
        self.dinofleet= Herd().dinosaur
        self.robot_defeated = []
        self.dinosaurs_defeated = []

    def display_welcome(self):
        print("Welcome to the Dinosaurs Vs Robots game! you will play as the robots to defeat the dinos!")
    
    def battle(self):
        print ("time to battle!")

    def robo_list(self):
        print(self.fleet)

    def dino_list(self):
        print(self.herd)

    while target.health > 0:
        def robo_turn(self):
            print (self.fleet)
            user_attack = input('who would you like to  attack with? robot1 robot2 or robot3 ?')
            print (self.herd)
            if user_attack== 1:
                attacker= robo1
                return attacker
            elif user_attack== 2:
                attacker= robo2
                return attacker
            elif user_attack== 1:
                attacker= robo3
                return attacker
            
            print (self.create_weapons)
            user_weapon= input("which weapon would you like to use? 1, 2, or 3?")
            if user_weapon== 1:
                weapon_choice= weapon1
            elif user_weapon== 2:
                weapon_choice= weapon2
            elif user_weapon== 3:
                weapon_choice= weapon3
                return weapon_choice
            
            
            user_target= input('who would you like to attack? dino1, dino2, or dino3 ?')
            if user_target== 1:
                target= dino1
                return target
            elif user_target== 2:
                target= dino2
                return target
            elif user_target== 3:
                target= dino3
                return target

            if target.health < 0:
                self.dinosaurs_defeated.append(target)

        def dino_turn(self):
            print (self.herd)
            user_attack = input('who would you like to  attack with? robot1 robot2 or robot3 ?')
            if user_attack == 1:
                attacker = dino1
                return attacker
            elif user_attack == 2:
                attacker = dino2
                return attacker
            elif user_attack == 1:
                attacker = dino3
            return attacker
            
            user_target = input('who would you like to attack? 1, 2, or 3 ?')
            print(self.fleet)
            if user_target == 1:
                target = robot1
                return target
            elif user_target == 2:
                target = robot2
                return target
            elif user_target == 3:
                target = robot3
                return target

            if target.health < 0:
                self.robot_defeated.append(target) 

    def display_winner(self):
        if len(self.robot_defeated) == 3:
            print('Dinodaurs Win!!')
        elif len(self.robot_defeated) == 3:
            print (Robots Win!!)  




















def run_game(self):
        self.display_welcome()
        while len(self.dinosaurs_defeated) or len(self.robot_defeated) < 3:
            self.battle()
            self.robots_turn()
            self.dinosaurs_turn()
        self.display_winner()
