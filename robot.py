
from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Laser', 50)


    def choose_weapon(choose_weapon):
      Robot.active_weapon = choose_weapon('Power Crusher', 'Shield', 'Laser')

    def attack(self, dinosaur):
     dinosaur.health -= self.attack_power.active_weapon

    

    
      


