
from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot

battlefield_a = Battlefield('robot', 'dinosaur')
battlefield_a.run_game()

battlefield_b = Battlefield('display_welcome')
battlefield_b.display_welcome()

dinosaur = Robot(-50)
dinosaur.robot_attack('battlefield phase')

robot = Battlefield()



# dinosaur = dinosaur_attack()
# dinosaur.attack_power




# dinosaur.dinosaur_attack()