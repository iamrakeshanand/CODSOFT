import math

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if there's a winner
def check_winner(board, player):
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_states

# Function to check for a draw
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to get the available moves
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

# Minimax function with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to find the best move for the AI
def find_best_move(board):
    best_move = None
    best_value = -math.inf
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        move_value = minimax(board, 0, False, -math.inf, math.inf)
        board[move[0]][move[1]] = ' '
        if move_value > best_value:
            best_move = move
            best_value = move_value
    return best_move

# Function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        
        if current_player == 'X':
            try:
                row, col = map(int, input("Enter your move (row and column): ").split())
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    if check_winner(board, 'X'):
                        print_board(board)
                        print("Congratulations! You win!")
                        break
                    current_player = 'O'
                else:
                    print("This cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers between 0 and 2.")
        else:
            move = find_best_move(board)
            if move:
                board[move[0]][move[1]] = 'O'
                if check_winner(board, 'O'):
                    print_board(board)
                    print("AI wins!")
                    break
                current_player = 'X'
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()
