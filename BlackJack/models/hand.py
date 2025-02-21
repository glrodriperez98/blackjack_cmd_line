from .card import values

class Hand:
    
    '''
    This is the hand class that holds those Cards that have been dealt to each
    player from the Deck
    '''
    
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
