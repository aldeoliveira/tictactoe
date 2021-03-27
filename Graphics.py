import pygame
from tictactoe import Dimensions


class Graphics:
    """
    Classe responsável pelos desenhos.
    """

    width = Dimensions.WIDTH
    height = Dimensions.HEIGHT
    sq_size = Dimensions.SQ_SIZE
    line_width = Dimensions.LINE_WIDTH
    dimension = Dimensions.DIMENSION
    x_size = Dimensions.X_SIZE
    o_size = Dimensions.O_SIZE
    mark_width = Dimensions.MARK_WIDTH

    def draw_gamestate(self, screen, current_gamestate):  # Atualiza os recursos gráficos
        self.draw_board(screen)
        self.draw_lines(screen)
        self.draw_marks(screen, current_gamestate)

    def draw_board(self, screen):  # Desenha o tabuleiro. Recebe a superfície em que será desenhado o tabuleiro
        board_color = pygame.Color("#646464")
        pygame.draw.rect(screen, board_color, pygame.Rect(0, 0, self.width, self.height))

    def draw_lines(self, screen):  # Desenha as linhas. Recebe a superfície em que serão desenhadas as linhas
        vertical_left = ((self.sq_size, 0), (self.sq_size, self.height))
        vertical_right = ((self.sq_size * 2, 0), (self.sq_size * 2, self.height))
        horizontal_top = ((0, self.sq_size), (self.width, self.sq_size))
        horizontal_bottom = ((0, self.sq_size * 2), (self.width, self.sq_size * 2))
        points_lines = [
            vertical_left,
            vertical_right,
            horizontal_top,
            horizontal_bottom
        ]  # Pontos de início e fim das quatro linhas do tabuleiro.
        for points in points_lines:
            pygame.draw.lines(screen, pygame.Color("White"), 1, points, self.line_width)

    def draw_marks(self, screen, current_gamestate):  # Localiza onde devem ser colocadas as marcas
        half_square_size = self.sq_size // 2
        for row in range(self.dimension):
            for col in range(self.dimension):
                col_dimension = self.sq_size * col
                row_dimension = self.sq_size * row
                center = (col_dimension + half_square_size, row_dimension + half_square_size)
                if current_gamestate.board[row][col] == 'x':
                    self.draw_an_x(screen, center)
                elif current_gamestate.board[row][col] == 'o':
                    self.draw_an_o(screen, center)

    def draw_an_x(self, screen, center):  # Desenha um 'x'
        half_x_size = self.x_size // 2
        center_horizontal = center[0]
        center_vertical = center[1]
        point_superior_left = (center_horizontal - half_x_size, center_vertical - half_x_size)
        point_superior_right = (center_horizontal - half_x_size, center_vertical + half_x_size)
        point_inferior_right = (center_horizontal + half_x_size, center_vertical + half_x_size)
        point_inferior_left = (center_horizontal + half_x_size, center_vertical - half_x_size)
        points_x = [
            (point_superior_left, point_inferior_right),
            (point_inferior_left, point_superior_right)
        ]
        for points in points_x:
            pygame.draw.lines(screen, pygame.Color("Red"), 1, points, self.mark_width)

    def draw_an_o(self, screen, center):  # Desenha um 'o'
        pygame.draw.circle(screen, pygame.Color("White"), center, self.o_size, self.mark_width)
