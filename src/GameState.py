from src import Board, LineChecking, Dimensions, SquareChecking

EMPTY = Dimensions.EMPTY
X_MARK = Dimensions.X_MARK
O_MARK = Dimensions.O_MARK
DIMENSION = Dimensions.DIMENSION


class GameState:

    def __init__(self):
        self.board = Board.Board(DIMENSION)
        self.mark_log = []
        self.x_to_play = True
        self.game_over = False
        self.winner = None

    def make_mark(self, mark):
        if not self.game_over and self.board.check_if_square_is_empty(mark.row, mark.col):
            self.board.change_mark_in_a_square(mark.row, mark.col, mark.symbol)
            self.mark_log.append(mark)
            self.x_to_play = not self.x_to_play

    def undo_mark(self):
        if len(self.mark_log):
            last_mark = self.mark_log.pop()
            self.board.change_mark_in_a_square(last_mark.row, last_mark.col, EMPTY)
            self.x_to_play = not self.x_to_play
            self.game_over = False

    def check_for_result(self):
        line_checking = LineChecking.LineChecking(self.board)
        square_checking = SquareChecking.SquareChecking(self.board)
        for symbol in [X_MARK, O_MARK]:
            if line_checking.check_for_win(symbol):
                print("VICTORY! " + str(symbol) + " won")
                self.game_over = True
                self.winner = symbol
        if not self.game_over and square_checking.check_for_draw():
            print("DRAW")
            self.game_over = True
