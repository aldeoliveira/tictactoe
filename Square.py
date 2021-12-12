import Dimensions

EMPTY = Dimensions.EMPTY


class Square:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.mark = EMPTY
        self.square_name = "{}{}".format(r, c)

    def __repr__(self):
        return self.square_name
