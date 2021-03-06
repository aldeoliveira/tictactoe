import pygame
from tictactoe import GameState
from tictactoe import Mark
from tictactoe import NewelSimonMethod
from tictactoe import Dimensions
from tictactoe import Graphics

WIDTH = Dimensions.WIDTH
HEIGHT = Dimensions.HEIGHT
FPS = Dimensions.FPS
SQ_SIZE = Dimensions.SQ_SIZE

X_MARK = Dimensions.X_MARK
O_MARK = Dimensions.O_MARK


class OldMain:
    """
    Esta classe gerencia os inputs do usuário.
    """

    current_gamestate = None
    graphics = None
    screen = None
    running = None

    def main(self):
        pygame.init()
        self.set_screen()
        self.start_new_game()
        self.running = True
        self.graphics = Graphics.Graphics()
        while self.running:
            self.graphics.draw_gamestate(self.screen, self.current_gamestate)
            self.detect_player_inputs()
            pygame.time.Clock().tick(FPS)  # Faz o laço rodar um número limitado de vezes por segundo
            pygame.display.flip()  # Atualiza o display a cada frame

    def set_screen(self):
        self.screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))  # Define largura e altura da tela
        self.screen.fill(pygame.Color("black"))  # Define a cor de fundo da tela

    def detect_player_inputs(self):  # Reconhece os inputs do jogador
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z:
                    self.current_gamestate.undo_mark()
                if e.key == pygame.K_r:
                    self.start_new_game()
                if e.key == pygame.K_SPACE:
                    self.ask_ai()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                square_selected = self.locate_left_click()
                self.put_a_mark(square_selected)

    def start_new_game(self):  # Renova o gamestate para um novo jogo
        self.current_gamestate = GameState.GameState()

    def ask_ai(self):  # Obtem o melhor lance de acordo com a AI
        newel_simon = NewelSimonMethod.NewelSimonMethod(self.current_gamestate)
        if not self.current_gamestate.game_over:
            best_square = newel_simon.get_best_square()
            if best_square:
                square_selected = (best_square.row, best_square.col)
                self.put_a_mark(square_selected)

    def locate_left_click(self):  # Insere lances com o botão esquerdo do mouse
        location = pygame.mouse.get_pos()
        square_selected = (location[1] // SQ_SIZE, location[0] // SQ_SIZE)
        return square_selected

    def put_a_mark(self, square_selected):  # Insere um lance no gamestate
        game_over = self.current_gamestate.game_over
        if not game_over:
            symbol = 'x'
            if not self.current_gamestate.x_to_play:
                symbol = 'o'
            mark = Mark.Mark(square_selected, symbol)
            self.current_gamestate.make_mark(mark)
            self.current_gamestate.check_for_result()


old_main = OldMain()
old_main.main()
