
class Mark:

    symbol = None
    row = None
    col = None

    def __init__(self, square_clicked, symbol):
        self.row = square_clicked[0]
        self.col = square_clicked[1]
        self.symbol = symbol
