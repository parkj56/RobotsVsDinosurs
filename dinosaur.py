
class Dinosaur:
    def __init__(self, name, health, attack_power, weapon):
        self.name= name
        self.health= health
        self.attackpower= attack_power
        self.weapon= weapon

    def attack(self, robot):
        if (robot.health != 0):
            robot.health = robot.health - self.attack_power
            print ("you have", robot.health, "health left!" )

        
        