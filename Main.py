import pygame
from tictactoe import GameState
from tictactoe import Mark
from tictactoe import BestMove
from tictactoe import Dimensions
from tictactoe import Graphics


class OldMain:
    """
    Esta classe gerencia os inputs do usuário.
    """

    width = Dimensions.WIDTH
    height = Dimensions.HEIGHT
    fps = Dimensions.FPS
    sq_size = Dimensions.SQ_SIZE

    current_gamestate = None
    graphics = None
    screen = None

    def __init__(self):
        self.running = True
        self.graphics = Graphics.Graphics()

    def main(self):
        pygame.init()
        self.set_screen()
        self.start_new_game()
        while self.running:
            self.graphics.draw_gamestate(self.screen, self.current_gamestate)
            self.detect_player_inputs()
            pygame.time.Clock().tick(self.fps)
            pygame.display.flip()

    def set_screen(self):
        self.screen = pygame.display.set_mode(size=(self.width, self.height))  # Define largura e altura da tela
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
                self.left_click()

    def start_new_game(self):  # Renova o gamestate para um novo jogo
        self.current_gamestate = GameState.GameState()

    def ask_ai(self):  # Obtem o melhor lance de acordo com a AI
        best_move = BestMove.BestMove(self.current_gamestate)
        chosen_move = best_move.chosen_move
        self.put_a_mark(chosen_move)

    def left_click(self):  # Insere lances com o botão esquerdo do mouse
        location = pygame.mouse.get_pos()
        square_selected = (location[1]//self.sq_size, location[0]//self.sq_size)
        self.put_a_mark(square_selected)

    def put_a_mark(self, square_selected):  # Insere um lance no gamestate
        mark = Mark.Mark(square_selected)
        self.current_gamestate.make_mark(mark)
        self.current_gamestate.check_for_victory()


old_main = OldMain()
old_main.main()
