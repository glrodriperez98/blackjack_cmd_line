
   															############################################################
                                                            #THIS IS THE ORIGINAL BLACKJACK MILESTONE CODE...DO NOT RUN#
                                                            ############################################################
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    
    This is the card class where each Card object has a suit and a rank
    

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    
    This is the deck class which holds all 52 Card objects and can be shuffled
    

    def __init__(self):
        self.deck = [] # starts with an empty list
        for suit in suits:
            for rank in ranks:
                # Creates card object
                created_card = Card(suit,rank)
                self.deck.append(created_card)
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    
    
    This is the hand class that holds those Cards that have been dealt to each
    player from the Deck
    
    
    def __init__(self):
        self.cards = [] # starts with an empty list as we did in the Deck Class
        self.value = 0 # starts with zero value
        self.aces = 0 # add an attribute to keep track of aces (can be 1 or 11)

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1 # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    
    This is the Chips class that keeps track of a Player's starting chips, bets,
    and ongoing winnings
    

    def __init__(self):
        self.total = int(input("Please enter your Buy-In: ")) # User inputs their starting amount for the game
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    
    This function allows the Player to input the amount they would like to bed.
    It uses a while loop to continually prompt the user for input until it recieves an i
    integer value that IS WITHIN the Player's better limit
    
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?: '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(deck,hand):

    
    This functions allows player to take a hit until the bust (over 21). It takes in
    Deck and Hand objects as arguments, and deals one card off the deck and adds to Hand.
    It checks for aces in the even that a player's hand exceeds 21
    

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):

    
    This function accepts the deck and the player's hand as arguments, and assigns playing 
    as a global variable. If the Player Hits, employ the hit() function above. 
    If the Player Stands, set the playing variable to False - this will control the behavior of a while loop later 
    on in our code.
    
    
    global playing # controls an upcoming while loop
    
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck,hand) # hit() function defined above
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):

    
    When the game starts, and after each time Player takes a card, 
    the dealer's first card is hidden and all of Player's cards are visible.
    

    print("\nDealer's Hand: ")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')

def show_all(player,dealer):

    
    At the end of the hand all cards are shown, 
    and you may want to show each hand's total value.
    
    
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


These functions handle end of game scenarios by passing player's hand, dealer's hand
and chips as needed


def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push")

while True:
    
    
    Game logic and control flow
    

    # Print an opening statement
    print('Welcome to BackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until they reach 17. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips() # Chips is based on user input

    # Prompt the player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing: # recall variable from hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        # If player's hand exceeds 21, run player(busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scnenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        
        else:
            push(player_hand,dealer_hand)

    # Inform Player of their chips total
    print("\nPlayer's winning stand at $",player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
'''