import random
import math

class GuessingGame:

    def __init__(self, low, high):
        self.low = low
        self.high = high

    def play(self):
        
        guesses = int(math.log2(self.high - self.low + 1)) + 1
        number = random.choice(range(self.low, self.high + 1))
        while guesses > 0:
            print(f"You have {guesses} guesses remaining.")
            guess = int(input(f"Enter a number between {self.low} and {self.high}: "))
            while not self.valid_number(guess):
                guess = int(input((f"Invalid guess. "
                                   f"Enter a number between 1 and 100: ")))
            
            if guess == number:
                print("That's the number!\n\nYou won!")
                break
            elif guess < number:
                print("Your guess is too low.\n")
            else:
                print("Your guess is too high.\n")
            
            guesses -= 1
        
        if guesses == 0:
            print('You have no more guesses. You lost!')
    
    
    def valid_number(self, value):
        return isinstance(value, int) and value in range(self.low, self.high + 1)
    
game = GuessingGame(501, 1500)
game.play()
            
            
