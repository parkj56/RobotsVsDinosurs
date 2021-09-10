from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.robofleet= Fleet().robots
        self.dinofleet= Herd().dinosaur

    def display_welcome(self):
        print("Welcome to the Dinosaurs Vs Robots game!")
        play_game= input("press 1 to start the battle!")
        
        if play_game == 1:
            return robo_turn
    
    def robo_turn(self, robot):
        





















def run_game(self):
        self.display_welcome()
        while len(self.dinosaurs_defeated) or len(self.robot_defeated) < 3:
            self.battle()
            self.robots_turn()
            self.dinosaurs_turn()
        self.display_winner()
