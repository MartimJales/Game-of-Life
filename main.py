from game import Game
import numpy as np

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
