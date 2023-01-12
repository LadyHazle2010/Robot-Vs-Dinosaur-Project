
from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot

battlefield_a = Battlefield()
battlefield_a.run_game()

battlefield_b = Battlefield()
battlefield_b.display_welcome()

battlefield_c = Battlefield()
battlefield_c.battle_phase()

battlefield_d = Battlefield()
battlefield_d.display_winner()

dinosaur = Robot(50)
print(dinosaur.robot_attack)

robot = Dinosaur(100,'attack_power' )
print(robot.dinosaur_attack)



# dinosaur = dinosaur_attack()
# dinosaur.attack_power




