class SquareChecking:

    def get_all_empty_squares(self, board):
        empty_squares = []
        squares = board.squares
        for key in squares:
            if squares[key].mark == '-':
                empty_squares.append(squares[key])
        return empty_squares
