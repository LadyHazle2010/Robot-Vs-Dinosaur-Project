
class Dinosaur:

    def __init__(self, name, attack_power) :
        self.name = name
        self.attack_power = attack_power, 50
        self.health = 100

    def dinosaur_attack(self, robot):
        robot.health -= self.attack_power(50)

    
