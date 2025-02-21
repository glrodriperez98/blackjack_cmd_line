# Blackjack Game

## Overview

This is a command-line Blackjack game written in Python. The game follows standard Blackjack rules where players compete against the dealer to get as close to 21 as possible without going over. The game includes features such as betting, chip management, and the ability to buy back in if the player runs out of chips.

## Features

- **Standard Blackjack Rules**: Players can hit, stand, and compete against the dealer.
- **Betting System**: Players must place a bet before each round.
- **Chip Management**: Players start with a set amount of chips and can continue playing until they run out.
- **Minimum & Maximum Buy-ins**: Players must buy in with an amount between \$10 and \$1000.
- **Buy-in Option if Chips Run Out**: Players can buy in again if they lose all their chips.
- **Clear Screen Between Rounds**: The console screen is cleared when a new round starts for a cleaner interface.
- **Exit Game Anytime**: Players can exit the game by entering 'q' during betting or hit/stand decisions.

## Requirements

- Python 3.x

## Running the Game

To start the game, navigate to the project directory and run:

```sh
python main.py
```

## How to Play

1. Run the script to start the game.
2. Enter your initial buy-in amount (between \$10 and \$1000).
3. Place a bet for the round.
4. Decide whether to hit or stand.
5. The dealer will play their turn after the player stands.
6. Win, lose, or push based on Blackjack rules.
7. Choose to play another hand or exit.
8. If chips run out, decide whether to buy in again or end the game.

## Project Structure and Description of Files

```
blackjack/
│
├── original_milestone_code/
│	├── blackjack_demo.py 	# Original Milestone Code **DO NOT RUN**
├── main.py                 # Entry point to start the game
├── game.py                 # Contains the main game logic
├── models/
│   ├── card.py             # Card and Deck classes
│   ├── hand.py             # Hand class for player and dealer
│   ├── chips.py            # Chip management for betting
├── utils/
│   ├── display.py          # Helper functions for displaying game status
└── README.md               # Documentation for the project
```

## Example Output

Below is an example of what the game looks like in the command-line interface:

```
Welcome to BackJack! Get as close to 21 as you can without going over!
    Dealer shits until they reach 17. Aces count as 1 or 11.
Enter Buy-In Amount (Min: 10, Max: 1000): 1000

How many chips would you like to bet? (or q to quit): 100

Dealer's Hand: 
 <card hidden>
 Ten of Diamonds

Player's Hand: 
 Two of Clubs
 Queen of Spades
Would you like to Hit or Stand or Quit? (h/s/q): h

Dealer's Hand: 
 <card hidden>
 Ten of Diamonds

Player's Hand: 
 Two of Clubs
 Queen of Spades
 Six of Hearts
Would you like to Hit or Stand or Quit? (h/s/q): h

Dealer's Hand: 
 <card hidden>
 Ten of Diamonds

Player's Hand: 
 Two of Clubs
 Queen of Spades
 Six of Hearts
 Ten of Spades
Player busts!
Player's total chips: 900
Play another hand? (y/n): n

Thanks for playing! Try again soon!
```

## Future Enhancements

- Add support for doubling down and splitting.
- Implement a graphical user interface (GUI) using Tkinter or PyGame.
- Introduce multiplayer support.
- Cash-out feature to allow for player to explicity end their session and walk away with winnings.

## Features Added

- Players must buy in with an amount between \$10 and \$1000 (02/21)
- The console screen is cleared when a new round starts for a cleaner interface (02/21)
- Players can exit the game by entering 'q' during betting or hit/stand decisions. (02/20)
- Players can buy back in if they run out of chips, instead of getting stuck. (02/21)
- Players cannot cheat by resetting their chips every round—they must continue with what they have (02/21)

Enjoy the game!

## License
This project is licensed under the MIT License.

## Author
Gabriel L. Rodriguez Perez

