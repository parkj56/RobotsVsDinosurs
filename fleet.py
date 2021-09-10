from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self) -> None:
        self.fleet= []
    
    def create_fleet(self):
        robo1= Robot("matilla", 15, 100)
        robo2= Robot("metal man", 20, 100)
        robo3= Robot("bolts", 10, 100)
        return[robo1,robo2,robo3]

    def creat_weapon(self):
        weapon1= Weapon("saw hand", 10)
        weapon2= Weapon("lasers", 5)
        weapon3= Weapon("chopping", 15)
        return[weapon1,weapon2,weapon3]

    

