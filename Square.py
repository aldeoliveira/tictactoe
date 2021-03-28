class Square:
    row = None
    col = None
    mark = '-'
    square_name = None

    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.square_name = "{}{}".format(r, c)

    def __str__(self):
        return self.square_name

    def put_mark(self, mark):
        self.mark = mark
