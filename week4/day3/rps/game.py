from random import random

class RockPaperScissors:
    def __init__(self, user):
        self.user = user
        self.comp_choice()
        self.results = []
    
    def comp_choice(self):
        possibilities = ['rock', 'paper', 'scissors']
        num = random(2)
        self.comp = possibilities[num]

    def play(self):
        if self.comp == "rock" and self.user == "rock":
            self.results.append("tie")

    def play_again(self, user):
        self.user = user
        self.play()
