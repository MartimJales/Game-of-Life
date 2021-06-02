import pygame

from menu import *

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
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
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
            self.draw_text('Upcoming Game of Life!', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                self.curr_menu.run_display = False
                print(self.curr_menu.display_menu)
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

    def reset_keys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False 
        self.START_KEY = False 
        self.BACK_KEY = False 
        self.RIGHT_KEY = False
        self.LEFT_KEY = False

    def draw_text(self, text, size, x,y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect) 