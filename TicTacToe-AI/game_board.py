class Board:
    def __init__(self):
        # Initialize board with positions 0-8 for empty cells
        self.board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.seen = set()

    def print_board(self):
        for row in self.board:
            print('|'.join(str(cell) for cell in row))
            print('-' * 5)

    def make_move(self, pos, symbol):
        if self.is_valid_move(pos):
            self.seen.add(pos)
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.board[i][j] == pos:
                        self.board[i][j] = symbol
                        return True
        return False

    def is_valid_move(self, pos):
        return pos not in self.seen and 0 <= pos <= 8

    def available_moves(self):
        moves = []
        for row in self.board:
            for cell in row:
                if isinstance(cell, int) and cell not in self.seen:
                    moves.append(cell)
        return moves

    def is_full(self):
        return len(self.seen) == 9

    def reset(self):
        self.board = [[0,1,2],[3,4,5],[6,7,8]]
        self.seen.clear()

    def undo_move(self, pos):
        if pos in self.seen:
            self.seen.remove(pos)
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.board[i][j] == 'X' or self.board[i][j] == 'O':
                        continue
                    if isinstance(self.board[i][j], int) and self.board[i][j] == pos:
                        self.board[i][j] = pos
                        return True
        return False
