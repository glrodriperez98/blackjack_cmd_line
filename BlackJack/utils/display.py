def show_some(player,dealer):

    '''
    When the game starts, and after each time Player takes a card, 
    the dealer's first card is hidden and all of Player's cards are visible.
    '''

    print("\nDealer's Hand: ")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')

def show_all(player,dealer):

    '''
    At the end of the hand all cards are shown, 
    and you may want to show each hand's total value.
    '''
    
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
