EMPTY = '-'


class GameState:
    def __init__(self):
        self.mark_log = []
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]
        self.x_to_play = True
        self.game_over = False

    def obtain_lines(self):
        top_row = self.board[0]
        mid_row = self.board[1]
        bottom_row = self.board[2]
        left_col = [self.board[0][0], self.board[1][0], self.board[2][0]]
        mid_col = [self.board[0][1], self.board[1][1], self.board[2][1]]
        right_col = [self.board[0][2], self.board[1][2], self.board[2][2]]
        top_left_diagonal = [self.board[0][0], self.board[1][1], self.board[2][2]]
        top_right_diagonal = [self.board[0][2], self.board[1][1], self.board[2][0]]
        return [top_row, mid_row, bottom_row, left_col, mid_col, right_col, top_left_diagonal, top_right_diagonal]

    def make_mark(self, mark):
        if not self.game_over and self.check_if_empty(mark):
            player_mark = 'o'
            if self.x_to_play:
                player_mark = 'x'
            self.board[mark.row][mark.col] = player_mark
            self.mark_log.append(mark)
            self.x_to_play = not self.x_to_play

    def undo_mark(self):
        if len(self.mark_log):
            last_mark = self.mark_log.pop()
            self.board[last_mark.row][last_mark.col] = EMPTY
            self.x_to_play = not self.x_to_play
        self.game_over = False

    def check_if_empty(self, mark):
        empty = False
        if self.board[mark.row][mark.col] == EMPTY:
            empty = True
        return empty

    def check_for_victory(self):
        if len(self.mark_log) < 5:
            return
        lines = self.obtain_lines()
        player_mark = 'x'
        if self.x_to_play:
            player_mark = 'o'
        for line in lines:
            if line.count(player_mark) == 3:
                print("VICTORY! " + str(player_mark) + " won")
                self.game_over = True
