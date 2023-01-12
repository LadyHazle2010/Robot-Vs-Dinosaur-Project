
from dinosaur import Dinosaur
from robot import Robot




class Battlefield:

    def __init__(self, attack_power):
      self.robot = Robot('Cyborg') 
      self.dinosaur = Dinosaur('Dino')

       
    def run_game(self):
        print('Fight!')
       


    def display_welcome(self):
        print('Welcome!Let us Being!')




    def battle_phase(self): 
        self.robot.attack(self.dinosaur)
        self.robot != 0
        print(self.dinosaur)

        self.dinosaur.attack(self.robot)
        self.dinosaur != 0
        print(self.robot)
                




    def display_winner(self,):
       self.dinosaur = 100
       print('Winner Dino!') 

       self.robot = 100
       print('Winner Cyborg')


       
        


       
