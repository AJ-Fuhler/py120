import random
import os
import time


class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')


    def __init__(self):
        self.move = None
        self.score = 0

    def move_object(self, choice):
        match choice:
            case 'rock':
                return Rock()
            case 'paper':
                return Paper()
            case 'scissors':
                return Scissors()
            case 'lizard':
                return Lizard()
            case 'spock':
                return Spock()


    def __str__(self):
        pass


class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        choice = random.choice(Player.CHOICES)
        self.move = self.move_object(choice)
        Move.history.append(f"{self} chose {self.move}.")

    def __str__(self):
        return 'Computer'

class Human(Player):
    CHOICE_ABBREVIATIONS = {
    'rock': ['r'],
    'paper': ['p'],
    'scissors': ['s', 'sc'],
    'lizard': ['l'],
    'spock': ['sp'],
}

    VALID_CHOICES =  [
        item for key, value in CHOICE_ABBREVIATIONS.items()
            for item in [key] + value]


    def __init__(self):
        super().__init__()


    def choose(self):
        print(f'Choose one: rock, paper, scissors, lizard or spock')
        choice = input().strip().lower()

        while choice not in Human.VALID_CHOICES:
            print("That's not a valid choice")
            choice = input().strip().lower()


        unabbreviated_choice = self._get_full_choice(choice)
        self.move = self.move_object(unabbreviated_choice)
        Move.history.append(f"{self} chose {self.move}.")

    def _get_full_choice(self, potential_abbreviation):
        for key, values in Human.CHOICE_ABBREVIATIONS.items():
            if potential_abbreviation in values:
                return key
        return potential_abbreviation

    def __str__(self):
        return 'You'

class Move:

    history = []

    def __init__(self):
        pass

    def __str__(self):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass


class Rock(Move):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'rock'

    def __gt__(self, other):
        return isinstance(other, (Lizard, Scissors))

    def __eq__(self, other):
        return isinstance(other, Rock)




class Paper(Move):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'paper'

    def __gt__(self, other):
        return isinstance(other, (Rock, Spock))

    def __eq__(self, other):
        return isinstance(other, Paper)



class Scissors(Move):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'scissors'

    def __gt__(self, other):
        return isinstance(other, (Paper, Lizard))



class Lizard(Move):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'lizard'

    def __gt__(self, other):
        return isinstance(other, (Spock, Paper))

    def __eq__(self, other):
        return isinstance(other, Lizard)



class Spock(Move):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Spock'

    def __gt__(self, other):
        return isinstance(other, (Scissors, Rock))

    def __eq__(self, other):
        return isinstance(other, Spock)




class RPSGame:
    WINNING_SCORE = 5

    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')


    @staticmethod
    def display_game_rules():
        print(
    '''Game Rules:

    Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons
    Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats
    paper, paper disproves Spock, Spock vaporizes rock, and rock crushes
    scissors. Whoever throws the winning signal wins! If both of you make the
    same signal, it's a tie.

    Tip: if you're feeling lazy, you can type: 
    'r' for rock
    'p' for paper
    's' or 'sc' for scissors 
    'l' for lizard
    'sp' for spock

    This is a Best of Seven. Whoever reaches 5 wins first, wins the match!
    ''')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _ready_to_start(self):
        print('Press Enter to start')
        input()

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        if human_move > computer_move:

            self._human.score += 1
            return True

        return None

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        if computer_move > human_move:

            self._computer.score += 1
            return True

        return None

    def _display_round_winner(self):

        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win this round!')
        elif self._computer_wins():
            print('Computer wins this round!')
        else:
            print("It's a tie this round")

        time.sleep(2)

    def _someone_won(self):
        return self._determine_winner()

    def _display_score(self):
        print(f"You: {self._human.score} | Computer: {self._computer.score}")

    def _determine_winner(self):
        if self._human.score == self.WINNING_SCORE:
            return 'You'
        if self._computer.score == self.WINNING_SCORE:
            return 'The computer'

        return None

    def _display_winner(self):
        print(f"{self._determine_winner()} won the Match!")


    def _play_again(self):
        print('Play again? (y/n)')
        answer = input().strip().lower()
        while answer not in ['y', 'yes', 'n', 'no']:
            print('Please choose a valid option')
            answer = input().strip().lower()

        return answer in ['y', 'yes']



    def _reset_scores(self):
        self._human.score = 0
        self._computer.score = 0


    def play(self):
        self._display_welcome_message()
        RPSGame.display_game_rules()
        self._ready_to_start()
        while True:
            self._reset_scores()
            while True:
                os.system('clear')
                self._display_score()
                self._human.choose()
                self._computer.choose()
                self._display_round_winner()
                if self._someone_won():
                    break

            os.system('clear')
            self._display_score()
            self._display_winner()

            if not self._play_again():
                break

        Move.history.clear()
        self._display_goodbye_message()


RPSGame().play()
