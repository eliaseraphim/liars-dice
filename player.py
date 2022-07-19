# author: elia deppe
# email: elia.deppe7@gmail.com
# filename: player.py

from random import randrange

BEHAVIORS = []
AFFIRMATIVES = ['y', 'yes', 'c', 'confirm']
NEGATIVES = ['n', 'no']
BETS = ['b', 'bet', 'make bet']
CALLS = ['l', 'c', 'liar', 'call', 'call liar', 'call a liar', 'make call']


class Player:
    def __init__(self, cpu=True):
        if cpu:
            self.name = self.__random_name()
        else:
            self.name = self.__select_name()

        self.cpu = cpu
        self.num_dice = 5
        self.dice = []

    def __repr__(self):
        return f'Player(\'{self.name}\', cpu={self.cpu}, num_dice={self.num_dice}, dice={self.dice})'

    def __str__(self):
        return f'{self.name} - {self.dice}'

    @staticmethod
    def __select_name():
        """
        select the name for the player (user) of the game
        :return: name / string / the name of the player
        """
        name = None
        while True:
            if name is None:
                print('Please enter your name...')
                name = input('>> ')

            print('Your name is:', name, '\nIs this correct?')
            response = input('>> ').lower().strip()

            if response in AFFIRMATIVES:
                print(end='\n\n')
                return name
            elif response in NEGATIVES:
                name = None
            else:
                print('Incorrect response, resetting...')

            print()

    @staticmethod
    def __random_name():
        """
        select a random name from names.txt
        :return: name / string / a random name from names.txt
        """
        # utilizing reservoir sampling to avoid loading a large amount of data
        # https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file

        file = open('names.txt', 'r')

        name = next(file)
        for i, aname in enumerate(file, 2):
            if randrange(i):
                continue
            name = aname

        file.close()
        return name.strip()  # strip spaces / newlines before return

    def get_name(self):
        """
        get name of player
        :return: self.name / string / player's name
        """
        return self.name

    def get_cpu(self):
        """
        get the player status as user or cpu
        :return: self.cpu / boolean / True if user is a cpu, False otherwise
        """
        return self.cpu

    def get_num_dice(self):
        """
        get the current number of dice the player has in their possession
        :return: self.num_dice / int / the number of dice the player currently has in their possession.
        """
        return self.num_dice

    def get_dice(self):
        """
        get the current dice rolls of the player
        :return: self.dice.copy() / [int] / the current list of dice rolls for the player
        """
        return self.dice.copy()

    def roll_dice(self):
        for i in range(self.num_dice):
            self.dice.append(randrange(1, 7))

    def lose_dice(self):
        """
        remove one die from the player
        :return: None
        """
        self.num_dice -= 1

    def action(self):
        """
        determines whether or not to allow a cpu to make the action or the user
        :return:
        """
        if self.cpu:
            self.__cpu_action()
        else:
            self.__player_action()

    def __cpu_action(self):
        pass

    @staticmethod
    def __player_action():
        """
        player makes the decision to call or bet
        :return:
        """
        action_ = None
        valid_action = False
        while True:
            if action_ is None:
                print('Please select an action: Bet or Call')
                action_ = input('>> ')

            if action_ in BETS or action_ in CALLS:
                valid_action = True
            else:
                print('Invalid action. Please try again.')

            if valid_action:
                print('Your wish to', action_, '\nIs this correct?')
                response = input('>> ').lower().strip()

                if response in AFFIRMATIVES:
                    if action_ in BETS:
                        return 'bet'
                    else:
                        return 'call'
                elif response in NEGATIVES:
                    action_ = None
                    valid_action = False
                else:
                    print('Incorrect response, resetting...')

            print()

    def make_bet(self, bet):
        def cpu_make_bet():
            pass

        def player_make_bet():
            """
                        player makes their bet. a player's bet must follow rule set 1 for Liar's Dice:
                            - the player may bid a higher quantity of any particular face
                            - the player may bid same quantity of a higher face (allowing a player to "re-assert" a face
                                value they believe prevalent if another player increased the face value on their bid)
                        :return: new_bet / {"face": int, "count": int} / the new player's bet
            """
            def set_face():
                def face_warning():
                    print('Please enter a digit between 1 and 6.')

                while True:
                    try:
                        return int(input('>> Face: '))
                    except ValueError:
                        face_warning()

            def set_count():
                def count_warning_value_error():
                    print('Please enter some whole number using digits.')

                def count_warning():
                    print(
                        '- The player may bid a higher quantity of any particular face.',
                        '- The player may bid same quantity of a higher face.', sep='\n'
                    )
                    display_bets()

                while True:
                    try:
                        new_count = int(input('>> Count: '))
                        if new_count > bet['count']:
                            return new_count
                        elif new_count == bet['count']:
                            if face > bet['face']:
                                return new_count
                            else:
                                count_warning()
                        else:
                            count_warning()
                    except ValueError:
                        count_warning_value_error()

            def display_bets():
                print(f'Previous Bet | Face: {bet["face"]}, Count: {bet["count"]}')
                print(f'Your Bet | Face: {face}, Count: {count}', end='\n\n')

            while True:
                print('Please place your bet.')
                face = set_face()
                count = set_count()

                display_bets()
                bet_set = input('>> Confirm: ')

                if bet_set in AFFIRMATIVES:
                    return {'face': face, 'count': count}
                elif bet_set not in NEGATIVES:
                    print('Invalid option.')

        if self.cpu:
            cpu_make_bet()
        else:
            player_make_bet()
