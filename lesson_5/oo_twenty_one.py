import random
import os
import time

def clear_screen():
    os.system('clear')

class Card:
    SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")
    RANKS = (
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    )

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self._hidden = False

    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, state):
        self._hidden = state

    @property
    def value(self):
        if self.is_ace():
            return "Ace"
        if self.is_face_card():
            return 10

        return int(self.rank)

    def is_jack(self):
        return self.rank == 'Jack'

    def is_queen(self):
        return self.rank == 'Queen'

    def is_king(self):
        return self.rank == 'King'

    def is_ace(self):
        return self.rank == 'Ace'

    def is_face_card(self):
        return self.is_jack() or self.is_queen() or self.is_king()

    def __str__(self):
        if self._hidden:
            return "Hidden"
        return f"{self.rank} of {self.suit}"





class Deck:

    def __init__(self):
        self.reset()

    def deal(self, num_cards):
        cards = [self.deck.pop() for _ in range(num_cards)]
        return cards

    def reset(self):
        self.deck = [Card(rank, suit)
                              for suit in Card.SUITS
                              for rank in Card.RANKS]
        random.shuffle(self.deck)




class Participant:
    def __init__(self):
        self.hand = []

    def reset_hand(self):
        self.hand.clear()




class Player(Participant):
    MAX_MONEY = 10
    def __init__(self):
        super().__init__()
        self._money = 5

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money = money

    def add_dollar(self):
        self.money += 1

    def remove_dollar(self):
        self.money -= 1

    def how_much_money(self):
        return f'You have ${self.money}!'

    def out_of_money(self):
        return self.money == 0

    def has_max_money(self):
        return self.money == Player.MAX_MONEY




class Dealer(Participant):
    def __init__(self):
        super().__init__()

    def hide_card(self):
        self.hand[1].hidden = True

    def reveal_card(self):
        self.hand[1].hidden = False




class TwentyOneGame:
    MAX_TOTAL = 21
    DEALER_MUST_STAY_SCORE = 17
    HIT = 'h'
    STAY = 's'

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()


    @staticmethod
    def join_or(lst, delimiter=', ', final_delimiter='or'):
        result = ''

        for element in lst[:-2]:
            result += f'{element}{delimiter}'
        if len(lst) > 1:
            result += f'{lst[-2]} {final_delimiter} {lst[-1]}'
        elif len(lst) == 1:
            return str(lst[0])


        return result


    def start(self):
        self.display_welcome_message()

        while True:
            self.play_one_round()
            if (self.player.out_of_money() or
                self.player.has_max_money() or
                not self.play_again()):
                break

        self.display_quitting_reason()
        self.display_goodbye_message()



    def deal_cards(self, participants, num_cards):
        for participant in participants:
            cards = self.deck.deal(num_cards)
            participant.hand.extend(cards)

    def show_cards(self):
        print("Dealer's cards:")
        for card in self.dealer.hand:
            print(card)

        print(f"\nPoints: {self.total_value(self.dealer.hand)}\n")

        print("Your cards:")
        for card in self.player.hand:
            print(card)

        print(f"\nPoints: {self.total_value(self.player.hand)}\n")
        print(self.player.how_much_money())



    def play_one_round(self):
        while True:
            self.reset_cards()
            clear_screen()
            self.deal_cards([self.player, self.dealer], 2)
            self.player_turn()
            if self.is_busted(self.player):
                break
            self.dealer_turn()
            break
        self.display_result()



    def reset_cards(self):
        self.deck.reset()
        self.player.reset_hand()
        self.dealer.reset_hand()



    def total_value(self, hand):
        total = 0
        ace_count = 0
        for card in hand:
            if card.hidden:
                continue
            if card.value == 'Ace':
                ace_count += 1
                continue

            total += card.value

        if ace_count > 0:
            total = self.handle_ace(total, ace_count)

        return total

    def handle_ace(self, total, ace_count):
        total += (11 * ace_count)
        for _ in range(ace_count):
            if total > 21:
                total -= 10

        return total


    def hit_or_stay(self):
        while True:
            answer = input("Hit or Stay? (h/s): ").strip().lower()
            if answer in [TwentyOneGame.HIT, TwentyOneGame.STAY]:
                return answer
            print("That's not a valid option\n")

    def is_busted(self, participant):
        return self.total_value(participant.hand) > 21



    def player_turn(self):
        self.dealer.hide_card()
        self.show_cards()
        while self.hit_or_stay() == TwentyOneGame.HIT:
            clear_screen()
            self.deal_cards([self.player], 1)
            self.show_cards()
            if self.is_busted(self.player):
                break



    def dealer_turn(self):
        self.dealer.reveal_card()
        while (self.total_value(self.dealer.hand) <
               TwentyOneGame.DEALER_MUST_STAY_SCORE):
            clear_screen()
            self.show_cards()
            print('Press enter to continue')
            input()
            self.deal_cards([self.dealer], 1)
            self.show_cards()
            if self.is_busted(self.dealer):
                break


    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Twenty-One!")
        print('Ready to play? Press enter to start!')
        input()

    def display_goodbye_message(self):
        print("Thank you for playing Twenty-One!")

    def get_result(self):
        player_score = self.total_value(self.player.hand)
        dealer_score = self.total_value(self.dealer.hand)

        if self.is_busted(self.player):
            self.player.remove_dollar()
            return (f'You busted! '
                    f'{self.player.how_much_money()}')

        if self.is_busted(self.dealer):
            self.player.add_dollar()
            return (f'The dealer busted! '
                    f'{self.player.how_much_money()}')

        if player_score > dealer_score:
            self.player.add_dollar()
            return (f'You had more points! '
                    f'{self.player.how_much_money()}')

        if dealer_score > player_score:
            self.player.remove_dollar()
            return (f'The dealer had more points! '
                   f'{self.player.how_much_money()}')

        return f"You tied! {self.player.how_much_money()}"

    def display_quitting_reason(self):
        clear_screen()
        if self.player.out_of_money():
            print("You're broke!")
        elif self.player.has_max_money():
            print('You bankrupted the dealer!')
        else:
            print('You chose to quit!')


    def display_result(self):
        clear_screen()
        self.show_cards()
        print()
        print(self.get_result())
        time.sleep(1.5)

    def play_again(self):
        prompt = 'Play again? (y/n): '
        while True:
            answer = input(prompt).strip().lower()
            if answer in ['yes', 'y', 'no', 'n']:
                break
            print("That's not a valid option.")
            print()

        return answer in ['yes', 'y']


game = TwentyOneGame()
game.start()