class Minimax:
    def __init__(self, board, ai_symbol='O', human_symbol='X'):
        self.board = board
        self.ai = ai_symbol
        self.human = human_symbol

    def check_winner(self):
        b = self.board.board
        n = len(b)
        m = len(b[0])

        # Check rows
        for i in range(n):
            symbol = b[i][0]
            if symbol != ' ' and all(b[i][j] == symbol for j in range(m)):
                return symbol

        # Check columns
        for j in range(m):
            symbol = b[0][j]
            if symbol != ' ' and all(b[i][j] == symbol for i in range(n)):
                return symbol

        # Check main diagonal
        symbol = b[0][0]
        if symbol != ' ' and all(b[i][i] == symbol for i in range(n)):
            return symbol

        # Check anti diagonal
        symbol = b[0][n-1]
        if symbol != ' ' and all(b[i][n-1-i] == symbol for i in range(n)):
            return symbol

        return None

    def is_draw(self):
        if self.check_winner() is not None:
            return False
        return self.board.is_full()

    def minimax(self, is_maximizing):
        winner = self.check_winner()
        if winner == self.ai:
            return 1
        elif winner == self.human:
            return -1
        elif self.is_draw():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in self.board.available_moves():
                self.board.make_move(move, self.ai)
                score = self.minimax(False)
                self.board.undo_move(move)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.board.available_moves():
                self.board.make_move(move, self.human)
                score = self.minimax(True)
                self.board.undo_move(move)
                best_score = min(best_score, score)
            return best_score

    def get_best_move(self):
        best_score = -float('inf')
        best_move = None
        for move in self.board.available_moves():
            self.board.make_move(move, self.ai)
            score = self.minimax(False)
            self.board.undo_move(move)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
