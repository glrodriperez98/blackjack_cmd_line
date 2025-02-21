import os
from models.card import Deck
from models.hand import Hand
from models.chips import Chips
from utils.display import show_some, show_all


class BlackjackGame:

    MIN_BUY_IN = 10
    MAX_BUY_IN = 1000

    def __init__(self):
        self.playing = True

    def exit_game(self):
        print("Exiting the game. Thanks for playing!")
        exit()

    def clear_screen(self):
        """Clears the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def take_bet(self, chips):
        while True:
            bet = input('How many chips would you like to bet? (or q to quit): ')
            if bet.lower() == 'q':
                self.exit_game()
            try:
                chips.bet = int(bet)
                if chips.bet > chips.total:
                    print(f"Sorry, your bet can't exceed {chips.total}")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def hit(self, deck, hand):
        hand.add_card(deck.deal())

    def hit_or_stand(self, deck, hand):
        while True:
            choice = input("Would you like to Hit or Stand or Quit? (h/s/q): ").lower()
            if choice == 'h':
                self.hit(deck, hand)
            elif choice == 's':
                print("Player stands. Dealer is playing.")
                self.playing = False
            elif choice == 'q':
                self.exit_game()
            else:
                print("Invalid input, try again.")
                continue
            break

    def play(self):
        print("Welcome to BackJack! Get as close to 21 as you can without going over!\n\
    Dealer shits until they reach 17. Aces count as 1 or 11.")

        while True:

            '''
            While loop uses global class variables MIN_BY_IN and MAX_BUY_IN to set a minimum and maximum buy-in amount of 10-1000 and will print an error if buy-ins are not within
            the acceptable range or a valid input is provided
            '''

            try:
                buy_in = int(input(f"Enter Buy-In Amount (Min: {self.MIN_BUY_IN}, Max: {self.MAX_BUY_IN}): "))
                if buy_in < self.MIN_BUY_IN or buy_in > self.MAX_BUY_IN:
                    print(f"Buy-in must be between {self.MIN_BUY_IN} and {self.MAX_BUY_IN}.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        chips = Chips(buy_in)

        while True:

            '''
            If players chips reach Zero, they will be given the option to Buy-In again or quit the game. It allows players to to continue playing without
            restarting the game and prevents playing with negative chips which would break game logic
            '''

            if chips.total <= 0:
                print("You have run out of chips!")
                buy_in = input("Would you like to buy in again? (y/n): ").lower()
                if buy_in == 'y':
                    chips.total = int(input("Enter new Buy-In Amount: "))
                else:
                    print("Thanks for playing!")
                    break

            self.clear_screen()
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand()

            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

            self.take_bet(chips)
            show_some(player_hand, dealer_hand)

            self.playing = True
            while self.playing:
                self.hit_or_stand(deck, player_hand)
                show_some(player_hand, dealer_hand)
                if player_hand.value > 21:
                    print("Player busts!")
                    chips.lose_bet()
                    break

            if player_hand.value <= 21:
                while dealer_hand.value < 17:
                    self.hit(deck, dealer_hand)

                show_all(player_hand, dealer_hand)

                if dealer_hand.value > 21:
                    print("Dealer busts!")
                    chips.win_bet()
                elif dealer_hand.value > player_hand.value:
                    print("Dealer wins!")
                    chips.lose_bet()
                elif dealer_hand.value < player_hand.value:
                    print("Player wins!")
                    chips.win_bet()
                else:
                    print("It's a push!")

            print(f"Player's total chips: {chips.total}")

            new_game = input("Play another hand? (y/n): ").lower()
            if new_game == 'y':
                self.clear_screen()
                print(f"Starting a new game with {chips.total} chips.")
                continue
            else: 
                print("Thanks for playing! Try again soon!")
                break
