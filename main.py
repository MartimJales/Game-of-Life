from game import Game
import numpy as np

g = Game()

matrix1 = np.zeros((3, 3), dtype=int)

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
