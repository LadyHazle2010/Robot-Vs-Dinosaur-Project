
from battlefield import Battlefield

class Robot:

    def __init__(self, name):
        self.name = 'Cyborg'
        self.health = 100
        self.active_weapon = ('Laser')

    def robot_attack(self, dinosaur):
        self.active_weapon += dinosaur

    def robot_name(self):


