class Robot:
    def __init__(self, name, health, attack_power, weapon) -> None:
        self.name= name
        self.health= health
        self.attackpower= attack_power
        self.weapon= weapon


    def attack(self, dinosaur):
        if (dinosaur.health != 0):
            dinosaur.health = dinosaur.health - self.weapon.attack_power
            print("you have", dinosaur.health, "health left!")