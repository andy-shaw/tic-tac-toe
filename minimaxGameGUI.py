'''
Author: Andy Shaw
Date:   12/13/2013

This is a dumb game.  
The GUI interacts with the user, and the user presses buttons to start events.
The board will update itself, and then place the computer's move.
'''

import sys
from Tkinter import *
import tkMessageBox
from board import Board
import agent
from game import GameGUI

if __name__ == '__main__':
    debug = False
    try: 
        if sys.argv[1] == 'DEBUG': debug = True
    except: pass

    playAgain = True
    intro = True
    
    while playAgain:
        root = Tk()
        game = GameGUI(root, intro, debug, 'minimax')
        root.mainloop()
        playAgain = game.playAgain
        intro = False
        root = None
    