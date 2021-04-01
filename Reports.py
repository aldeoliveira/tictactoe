class Reports:

    def print_squares(self, squares):
        names = []
        for square in squares:
            names.append(square.square_name)
        sorted_names = sorted(names)
        print(sorted_names)

    def print_squares_with_values(self, dict_squares_values):
        dict_print = {}
        for key in dict_squares_values:
            square_name = key.square_name
            dict_print[square_name] = dict_squares_values[key]
        print(dict_print)
