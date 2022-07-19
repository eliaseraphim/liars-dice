# author: elia deppe
# email: elia.deppe7@gmail.com
# filename: game.py

from player import Player
from random import shuffle

AFFIRMATIVES = ['y', 'yes']
NEGATIVES = ['n', 'no']


class Game:
    def __init__(self):
        self.num_players = self.__set_num_players()
        self.players = self.__create_players()
        self.total_dice = self.num_players * 5

    @staticmethod
    def __set_num_players():
        """
        set the number of cpu players for the game. can be set to any amount between [2, 4]
        :return: num_players / int / the number of players
        """
        num_players = None
        while True:
            if num_players is None:
                print(
                    'Please enter the number of computer players.',
                    'The minimum number of computer players is 2, the maximum is 4.',
                    sep='\n'
                )

                # catch possible ValueError from user entering an invalid response
                try:
                    num_players = int(input('>> '))
                except ValueError:
                    num_players = None  # set to None to avoid triggering the second step
                    print('Invalid option for number of computer players. Please enter a number between 2 and 4.')

            if num_players is not None:
                print('Number of computer players:', num_players, '\nIs this correct?')
                response = input('>> ')

                if response in AFFIRMATIVES:
                    return num_players
                elif response in NEGATIVES:
                    num_players = None
                else:
                    print('Incorrect response, resetting...')

                print(end='\n\n')

    def __create_players(self):
        """
        create the players for the game
        :return: players / [Player] / list of players for the game
        """
        players = []

        for i in range(self.num_players + 1):
            if i != 0:  # create cpu players
                players.append(Player())
            else:  # create user player
                players.append(Player(cpu=False))

        shuffle(players)
        return players

    def play(self):
        """
        main game loop
        :return: None
        """
        game_over = False
        while not game_over:
            current_bet = {}  # set current bet to be empty at start of round
            round_over = False

            # roll dice for all players
            for player in self.players:
                player.roll_dice()

            print(f'Current number of dice in play: {self.total_dice}')

            # begin round
            while not round_over:
                # get the current player, and determine their action: bet or call
                current_player = self.players.pop()
                action = current_player.action()

                # if betting, make the bet, announce to other players, and move onto next player
                if action == 'bet':
                    current_bet = current_player.make_bet(current_bet)
                    self.announce_bet(current_player.get_name(), current_bet)
                # if calling, the round is over, and proceeds to deliberation
                else:  # action == 'call'
                    round_over = True

                self.players.append(current_player)

            self.determine_liar(current_bet)

            if len(self.players) == 1:
                game_over = True

    @staticmethod
    def announce_bet(player_name, bet):
        """
        print the player's bet to the console
        :param player_name: string / player's name
        :param bet: {"face": int, "count": int} / the player's bet to be announced
        :return: None
        """
        print(f'{player_name} makes the following bet: {bet["count"]} {bet["face"]}(s)')

    def determine_liar(self, bet):
        """
        determine who is the liar between the accused and the accuser
        :param bet: {"face": int, "count": int} / the player's bet to be tested
        :return: None
        """

        # establish the accuser and the accused
        accuser = self.players[-1] # the player who made the bet is appended to the end of the list
        accused = self.players[-2] # the accused is the player before the last player

        print(f'{accuser.get_name()} calls {accused.get_name()} a liar. Showing dice...')

        # show all dice to the players
        for player in self.players:
            print(player)

        # determine the outcome of the call
        liar = self.is_liar(bet)

        if liar:  # if the accuser is correct
            print(f'{accused.get_name()} lied. They lose one dice.')
            accused.lose_dice()

            if accused.get_num_dice() == 0:
                print(f'{accused.get_name()} is out of dice, and out of the game.')
                self.players.pop(-2)
        else:  # if the accuser is incorrect
            print(f'{accuser.get_name()} was incorrect. They lose one dice.')
            accuser.lose_dice()

            if accuser.get_num_dice() == 0:
                print(f'{accuser.get_name()} is out of dice, and out of the game.')
                self.players.pop(-1)

        self.total_dice -= 1

    def is_liar(self, bet):
        """
        determines if the last bet played is false according to the dice of the players
        :param bet: {"face": int, "count": int} / the player's bet to be tested
        :return: True if the bet is not over the current number of die with the given face, otherwise False
        """
        face = bet['face']
        bet_count = bet['count']
        count = 0

        for player in self.players:
            dice = player.get_dice()
            for die in dice:
                if die == face:
                    count += 1

        if bet_count > count:
            return True
        else:
            return False
