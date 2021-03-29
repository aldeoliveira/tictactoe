import pygame
from tictactoe import Dimensions


WIDTH = Dimensions.WIDTH
HEIGHT = Dimensions.HEIGHT
SQ_SIZE = Dimensions.SQ_SIZE
LINE_WIDTH = Dimensions.LINE_WIDTH
DIMENSION = Dimensions.DIMENSION
X_SIZE = Dimensions.X_SIZE
O_SIZE = Dimensions.O_SIZE
MARK_WIDTH = Dimensions.MARK_WIDTH


class Graphics:
    """
    Classe responsável pelos desenhos.
    """

    def draw_gamestate(self, screen, gamestate):  # Atualiza os recursos gráficos
        self.draw_board(screen)
        self.draw_lines(screen)
        self.draw_marks(screen, gamestate)

    def draw_board(self, screen):  # Desenha o tabuleiro. Recebe a superfície em que será desenhado o tabuleiro
        board_color = pygame.Color("#646464")
        pygame.draw.rect(screen, board_color, pygame.Rect(0, 0, WIDTH, HEIGHT))

    def draw_lines(self, screen):
        points_lines = []
        for r in range(1, DIMENSION):
            points = ((SQ_SIZE * r, 0), (SQ_SIZE * r, HEIGHT))
            points_lines.append(points)
        for c in range(1, DIMENSION):
            points_lines.append(((0, SQ_SIZE * c), (WIDTH, SQ_SIZE * c)))
        for points in points_lines:
            pygame.draw.lines(screen, pygame.Color("White"), 1, points, LINE_WIDTH)

    def draw_marks(self, screen, gamestate):  # Localiza onde devem ser colocadas as marcas
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                square_name = gamestate.get_square_name(row, col)
                square = gamestate.board.squares[square_name]
                center = (SQ_SIZE * col + SQ_SIZE//2, SQ_SIZE * row + SQ_SIZE//2)
                if square.mark == 'x':
                    self.draw_an_x(screen, center)
                elif square.mark == 'o':
                    self.draw_an_o(screen, center)

    def draw_an_x(self, screen, center):  # Desenha um 'x'
        half_mark_size = X_SIZE // 2
        center_x_location = center[0]
        center_y_location = center[1]
        point_superior_left = (center_x_location - half_mark_size, center_y_location - half_mark_size)
        point_superior_right = (center_x_location - half_mark_size, center_y_location + half_mark_size)
        point_inferior_right = (center_x_location + half_mark_size, center_y_location + half_mark_size)
        point_inferior_left = (center_x_location + half_mark_size, center_y_location - half_mark_size)
        points_x = [
            (point_superior_left, point_inferior_right),
            (point_inferior_left, point_superior_right)
        ]
        for points in points_x:
            pygame.draw.lines(screen, pygame.Color("Red"), 1, points, MARK_WIDTH)

    def draw_an_o(self, screen, center):  # Desenha um 'o'
        pygame.draw.circle(screen, pygame.Color("White"), center, O_SIZE, MARK_WIDTH)
