from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self) -> None:
        self.fleet= []
    
    def create_fleet(self):
        robo1= Fleet("matilla", 20, 100)
        robo2= Fleet("metal man", 30, 100)
        robo3= Fleet("bolts", 25, 100)
        return[robo1,robo2,robo3]

