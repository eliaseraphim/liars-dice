# author: elia deppe
# email: elia.deppe7@gmail.com
# filename: main.py

from game import Game

TITLE = """
██      ██  █████  ██████  ███████     ██████  ██  ██████ ███████ 
██      ██ ██   ██ ██   ██ ██          ██   ██ ██ ██      ██      
██      ██ ███████ ██████  ███████     ██   ██ ██ ██      █████   
██      ██ ██   ██ ██   ██      ██     ██   ██ ██ ██      ██      
███████ ██ ██   ██ ██   ██ ███████     ██████  ██  ██████ ███████ 
"""

RULES = """
Five dice are used per player with dice cups used for concealment.

Each round, each player rolls a "hand" of dice under their cup and looks at their hand while keeping it concealed from
the other players. The first player begins bidding, announcing any face value and the minimum number of dice that the
player believes are showing that value, under all of the cups in the game. Ones are often wild, always counting as the
face of the current bid.

Turns rotate among the players in a clockwise order. Each player has two choices during their turn: to make a higher
bid, or challenge the previous bid—typically with a call of "liar". Raising the bid means either increasing the
quantity, or the face value, or both, according to the specific bidding rules used. There are many variants of allowed
and disallowed bids; common bidding variants, given a previous bid of an arbitrary quantity and face value, include:
    - The player may bid a higher quantity of any particular face, or the same quantity of a higher face
        (allowing a player to "re-assert" a face value they believe prevalent if another player increased the face
        value on their bid);
    - The player may bid a higher quantity of the same face, or any particular quantity of a higher face
        (allowing a player to "reset" the quantity);
    - The player may bid a higher quantity of the same face or the same quantity of a higher face
        (the most restrictive; a reduction in either face value or quantity is usually not allowed).

If the current player challenges the previous bid, all dice are revealed. If the bid is valid (at least as many of the
face value and any wild aces are showing as were bid), the bidder wins. Otherwise, the challenger wins. The player who
loses a round loses one of their dice. The last player to still retain a die (or dice) is the winner. The loser of the
last round starts the bidding on the next round. If the loser of the last round was eliminated, the next player starts
the new round.

Authors Note: We will utilize rule variant 2 for now.
"""

"""
Program execution:
1. Start program, accepts Player's Name for the game.
2. Set the number of CPU players to join (2 - 4).
3. Start the game:
    i. Per round the players will:
        1. Examine their dice. 
            i. This will be done automatically at the start of the round.
        3. Make a bid or call previous bid a lie.
            i. To make a bid, players will be asked to enter their bid in the following format:
                1. Enter the dice face you will bid on.
                2. Enter the number of dice.
                3. A bid must follow variant 2 rules, meaning the prvious bid should be tracked.
"""


def main():
    print(TITLE)
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
