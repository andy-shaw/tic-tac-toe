'''
Author: Andy Shaw
Date:   5/1/2014

This will open the Game GUI, but create an easy to copy and paste output of the inputted board.
'''

from board import Board
from Tkinter import *

class Maker:
    def __init__(self, master, debug, scale=6):
        self.debug = debug
        self.master = master
        self.master.title('Tic-Tac-Toe Maker')
        self.board = Board()
        self.placing = 'X'
        self.scale = scale

        #number of rows above the board for filler buttons
        self.offset = 1

        if self.debug: print 'board initialized'
    
        #read in images for X, O, and blank
        X = PhotoImage(file='X.gif')
        O = PhotoImage(file='O.gif')
        blank = PhotoImage(file='blank.gif')

        if self.debug: print 'images instantiated'



        #initialize to all blanks
        #couldn't think of a better way to do the indexing for the updateBoard command
        self.gifBoard = [
        #row1
        [Button(self.master, image=blank, command=lambda : self.updateBoard(0,0)), 
        Button(self.master, image=blank, command=lambda : self.updateBoard(0,1)), 
        Button(self.master, image=blank, command=lambda : self.updateBoard(0,2))],
        #row2
        [Button(self.master, image=blank, command=lambda : self.updateBoard(1,0)), 
        Button(self.master, image=blank, command=lambda : self.updateBoard(1,1)), 
        Button(self.master, image=blank, command=lambda : self.updateBoard(1,2))],
        #row3
        [Button(self.master, image=blank, command=lambda : self.updateBoard(2,0)), 
        Button(self.master, image=blank, command=lambda : self.updateBoard(2,1)), 
        Button(self.master, image=blank, command=lambda : self.updateBoard(2,2))],
        ]

        if self.debug: print 'gifs and board built'

        #create reference for each widget
        for row in range(3):
            for column in range(3):
                self.gifBoard[row][column].image = blank
                
        if self.debug: print 'images referenced in gif matrix'

        for row in range(3):
            for column in range(3):
                self.gifBoard[row][column].grid(row=(row+self.offset)*self.scale, column=column*self.scale, rowspan=self.scale, columnspan=self.scale, sticky=W+N+E+S)
                

        self.buttonX = Button(self.master, image=X, command=self.setX)
        self.buttonO = Button(self.master, image=O, command=self.setO)
        self.buttonBlank = Button(self.master, image=blank, command=self.setBlank)

        self.buttonX.image = X
        self.buttonO.image = O
        self.buttonBlank.image = blank

        self.buttonX.grid(row=0, column=0, rowspan=self.scale, columnspan=self.scale, sticky=W+N+E+S)
        self.buttonO.grid(row=0, column=1*scale, rowspan=self.scale, columnspan=self.scale, sticky=W+N+E+S)
        self.buttonBlank.grid(row=0, column=2*self.scale, rowspan=self.scale, columnspan=self.scale, sticky=W+N+E+S)

        self.alert = StringVar()
        self.alert.set('Placing ' + self.placing)
        self.alertText = Entry(self.master, textvariable=self.alert)
        self.alertText.grid(row=(3+self.offset)*self.scale, columnspan=3*self.scale)
        
        self.outputButton = Button(self.master, text="Output Board", justify=CENTER, command=self.outputBoard)
        self.outputButton.grid(row=(4+self.offset)*self.scale, columnspan=3*self.scale)

        self.close = Button(self.master, text="Exit", justify=CENTER, command=self.master.destroy)
        self.close.grid(row=(5+self.offset)*self.scale, columnspan=3*self.scale)

        if self.debug: print 'buttons bound to grid'

    def setX(self):
        self.placing = 'X'
        self.updateAlert('Placing ' + self.placing)

    def setO(self):
        self.placing = 'O'
        self.updateAlert('Placing ' + self.placing)

    def setBlank(self):
        self.placing = ' '
        self.updateAlert('Placing blank')

    def outputBoard(self):
        self.updateAlert(self.board.toList())

    def updateAlert(self, text):
        self.alert.set(text)

    def updateBoard(self, row, column):
        if self.placing is ' ': 
            self.updateAlert('Placing blank')
        else:
            self.updateAlert('Placing ' + self.placing)

        if self.debug: print 'update ' + str(row) + ' ' + str(column)
        if self.updatePlayer(row,column) == -1: 
            self.updateAlert("Block already contains an X or O, please choose another box.")
            return

    def updatePlayer(self, row, column):
        #check if block is already occupied
        if self.board.getBlock(row, column) is not ' ' and self.placing is not ' ': return -1
        
        if self.debug: print 'updated player at', row, column
        
        self.board.setBlock(row, column, self.placing)
        
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
                    self.gifBoard[row][column].grid(row=(row+self.offset)*self.scale, column=column*self.scale, rowspan=self.scale, columnspan=self.scale, sticky=N+S+E+W)
                elif self.board.getBlock(row, column) is 'O':
                    #create a new identical button with image O
                    O = PhotoImage(file='O.gif')
                    self.gifBoard[row][column]= Button(self.master, image=O, command=(lambda x=row,y=column:self.updateBoard(x,y)))
                    self.gifBoard[row][column].image = O
                    self.gifBoard[row][column].grid(row=(row+self.offset)*self.scale, column=column*self.scale, rowspan=self.scale, columnspan=self.scale, sticky=N+S+E+W)
                elif self.board.getBlock(row, column) is ' ':
                    #create a new identical button with blank as the image
                    blank = PhotoImage(file='blank.gif')
                    self.gifBoard[row][column]= Button(self.master, image=blank, command=(lambda x=row,y=column:self.updateBoard(x,y)))
                    self.gifBoard[row][column].image = blank
                    self.gifBoard[row][column].grid(row=(row+self.offset)*self.scale, column=column*self.scale, rowspan=self.scale, columnspan=self.scale, sticky=N+S+E+W)


if __name__ == '__main__':
    root = Tk()
    debug = False
    maker = Maker(root, debug)
    root.mainloop()
