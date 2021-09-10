from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaur= []
    
    def create_herd(self):
           dino1= Dinosaur("travypatty", 30, 110)
           dino2= Dinosaur("datboi", 25, 100)
           dino3= Dinosaur("kermit",20, 100)
           return [dino1,dino2,dino3]
           
    