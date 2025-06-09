def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")

def check_winner(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    return None

def is_board_full(board):
    return " " not in board

def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == " "]

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O": 
        return 1
    if winner == "X":  
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for cell in get_empty_cells(board):
            board[cell] = "O"
            score = minimax(board, depth + 1, False)
            board[cell] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for cell in get_empty_cells(board):
            board[cell] = "X"
            score = minimax(board, depth + 1, True)
            board[cell] = " "
            best_score = min(score, best_score)
        return best_score

def get_ai_move(board):
    best_score = float('-inf')
    best_move = None
    
    for cell in get_empty_cells(board):
        board[cell] = "O"
        score = minimax(board, 0, False)
        board[cell] = " "
        
        if score > best_score:
            best_score = score
            best_move = cell
    
    return best_move

def main():
    board = [" " for _ in range(9)]
    print("Welcome to Tic Tac Toe vs AI!")
    print("You are X, AI is O")
    print("Enter a number (1-9) to make your move:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print()

    while True:
        print_board(board)
        print("\nYour turn (X)")
        
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9!")
        
        board[move] = "X"
        
        if check_winner(board):
            print_board(board)
            print("\nYou win!")
            break
            
        if is_board_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break
        
        # AI's turn
        print("\nAI's turn (O)")
        ai_move = get_ai_move(board)
        board[ai_move] = "O"
        
        if check_winner(board):
            print_board(board)
            print("\nAI wins!")
            break
            
        if is_board_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break

if __name__ == "__main__":
    main() 