EMPTY = '-'


class Square:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.mark = EMPTY
        self.square_name = "{}{}".format(r, c)

    """
        def __str__(self):
        return self.square_name
    """

    def put_mark(self, mark):
        self.mark = mark
