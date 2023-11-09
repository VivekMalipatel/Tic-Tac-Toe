import sys

def get_and_validate_input(args):
    # Check if the number of arguments is correct
    if len(args) != 4: 
        return None, "ERROR: Not enough/too many input arguments."

    # Extract arguments
    _, ALGO, FIRST, MODE = args

    # Validate ALGO,FIRST,MODE
    if ALGO not in ['1', '2'] or FIRST not in ['X', 'O'] or MODE not in ['1', '2']:
        return None, "ERROR: illegal input arguments."

    return {
        'ALGO': ALGO,
        'FIRST': FIRST,
        'MODE': MODE
    }, None

# Initial Information Display
def display_game_info(parsed_args):
    algo_mapping = {
        '1': 'Min-Max',
        '2': 'Min-Max with alpha-beta pruning'
    }

    mode_mapping = {
        '1': 'human versus computer',
        '2': 'computer versus computer'
    }

    print(f"Malipatel, Vivekanand Reddy, A20524971 solution:")
    print(f"Algorithm: {algo_mapping[parsed_args['ALGO']]}")
    print(f"First: {parsed_args['FIRST']}")
    print(f"Mode: {mode_mapping[parsed_args['MODE']]}")
    print("\n")

#Game Implementation
class TicTacToe:

    #Initialising global variables
    def __init__(self, starting_player='X'):
        #List Structure to Store the board
        self.board = [' '] * 9
        #Varibale to store the current player
        self.current_player = starting_player
        #Variable to count the number of nodes generated
        self.nodes_explored = 0

    def display_board(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} ")
            if i < 6:
                print("---+---+---")
        print("\n")

    def available_moves(self):
        return [i+1 for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position, player):
        self.board[position - 1] = player

    def get_human_move(self):
        moves = self.available_moves()
        move = ''
        while move not in moves:
            move = int(input(f"{self.current_player}’s move. What is your move (possible moves at the moment are: {', '.join(map(str, moves))} | enter 0 to exit the game)? "))
            if move == 0:
                print("Exiting the game.")
                sys.exit(0)
            elif move not in moves:
                print("Invalid move.")
        return move

    def play_human_turn(self):
        self.display_board()
        move = self.get_human_move()
        self.make_move(move, self.current_player)
        self.display_board()

    #Deciding the winner with predefined winning combinations
    def is_winner(self, player):
    
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == player and self.board[combo[1]] == player and self.board[combo[2]] == player:
                return True
        return False

    def is_tie(self):
        return ' ' not in self.board
    
    #Min-Max Algorithm implementation
    def minimax(self, depth, is_maximizing):
        self.nodes_explored += 1
        if self.is_winner('X'):
            return -10 + depth
        if self.is_winner('O'):
            return 10 - depth
        if not self.available_moves():  # Tie
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for move in self.available_moves():
                self.board[move - 1] = 'O'
                eval = self.minimax(depth + 1, False)
                self.board[move - 1] = ' '  # Reset the board
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.board[move - 1] = 'X'
                eval = self.minimax(depth + 1, True)
                self.board[move - 1] = ' '  # Reset the board
                min_eval = min(min_eval, eval)
            return min_eval

    #Min-Max with alpha-beta pruning Algorithm implementation
    def minimax_alpha_beta(self, depth, is_maximizing, alpha, beta):
        self.nodes_explored += 1
        if self.is_winner('X'):
            return -10 + depth
        if self.is_winner('O'):
            return 10 - depth
        if not self.available_moves():  # Tie
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for move in self.available_moves():
                self.board[move - 1] = 'O'
                eval = self.minimax_alpha_beta(depth + 1, False, alpha, beta)
                self.board[move - 1] = ' '  # Reset the board to current state
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval

        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.board[move - 1] = 'X'
                eval = self.minimax_alpha_beta(depth + 1, True, alpha, beta)
                self.board[move - 1] = ' '  # Reset the board to current state
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def play_computer_turn(self, algo):
        self.nodes_explored = 0  # Reset nodes generated for each turn
        best_score = float('-inf') if self.current_player == 'O' else float('inf')
        best_move = None
        
        for move in self.available_moves():
            self.board[move - 1] = self.current_player
            if self.current_player == 'O':
                if algo == '1':  # Min-Max
                    score = self.minimax(0, False)
                else:  # Min-Max with alpha-beta pruning
                    score = self.minimax_alpha_beta(0, False, float('-inf'), float('inf'))
                if score > best_score:
                    best_score = score
                    best_move = move
            else:
                if algo == '1':  # Min-Max
                    score = self.minimax(0, True)
                else:  # Min-Max with alpha-beta pruning
                    score = self.minimax_alpha_beta(0, True, float('-inf'), float('inf'))
                if score < best_score:
                    best_score = score
                    best_move = move
            self.board[move - 1] = ' '  # Reset the board to current state after testing the move
            
        self.make_move(best_move, self.current_player)
        print(f"{self.current_player}'s selected move: {best_move}. Number of search tree nodes generated: {self.nodes_explored}")
        self.display_board()

    def play_game(self, algo, mode):
        while True:
            if self.current_player == 'X':
                if mode == '1':  # human vs computer
                    self.play_human_turn()
                else:  # computer vs computer
                    self.play_computer_turn(algo)
                if self.is_winner('X'):
                    print("X WON")
                    return
                elif self.is_tie():
                    print("TIE")
                    return
                self.current_player = 'O'
            else:
                self.play_computer_turn(algo)
                if self.is_winner('O'):
                    print("O WON")
                    return
                elif self.is_tie():
                    print("TIE")
                    return
                self.current_player = 'X'

#Main Method

#Validate Inputs
parsed_args, error = get_and_validate_input(sys.argv)
if error:
    print(error)
    sys.exit(1)

#Display Initial Info
display_game_info(parsed_args)

# Initialize and play the TicTacToe 
game = TicTacToe(parsed_args['FIRST'])

game.play_game(parsed_args['ALGO'],parsed_args['MODE'])