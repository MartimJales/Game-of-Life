import pygame
from time import sleep
from menu import *

# Tenho que colocar comentáriosnesta desgraça antes de dormir


class Game():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.DISPLAY_W = 1340
        self.DISPLAY_H = 690
        self.matrixH = 3
        self.matrixW = 3
        self.gen = 0
        self.k = self.DISPLAY_H - 120
        self.blockH = self.k // self.matrixH
        self.blockW = self.k // self.matrixW
        self.blockx, self.blocky = 0, 0
        self.gridx, self.gridy = (self.DISPLAY_W - self.k) // 2, 100
        self.matrix = np.random.randint(1, size=(self.matrixH, self.matrixW))
        self.newmatrix = self.matrix
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.mainmenu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditMenu(self)
        self.start = StartMenu(self)
        self.grid = GridMenu(self)
        self.curr_menu = self.mainmenu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.drawGrid()
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.changeState()
            sleep(1)
            self.reset_keys()

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

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def neighbours(self, coordx, coordy):
        alive = 0
        for i in range(3):
            for j in range(3):
                if not(i == 1 and j == 1):
                    x = i - 1 + coordx
                    y = j - 1 + coordy
                    if (x >= 0 and x < self.matrixW and y >= 0 and y < self.matrixH):
                        neighbour = (x, y)
                        if self.matrix[x][y] == 1:
                            alive += 1
        return alive

    def changeState(self):
        for i in range(self.matrixH):
            for j in range(self.matrixW):
                neighborhood = self.neighbours(i, j)
                if (neighborhood == 3):
                    self.newmatrix[i][j] = 1
                elif (neighborhood == 2):
                    if self.matrix[i][j] == 1:
                        self.newmatrix[i][j] = 1
                else:
                    self.newmatrix[i][j] = 0
        self.matrix = self.newmatrix

    def drawGrid(self):
        for i in range(self.matrixW):
            for j in range(self.matrixH):
                rect = pygame.Rect(
                    self.gridx + i*self.blockW, self.gridy + j*self.blockH, self.blockW, self.blockH)
                if (self.matrix[j][i] == 0):
                    pygame.draw.rect(self.display,
                                     (255, 255, 255), rect, 1)
                else:
                    pygame.Surface.fill(self.display,
                                        (255, 0, 0), rect, 1)
