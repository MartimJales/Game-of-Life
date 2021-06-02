import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w = self.game.DISPLAY_W/2
        self.mid_h = self.game.DISPLAY_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100
    
    def draw_cursor(self):
        self.game.draw_text('>',20, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display,(0,0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 20)
            self.game.draw_text('Start', 20, self.startx, self.starty)
            self.game.draw_text('Options', 20, self.optionsx, self.optionsy)
            self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start': 
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        if self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
                
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 30
        self.colorx, self.colory = self.mid_w, self.mid_h + 50
        self.languagex, self.languagey = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Options', 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 20)
            self.game.draw_text('Volume (Upcoming)', 20, self.volx, self.voly)
            self.game.draw_text('Colors (Upcoming)', 20, self.colorx, self.colory)
            self.game.draw_text('Language (Upcoming)', 20, self.languagex, self.languagey)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.mainmenu 
            self.run_display = False
        elif self.game.START_KEY:
            if self.state == 'Volume':
                pass #Volume menu 
            elif self.state == 'Colors':
                pass #Colors menu
            elif self.state == 'Language':
                pass #Language menu
            
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Volume': 
                self.cursor_rect.midtop = (self.colorx + self.offset, self.colory)
                self.state = 'Color'
            elif self.state == 'Color':
                self.cursor_rect.midtop = (self.languagex + self.offset, self.languagey)
                self.state = 'Language'
            elif self.state == 'Language':
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                self.state = 'Volume'
        if self.game.UP_KEY:
            if self.state == 'Volume':
                self.cursor_rect.midtop = (self.languagex + self.offset, self.languagey)
                self.state = 'Language'
            elif self.state == 'Color':
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                self.state = 'Volume'
            elif self.state == 'Language':
                self.cursor_rect.midtop = (self.colorx + self.offset, self.colory)
                self.state = 'Color'
                
class CreditMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'History'
        self.histx, self.histy = self.mid_w, self.mid_h + 20
        self.progx, self.progy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.histx + self.offset, self.histy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 20)
            self.game.draw_text('History (Upcoming)', 20, self.histx, self.histy)
            self.game.draw_text('Programmer (Upcoming)', 20, self.progx, self.progy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.mainmenu 
            self.run_display = False
        elif self.game.START_KEY:
            if self.state == 'History':
                pass #History of Game of Life 
            elif self.state == 'Programmer':
                pass #Programmer name
            self.run_display = False
            
    def move_cursor(self):
        if self.game.DOWN_KEY or self.game.UP_KEY:
            if self.state == 'History': 
                self.cursor_rect.midtop = (self.progx + self.offset, self.progy)
                self.state = 'Programmer'
            elif self.state == 'Programmer':
                self.cursor_rect.midtop = (self.histx + self.offset, self.histy)
                self.state = 'History'
            
            
            
            
            
            















