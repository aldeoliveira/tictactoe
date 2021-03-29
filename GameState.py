from tictactoe import Board
from tictactoe import Dimensions


EMPTY = '-'
DIMENSION = Dimensions.DIMENSION


class GameState:

    board = None
    mark_log = []
    x_to_play = None
    game_over = None

    def __init__(self):
        self.board = Board.Board(DIMENSION)
        self.x_to_play = True
        self.game_over = False

    def make_mark(self, mark):
        if not self.game_over and self.check_if_empty(mark):
            player_mark = mark.symbol
            square_name = self.get_square_name(mark.row, mark.col)
            self.board.squares[square_name].mark = player_mark
            self.mark_log.append(mark)
            self.x_to_play = not self.x_to_play

    def get_square_name(self, row, col):
        square_name = "{}{}".format(row, col)
        return square_name

    def undo_mark(self):
        if len(self.mark_log):
            last_mark = self.mark_log.pop()
            square_name = self.get_square_name(last_mark.row, last_mark.col)
            self.board.squares[square_name].mark = EMPTY
            self.x_to_play = not self.x_to_play
            self.game_over = False

    def check_if_empty(self, mark):
        is_empty = False
        square_name = self.get_square_name(mark.row, mark.col)
        square = self.board.squares[square_name]
        if square.mark == EMPTY:
            is_empty = True
        return is_empty

    def check_for_victory(self):
        if len(self.mark_log) < 5:
            return
        lines = self.board.rows + self.board.columns + self.board.diagonals
        player_mark = 'x'
        if self.x_to_play:
            player_mark = 'o'
        for line in lines:
            marks_in_a_line = []
            for square in line:
                marks_in_a_line.append(square.mark)
            if marks_in_a_line.count(player_mark) == 3:
                print("VICTORY! " + str(player_mark) + " won")
                self.game_over = True
