import pygame
from pygame import draw
import numpy as np

# Tenho que alterar isto porque estou sem acesso às var locais...
# para já vamos começar no Start Menu e enquanto não adicionar as outras funcionalidades
# não altero esta feature... Depois logo se vê


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w = self.game.DISPLAY_W/2
        self.mid_h = self.game.DISPLAY_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text('>', 20, self.cursor_rect.x,
                            self.cursor_rect.y, self.game.col_cursor)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.startx, self.starty = self.mid_w, self.mid_h - 20
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 20
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.col_background)
            self.game.draw_text(
                'Main Menu', 20, self.game.DISPLAY_W/2, 20, self.game.col_text)
            self.game.draw_text('Start', 20, self.startx,
                                self.starty, self.game.col_text)
            self.game.draw_text('Colors', 20, self.optionsx,
                                self.optionsy, self.game.col_text)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY or self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.curr_menu = self.game.start
            elif self.state == 'Options':
                self.game.curr_menu = self.game.colors
        self.run_display = False


class ColorsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Text'
        self.color = False
        self.state_col = 'White'
        self.blockSize = 120
        self.txtx, self.txty = self.mid_w, self.mid_h - 60
        self.blockx, self.blocky = self.mid_w, self.mid_h - 30
        self.cx, self.cy = self.mid_w, self.mid_h
        self.tlx, self.tly = self.mid_w, self.mid_h + 30
        self.backx, self.backy = self.mid_w, self.mid_h + 60
        self.gridx, self.gridy = self.mid_w + 200, self.mid_h - 120
        self.whitex, self.whitey = self.mid_w - 200, self.mid_h - 60
        self.blackx, self.blacky = self.mid_w - 200, self.mid_h - 30
        self.redx, self.redy = self.mid_w - 200, self.mid_h
        self.greenx, self.greeny = self.mid_w - 200, self.mid_h + 30
        self.bluex, self.bluey = self.mid_w - 200, self.mid_h + 60
        self.cursor_rect.midtop = (self.txtx + self.offset, self.txty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.col_background)
            self.game.draw_text(
                'Colors', 20, self.game.DISPLAY_W/2, 20, self.game.col_text)
            self.game.draw_text('Text', 20,
                                self.txtx, self.txty, self.game.col_text)
            self.game.draw_text(
                'Block', 20, self.blockx, self.blocky, self.game.col_text)
            self.game.draw_text(
                'Cursor', 20, self.cx, self.cy, self.game.col_text)
            self.game.draw_text(
                'Table lines', 20, self.tlx, self.tly, self.game.col_text)
            self.game.draw_text(
                'Background', 20, self.backx, self.backy, self.game.col_text)
            self.game.draw_text(
                'White', 20, self.whitex, self.whitey, self.game.WHITE)
            self.game.draw_text(
                'Black', 20, self.blackx, self.blacky, self.game.BLACK)
            self.game.draw_text(
                'Red', 20, self.redx, self.redy, self.game.RED)
            self.game.draw_text(
                'Green', 20, self.greenx, self.greeny, self.game.GREEN)
            self.game.draw_text(
                'Blue', 20, self.bluex, self.bluey, self.game.BLUE)
            self.draw_cursor()
            self.drawGrid()
            self.draw_block()
            self.blit_screen()

    def drawGrid(self):
        for i in range(2):
            for j in range(2):
                rect = pygame.Rect(
                    self.gridx + j*self.blockSize, self.gridy + i*self.blockSize, self.blockSize, self.blockSize)
                if (self.game.matrix[i][j] == 0):
                    pygame.draw.rect(self.game.display,
                                     self.game.col_grid, rect, 1)
                else:
                    pygame.Surface.fill(self.game.display,
                                        self.game.col_grid, rect, 1)

    def draw_block(self):
        rect = pygame.Rect(self.gridx, self.gridy,
                           self.blockSize, self.blockSize)
        pygame.Surface.fill(self.game.display, self.game.col_block, rect, 1)

    def check_input(self):
        if self.color:
            self.move_color()
            self.change_color()
        else:
            self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.mainmenu
            self.run_display = False
        elif self.game.START_KEY:
            if self.color:
                self.color = False
                self.cursor_rect.midtop = (
                    self.txtx + self.offset, self.txty)
                self.state = 'Text'
            else:
                self.color = True
                self.cursor_rect.midtop = (
                    self.whitex + self.offset, self.whitey)
                self.state_col = 'White'

    def change_color(self):
        color = self.chose_color()
        if self.state == 'Text':
            self.game.col_text = color
        elif self.state == 'Block':
            self.game.col_block = color
        elif self.state == 'Cursor':
            self.game.col_cursor = color
        elif self.state == 'Table':
            self.game.col_grid = color
        elif self.state == 'Back':
            self.game.col_background = color

    def chose_color(self):
        if self.state_col == 'White':
            return self.game.WHITE
        elif self.state_col == 'Black':
            return self.game.BLACK
        elif self.state_col == 'Red':
            return self.game.RED
        elif self.state_col == 'Green':
            return self.game.GREEN
        elif self.state_col == 'Blue':
            return self.game.BLUE

    def move_color(self):
        if self.game.DOWN_KEY:
            if self.state_col == 'White':
                self.cursor_rect.midtop = (
                    self.blackx + self.offset, self.blacky)
                self.state_col = 'Black'
            elif self.state_col == 'Black':
                self.cursor_rect.midtop = (
                    self.redx + self.offset, self.redy)
                self.state_col = 'Red'
            elif self.state_col == 'Red':
                self.cursor_rect.midtop = (
                    self.greenx + self.offset, self.greeny)
                self.state_col = 'Green'
            elif self.state_col == 'Green':
                self.cursor_rect.midtop = (
                    self.bluex + self.offset, self.bluey)
                self.state_col = 'Blue'
            elif self.state_col == 'Blue':
                self.cursor_rect.midtop = (
                    self.whitex + self.offset, self.whitey)
                self.state_col = 'White'
        if self.game.UP_KEY:
            if self.state_col == 'Blue':
                self.cursor_rect.midtop = (
                    self.greenx + self.offset, self.greeny)
                self.state_col = 'Green'
            elif self.state_col == 'Green':
                self.cursor_rect.midtop = (
                    self.redx + self.offset, self.redy)
                self.state_col = 'Red'
            elif self.state_col == 'Red':
                self.cursor_rect.midtop = (
                    self.blackx + self.offset, self.blacky)
                self.state_col = 'Black'
            elif self.state_col == 'Black':
                self.cursor_rect.midtop = (
                    self.whitex + self.offset, self.whitey)
                self.state_col = 'White'
            elif self.state_col == 'White':
                self.cursor_rect.midtop = (
                    self.bluex + self.offset, self.bluey)
                self.state_col = 'Blue'

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Text':
                self.cursor_rect.midtop = (
                    self.blockx + self.offset, self.blocky)
                self.state = 'Block'
            elif self.state == 'Block':
                self.cursor_rect.midtop = (
                    self.cx + self.offset, self.cy)
                self.state = 'Cursor'
            elif self.state == 'Cursor':
                self.cursor_rect.midtop = (
                    self.tlx + self.offset, self.tly)
                self.state = 'Table'
            elif self.state == 'Table':
                self.cursor_rect.midtop = (
                    self.backx + self.offset, self.backy)
                self.state = 'Back'
            elif self.state == 'Back':
                self.cursor_rect.midtop = (
                    self.txtx + self.offset, self.txty)
                self.state = 'Text'
        if self.game.UP_KEY:
            if self.state == 'Back':
                self.cursor_rect.midtop = (
                    self.tlx + self.offset, self.tly)
                self.state = 'Table'
            elif self.state == 'Table':
                self.cursor_rect.midtop = (
                    self.cx + self.offset, self.cy)
                self.state = 'Cursor'
            elif self.state == 'Cursor':
                self.cursor_rect.midtop = (
                    self.blockx + self.offset, self.blocky)
                self.state = 'Block'
            elif self.state == 'Block':
                self.cursor_rect.midtop = (
                    self.txtx + self.offset, self.txty)
                self.state = 'Text'
            elif self.state == 'Text':
                self.cursor_rect.midtop = (
                    self.backx + self.offset, self.backy)
                self.state = 'Back'


class StartMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Height'
        self.hx, self.hy = 120, self.mid_h - 60
        self.wx, self.wy = 120, self.mid_h
        self.genx, self.geny = 120, self.mid_h + 60
        self.gridx, self.gridy = (self.game.DISPLAY_W - self.game.k) // 2, 100
        self.cursor_rect.midtop = (self.hx - 50, self.hy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.blockH = self.game.k // self.game.matrixH
            self.game.blockW = self.game.k // self.game.matrixW
            if not(self.state == 'Grid'):
                self.game.matrix = np.random.randint(
                    1, size=(self.game.matrixH, self.game.matrixW))
            self.game.newmatrix = self.game.matrix
            self.game.display.fill(self.game.col_background)
            self.game.draw_text(
                'Start Menu', 20, self.game.DISPLAY_W/2, 20, self.game.col_text)
            self.game.draw_text('Height', 20, self.hx,
                                self.hy, self.game.col_text)
            self.game.draw_text(str(self.game.matrixH),
                                20, self.hx + 50, self.hy, self.game.col_text)
            self.game.draw_text('Width', 20, self.wx,
                                self.wy, self.game.col_text)
            self.game.draw_text(str(self.game.matrixW),
                                20, self.hx + 50, self.wy, self.game.col_text)
            self.game.draw_text('Lives', 20, self.genx,
                                self.geny, self.game.col_text)
            if (self.game.gen == 0):
                self.game.draw_text('Infnity', 20,
                                    self.hx + 70, self.geny, self.game.col_text)
            else:
                self.game.draw_text(str(self.game.gen), 20,
                                    self.hx + 50, self.geny, self.game.col_text)
            self.drawGrid()
            if (self.state == 'Grid'):
                self.draw_block()
            else:
                self.draw_cursor()
            self.blit_screen()

    def drawGrid(self):
        for i in range(self.game.matrixH):
            for j in range(self.game.matrixW):
                rect = pygame.Rect(
                    self.gridx + j*self.game.blockW, self.gridy + i*self.game.blockH, self.game.blockW, self.game.blockH)
                if (self.game.matrix[i][j] == 0):
                    pygame.draw.rect(self.game.display,
                                     self.game.col_grid, rect, 1)
                else:
                    pygame.Surface.fill(self.game.display,
                                        self.game.col_grid, rect, 1)

    def draw_block(self):
        rect = pygame.Rect(self.gridx + self.game.blockx*self.game.blockW,
                           self.gridy + self.game.blocky*self.game.blockH, self.game.blockW, self.game.blockH)
        pygame.Surface.fill(self.game.display, self.game.col_block, rect, 1)

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Height':
                self.cursor_rect.midtop = (
                    self.wx - 50, self.wy)
                self.state = 'Width'
            elif self.state == 'Width':
                self.cursor_rect.midtop = (
                    self.genx - 50, self.geny)
                self.state = 'Generations'
            elif self.state == 'Generations':
                self.cursor_rect.midtop = (
                    self.hx - 50, self.hy)
                self.state = 'Height'
        if self.game.UP_KEY:
            if self.state == 'Height':
                self.cursor_rect.midtop = (
                    self.genx - 50, self.geny)
                self.state = 'Generations'
            elif self.state == 'Width':
                self.cursor_rect.midtop = (
                    self.hx - 50, self.hy)
                self.state = 'Height'
            elif self.state == 'Generations':
                self.cursor_rect.midtop = (
                    self.wx - 50, self.wy)
                self.state = 'Width'

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.mainmenu
            self.run_display = False
        elif self.game.START_KEY:
            if not(self.state == 'Grid'):
                self.game.blockx, self.game.blocky = 0, 0
                self.state = 'Grid'
            elif self.state == 'Grid':
                self.game.playing = True
                self.run_display = False
        elif self.game.RIGHT_KEY:
            if self.state != 'Grid':
                if self.state == 'Height':
                    self.game.matrixH += 1
                elif self.state == 'Width':
                    self.game.matrixW += 1
                elif self.state == 'Generations':
                    self.game.gen += 1
            elif self.game.blockx < self.game.matrixW - 1:
                self.game.blockx += 1
        elif self.game.LEFT_KEY:
            if self.state != 'Grid':
                if self.state == 'Height':
                    if self.game.matrixH > 5:
                        self.game.matrixH -= 1
                elif self.state == 'Width':
                    if self.game.matrixW > 5:
                        self.game.matrixW -= 1
                elif self.state == 'Generations':
                    if self.game.gen > 0:
                        self.game.gen -= 1
            elif self.game.blockx > 0:
                self.game.blockx -= 1
        elif self.game.UP_KEY:
            if self.game.blocky > 0:
                self.game.blocky -= 1
        elif self.game.DOWN_KEY:
            if self.game.blocky < self.game.matrixH - 1:
                self.game.blocky += 1
        elif self.game.SPACE_KEY:
            if self.state == 'Grid':
                if self.game.matrix[self.game.blocky][self.game.blockx] == 0:
                    self.game.matrix[self.game.blocky][self.game.blockx] = 1
                else:
                    self.game.matrix[self.game.blocky][self.game.blockx] = 0
