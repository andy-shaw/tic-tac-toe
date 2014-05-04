'''
Author: Andy Shaw
Date:   12/20/2013

This module has the game GUI and the text based game classes. Both rely on the Board class
'''

from board import Board
from Tkinter import *
import agent

class GameGUI:

    def __init__(self, master, intro, debug, gameType):
        self.debug = debug
        self.gameType = gameType
        self.difficulty = None
        self.playAgain = False
        self.master = master
        self.master.title('Tic-Tac-Toe')
        self.board = Board()
        
        #player characters
        self.player = 'X'
        self.opponent = 'O'
        
        if self.debug: print 'board initialized'
    
        #Give introduction to game
        #request difficulty again if in minimax mode
        if intro or gameType is 'minimax': self.intro()
        if self.debug: print 'intro complete'
        
        #read in images for X, O, and blank
        X = PhotoImage(file='X.gif')
        O = PhotoImage(file='O.gif')
        blank = PhotoImage(file='blank.gif')

        if self.debug: print 'images instantiated'
        
        #initialize to all blanks
        #couldn't think of a better way to do the indexing for the updateBoard command
        self.gifBoard = [
        #row1
        [Button(master, image=blank, command=lambda : self.updateBoard(0,0)), 
        Button(master, image=blank, command=lambda : self.updateBoard(0,1)), 
        Button(master, image=blank, command=lambda : self.updateBoard(0,2))],
        #row2
        [Button(master, image=blank, command=lambda : self.updateBoard(1,0)), 
        Button(master, image=blank, command=lambda : self.updateBoard(1,1)), 
        Button(master, image=blank, command=lambda : self.updateBoard(1,2))],
        #row3
        [Button(master, image=blank, command=lambda : self.updateBoard(2,0)), 
        Button(master, image=blank, command=lambda : self.updateBoard(2,1)), 
        Button(master, image=blank, command=lambda : self.updateBoard(2,2))],
        ]
        
        if self.debug: print 'gifs and board built'
        
        #create reference for each widget
        for row in range(3):
            for column in range(3):
                self.gifBoard[row][column].image = blank
                
        if self.debug: print 'images referenced in gif matrix'
        
        for row in range(3):
            for column in range(3):
                self.gifBoard[row][column].grid(row=row*3, column=column*3, rowspan=3, columnspan=3, sticky=W+N+E+S)
                
        if self.debug: print 'buttons bound to grid'
            
        self.alert = StringVar()
        self.alert.set('')
        self.alertText = Message(master, textvariable=self.alert, padx=3, pady=3,width=100).grid(
            row=9, columnspan=9)
            
        if self.debug: print 'alert box created and bound to frame'
        
    def intro(self):
        import tkMessageBox
        dumbWelcome =  '''Welcome to tic-tac-toe! This game has no intelligence behind 
your opponent.  The computer will select a random square to 
place its O.  You have to try to lose.'''

        minimaxWelcome = '''Welcome to tic-tac-toe! This game has 3 levels of difficulty.
Easy, Medium, and Hard.  Easy can plan ahead 1 move, Medium can 
plan ahead 2 moves, and Hard can plan ahead to the end of the 
game.  Please select a difficulty.'''
        
        if self.gameType is 'dumb': 
            tkMessageBox.showinfo('Welcome', dumbWelcome)
        if self.gameType is 'minimax': 
            tkMessageBox.showinfo('Welcome', minimaxWelcome)
        
            #open new frame to get difficulty
            root = Toplevel(master=self.master)
            root.title('Difficulty')
            difficulty = StringVar()
            Radiobutton(root, text='Easy', indicatoron=0, variable=difficulty, value='E', width=10, command=lambda x=root: self.close(x)).grid(row=0)
            Radiobutton(root, text='Medium', indicatoron=0, variable=difficulty, value='M', width=10,command=lambda x=root: self.close(x)).grid(row=1)
            Radiobutton(root, text='Hard', indicatoron=0, variable=difficulty, value='H', width=10, command=lambda x=root: self.close(x)).grid(row=2)
            
            root.protocol('WM_DELETE_WINDOW', lambda x=root: self.close(x))
            
            root.mainloop()

            if self.debug: print 'difficulty is', difficulty.get()
            
            if len(difficulty.get()) is not 0: self.difficulty = difficulty.get()
            else: 
                #notify player that they did not set the difficulty, so they are facing an easy opponent
                tkMessageBox.showinfo('Difficulty', 'You did not select a difficulty, so you will be on Easy.')
                self.difficulty = 'E'
                
    def close(self, tk):
        tk.withdraw()
        self.master.quit()
        
    def updateAlert(self, text):
        self.alert.set(text)
        
    def updateBoard(self, row, column):
    
        self.updateAlert('')
        if self.debug: print 'update ' + str(row) + ' ' + str(column)
        if self.updatePlayer(row,column) == -1: 
            self.updateAlert("Block already contains an X or O, please choose another box.")
            return
            
        #check for a winner or a full board
        if self.board.hasWinner(): self.endGame(); return
        if self.board.isFull(): self.endGame(); return
        
        self.updateOpponent()
        
        #check for a winner or a full board
        if self.board.hasWinner(): self.endGame(); return
        if self.board.isFull(): self.endGame(); return
        
    def updateOpponent(self):
        if self.gameType is 'dumb': row, column = agent.dumb(self.board)
        if self.gameType is 'minimax': row, column = agent.difficult(self.board, self.difficulty)
        
        if self.debug: print 'updated opponent at', row, column
        
        self.board.setBlock(row, column, 'O')
        
        self.updateGif()
        
    def updatePlayer(self, row, column):
        #check if block is already occupied
        if self.board.getBlock(row, column) is not ' ': return -1
        
        if self.debug: print 'updated player at', row, column
        
        self.board.setBlock(row, column, 'X')
        
        self.updateGif()
        return 1
        
    def updateGif(self):
        '''update visual board by replacing the button'''
        if self.debug: print self.board.toString(), '\n'
        
        for row in range(3):
            for column in range(3):
                if self.board.getBlock(row, column) is 'X':
                    #create a new identical button with image X
                    X = PhotoImage(file='X.gif')
                    self.gifBoard[row][column]= Button(self.master, image=X, command=(lambda x=row,y=column:self.updateBoard(x,y)))
                    self.gifBoard[row][column].image = X
                    self.gifBoard[row][column].grid(row=row*3, column=column*3, rowspan=3, columnspan=3, sticky=N+S+E+W)
                elif self.board.getBlock(row, column) is 'O':
                    #create a new identical button with image O
                    O = PhotoImage(file='O.gif')
                    self.gifBoard[row][column]= Button(self.master, image=O, command=(lambda x=row,y=column:self.updateBoard(x,y)))
                    self.gifBoard[row][column].image = O
                    self.gifBoard[row][column].grid(row=row*3, column=column*3, rowspan=3, columnspan=3, sticky=N+S+E+W)
                    
    def endGame(self):
        '''ask user if they wish to play again'''
        import tkMessageBox
        
        winner = ''
        again = '\nWould you like to play again?'
        if self.board.hasWinner() is 'X':
            winner = 'Congratulations, you won!'
        elif self.board.hasWinner() is 'O':
            winner = 'Sorry, but you lost.'
        elif self.board.isFull():
            winner = 'There was no winner this time'
            
        if not tkMessageBox.askyesno('Play Again?', winner + again):
            self.playAgain = False
        else:
            self.playAgain = True
            
        self.master.destroy()