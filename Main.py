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

    current_gamestate = None
    graphic_resources = None

    width = Dimensions.WIDTH
    height = Dimensions.HEIGHT
    fps = Dimensions.FPS
    sq_size = Dimensions.SQ_SIZE

    def __init__(self):
        self.running = True
        self.current_gamestate = GameState.GameState()
        self.graphic_resources = Graphics.Graphics()

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(size=(self.width, self.height))  # Define largura e altura da tela
        screen.fill(pygame.Color("black"))  # Define a cor de fundo da tela
        while self.running:
            self.detect_player_inputs()
            self.graphic_resources.draw_gamestate(screen, self.current_gamestate)  # Faz os desenhos
            pygame.time.Clock().tick(self.fps)  # Faz o laço rodar um número limitado de vezes por segundo
            pygame.display.flip()  # Atualiza o tabuleiro a cada frame

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
        if not self.current_gamestate.game_over:
            mark = Mark.Mark(square_selected)
            if self.current_gamestate.check_if_empty(mark):
                self.current_gamestate.make_mark(mark)
            self.current_gamestate.check_for_victory()


old_main = OldMain()
old_main.main()
