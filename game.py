import pygame
from time import sleep
from menu import *


class Game():
    def __init__(self):
        pygame.init()
        self.running = True  # Correr o jogo no geral
        self.playing = False  # Correr o game_loop
        # Teclas que podemos utilizar
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.SPACE_KEY = False
        # Dimensões da janela
        self.DISPLAY_W = 1200
        self.DISPLAY_H = 690
        # Dimensões da matriz principal
        self.matrixH = 5
        self.matrixW = 5
        self.gen = 0  # Numero de gerações
        self.k = self.DISPLAY_H - 120  # Tamanho do lado da matriz
        # Dimensões de cada bloco da matriz
        self.blockH = self.k // self.matrixH
        self.blockW = self.k // self.matrixW
        self.blockx, self.blocky = 0, 0  # Coordendas do bloco onde o user está
        # Coordenadas da matriz (Canto sup esquerdo)
        self.gridx, self.gridy = (self.DISPLAY_W - self.k) // 2, 100
        # Gerar matriz (Parent)
        self.matrix = np.zeros((3, 3))
        # Gerar matriz (Child)
        self.newmatriz = self.matrix.copy()
        self.display = pygame.Surface(
            (self.DISPLAY_W, self.DISPLAY_H))      # Superficie do jogo
        self.window = pygame.display.set_mode(
            (self.DISPLAY_W, self.DISPLAY_H))  # Criação da janela
        self.font_name = pygame.font.get_default_font()  # Fonte do texto
        # Cores utilizadas
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        # Variáveis para aplicar as cores:
        self.col_grid = self.WHITE
        self.col_block = self.BLUE
        self.col_cursor = self.GREEN
        self.col_text = self.WHITE
        self.col_background = self.BLACK
        # Menus que o jogo contém
        self.mainmenu = MainMenu(self)
        self.colors = ColorsMenu(self)
        self.credits = CreditMenu(self)
        self.start = StartMenu(self)
        # Menu atual
        self.curr_menu = self.mainmenu

    def game_loop(self):
        self.newmatriz = self.matrix.copy()
        if self.gen == 0:
            __flag__ = -1
        else:
            __flag__ = self.gen
            self.gen = 0
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.col_background)
            self.drawGrid()
            self.draw_text('Generations: ' + str(self.gen),
                           20, self.DISPLAY_W/2, 20, self.col_text)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.changeState(self.matrix, self.newmatriz)
            self.matrix = self.newmatriz.copy()
            if (self.gen == __flag__):
                self.playing = False
                self.gen -= 1
            self.gen += 1
            sleep(1)
            self.reset_keys()

    def neighbours(self, ci, cj, matriz, nolimit):
        alive = 0
        # Este serve para verificar a vizinhança!!!
        for i in range(3):
            for j in range(3):
                if not(i == 1 and j == 1):
                    x = i + ci
                    y = j + cj
                    if (x >= 0 and x < self.matrixH + 2 and y >= 0 and y < self.matrixW + 2):
                        if (nolimit[x][y] == 1):
                            alive += 1
        return alive

    def changeState(self, matriz, newmatrix):
        nolimit = np.zeros((self.matrixH + 2, self.matrixW + 2), dtype=int)
       # Com estes 2 ciclos alcanço o mundo infinito
        for i in range(self.matrixH):
            for j in range(self.matrixW):
                if i == 0:
                    nolimit[i][j+1] = self.matrix[self.matrixH-1][j]
                if i == self.matrixH - 1:
                    nolimit[self.matrixH + 1][j+1] = self.matrix[0][j]
                nolimit[i+1][j+1] = self.matrix[i][j]
        for j in range(self.matrixH + 2):
            nolimit[j][0] = nolimit[j][self.matrixW]
            nolimit[j][self.matrixW + 1] = nolimit[j][1]
        for i in range(self.matrixH):
            for j in range(self.matrixW):
                neighborhood = self.neighbours(i, j, matriz, nolimit)
                if (neighborhood == 3):
                    newmatrix[i][j] = 1
                elif (neighborhood == 2):
                    if matriz[i][j] == 1:
                        newmatrix[i][j] = 1
                else:
                    newmatrix[i][j] = 0

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    if self.playing == True:
                        self.playing = False
                        self.gen = 0
                    else:
                        self.running = False
                        self.playing = False
                    self.curr_menu.run_display = False
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True

    def reset_keys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.RIGHT_KEY = False
        self.LEFT_KEY = False
        self.SPACE_KEY = False

    def draw_text(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def drawGrid(self):
        for i in range(self.matrixH):
            for j in range(self.matrixW):
                rect = pygame.Rect(
                    self.gridx + j*self.blockW, self.gridy + i*self.blockH, self.blockW, self.blockH)
                if (self.matrix[i][j] == 0):
                    pygame.draw.rect(self.display,
                                     self.col_grid, rect, 1)
                else:
                    pygame.Surface.fill(self.display,
                                        self.col_block, rect, 1)
