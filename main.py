
from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot

battlefield_a = Battlefield('robot', 'dinosaur')
battlefield_a.run_game()

battlefield_b = Battlefield('display_welcome', 'robot')
battlefield_b.display_welcome()

battlefield_c = Battlefield('Fight!', 'name')
battlefield_c.battle_phase()

battlefield_d = Battlefield("Winner is: ",'name_of_winner')
battlefield_d.display_winner()

dinosaur = Robot(50)
dinosaur.robot_attack()

robot = Dinosaur(100,'attack_power' )
robot.dinosaur_attack('Laser')



# dinosaur = dinosaur_attack()
# dinosaur.attack_power




# dinosaur.dinosaur_attack()