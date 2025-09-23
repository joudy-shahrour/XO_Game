import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # clean screan in windows 'cls' 

class player:
    '''
    to store player's data.
    '''
    def __init__(self):
        self.name=''
        self.symbol=''
    
    def choose_name(self):
        '''
        in this method every player enter his name.
        '''
        while True:
            name=input('Enter your name, should be letters only: ')
            if name.isalpha(): # name only contain letters.
                self.name=name
                break
            print('Invalid name. please try again: ') # if name not only letters.
    
    def choose_symbol(self):
        '''
        in this method every player enter his symbol.
        '''
        while True:
            symbol=input('Choose "X" or "O": ').lower()
            if symbol=='x' or symbol=='o':
                self.symbol=symbol
                break
            print('Invalid symbol. please try again: ')

class Menu:
    '''
    It contains a menu like interface for the start and end of the game.
    '''
    def display_main_menu(self):
        messag_input='''
please choose what do you want:
1- Start Game
2- End Game
Your choice is (1 or 2): 
'''
        choice=input(messag_input).strip()
        return choice
    
    def display_endgame_menu(self):
        messag_input='''
geme is end, please choose what do you want:
1- Restart Game
2- End Game
Your choice is (1 or 2): 
'''        
        choice=input(messag_input).strip()
        return choice

class Board:

    def __init__(self):
        self.board=[str(i) for i in range(1, 10)] # initiate the board

    def display_board(self): # to display board at form play (x, o) 
        for i in range(0, 9, 3):
            print(' | '.join(self.board[i:i+3]))
            if i<6:
                print('-'*9)

    def update_board(self, choice, symbol): #update the board after playing.
        # if self.board[choice-1]!='x' and self.board[choice-1]!='o':
        if self.board[choice-1].isdigit(): # cell must be empty.
            self.board[choice-1]=symbol
            return True
        else:
            print('this cell is not empty')
            return False

    def reset_board(self): # to reset the board.
        self.board=[str(i) for i in range(1, 10)]

class Game:

    def __init__(self):    
        self.board_ob=Board()
        self.players=[player(), player()]
        self.menu=Menu()
        self.current_player=0 # player's turn.

    def start_game(self):
        choice=self.menu.display_main_menu()
        if choice=='1': # if chioce is start game:
            self.setup_players() # every player enter his data.
            self.play_game() # start game
        else: # if choice is end game.
            self.end_game() 

    def play_game(self):
        while True:
            self.play_turn() # Each player plays and the role is switched.
            if self.win() or self.draw():
                choice=self.menu.display_endgame_menu() 
                if choice == '1': # if choice is restart game.
                    self.restart_game()
                else: # if choice is end game.
                    self.end_game()
                    break # end game.

    def play_turn(self):
        player=self.players[self.current_player] 
        self.board_ob.display_board()
        print(f'{player.name}\'s turn ({player.symbol})')
        while True:
            try:
                cell=int(input('choose cell (1-9): '))
                if 1<= cell <= 9 and self.board_ob.update_board(cell, player.symbol):
                    clear_screen()
                    break
                else: raise ValueError # if cell not in (1-9)
            except ValueError:
                print('Invalid choice, please choose number from (1-9)')
        self.switch_player()

    def switch_player(self):
        self.current_player = 1-self.current_player # current player= 1-0=1 (The second player's turn) 
                                                    #or current player= 1-0=1 (The first player's turn) 

    def win(self):
        wins=[ # wins possibilities
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
            [0, 4, 8], [2, 4, 6]             # Diameters
        ]
        for combo in wins:
            a, b, c=combo
            if self.board_ob.board[a] == self.board_ob.board[b] == self.board_ob.board[c]:
                win_symbol=self.board_ob.board[a]
                for i in self.players:
                    if win_symbol == i.symbol:
                        win_name=i.name
                print(f'Congrats {win_name} you are win!')
                return True
        return False

    def draw(self):
        sum=0
        for i in self.board_ob.board:
            if not i.isdigit():
                sum+=1
            if sum == len(self.board_ob.board):
                print('Ops! it\'s a Draw.')
                return True

    def restart_game(self):
        self.board_ob.reset_board()
        self.current_player=0
        self.play_game()

    def end_game(self):
        print('Thank you for playing!')

    def setup_players(self):
        for num ,player in enumerate(self.players, start=1):
            print(f'player number {num}: ')
            player.choose_name()
            player.choose_symbol()
            clear_screen()
        
game=Game()
game.start_game()
