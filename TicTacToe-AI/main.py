from game_board import Board
from min_max import Minimax  # Assuming Minimax is implemented in min_max.py

def main():
    game_board = Board()
    minimax_solver = Minimax()

    human_symbol = 'X'
    bot_symbol = 'O'

    while True:
        game_board.print_board()

        # Human move
        try:
            pos = int(input("Enter move (0-8): "))
        except ValueError:
            print("Invalid Input. Please enter a number between 0 and 8.")
            continue

        if not game_board.is_valid_move(pos):
            print("Position already taken or invalid. Try again.")
            continue

        game_board.make_move(pos, human_symbol)

        winner = check_winner(game_board.board)
        if winner:
            game_board.print_board()
            print(f"Player '{winner}' wins!")
            break

        if game_board.is_full():
            game_board.print_board()
            print("It's a draw!")
            break

        # Bot move using minimax
        print("Bot Move:")
        bot_move = minimax_solver.get_best_move(game_board, bot_symbol)
        game_board.make_move(bot_move, bot_symbol)

        winner = check_winner(game_board.board)
        if winner:
            game_board.print_board()
            print(f"Player '{winner}' wins!")
            break

        if game_board.is_full():
            game_board.print_board()
            print("It's a draw!")
            break

def check_winner(board):
    n = len(board)
    m = len(board[0])

    # Check rows
    for i in range(n):
        symbol = board[i][0]
        if symbol != ' ' and all(board[i][j] == symbol for j in range(m)):
            return symbol

    # Check columns
    for j in range(m):
        symbol = board[0][j]
        if symbol != ' ' and all(board[i][j] == symbol for i in range(n)):
            return symbol

    # Check main diagonal
    symbol = board[0][0]
    if symbol != ' ' and all(board[i][i] == symbol for i in range(n)):
        return symbol

    # Check anti-diagonal
    symbol = board[0][n-1]
    if symbol != ' ' and all(board[i][n-1-i] == symbol for i in range(n)):
        return symbol

    return None

if __name__ == "__main__":
    main()
