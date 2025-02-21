class Chips:

    '''
    This is the Chips class that keeps track of a Player's starting chips, bets,
    and ongoing winnings
    '''

    def __init__(self, total):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet