'''
Author: Andy Shaw
Date:   12/13/2013

This is a dumb game.  
The game will output to the console each turn.
The game agent will select a random, empty square and place its move there.
'''


from Tkinter import *
import tkMessageBox
from board import Board

class Game:
    def __init__(self, master):
        #Give introduction to game
        self.intro()
        
        #read in images for X, O, and blank
        X = PhotoImage(file='X.gif')
        O = PhotoImage(file='O.gif')
        blank = PhotoImage(file='blank.gif')

        #initialize to all blanks
        #couldn't think of a better way to do the indexing for the updateBoard command
        self.gifBoard = [
        #row1
        [Button(master, image=X, command=self.updateBoard(0,0)), 
        Button(master, image=X, command=self.updateBoard(0,1)), 
        Button(master, image=X, command=self.updateBoard(0,2))],
        #row2
        [Button(master, image=X, command=self.updateBoard(1,0)), 
        Button(master, image=X, command=self.updateBoard(1,1)), 
        Button(master, image=X, command=self.updateBoard(1,2))],
        #row3
        [Button(master, image=X, command=self.updateBoard(2,0)), 
        Button(master, image=X, command=self.updateBoard(2,1)), 
        Button(master, image=X, command=self.updateBoard(2,2))],
        ]
        
        #create reference for each widget
        for row in range(3):
            for column in range(3):
                self.gifBoard[row][column].image = X
        
        for row in range(3):
            self.gifBoard[row][0].grid(row=row*3, column=0, rowspan=3, columnspan=3, sticky=W+N+E+S)
            self.gifBoard[row][1].grid(row=row*3+1, column=5, rowspan=3, columnspan=3, sticky=W+N+E+S)
            self.gifBoard[row][2].grid(row=row*3+2, column=9, rowspan=3, columnspan=3, sticky=W+N+E+S)
            
        self.alert = StringVar()
        self.alert.set('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        self.alertText = Message(master, textvariable=self.alert, padx=3, pady=3,width=100).grid(
            row=11, columnspan=11)
            
        Button(master, text='help', command=self.updateAlert).grid(row=12)
        
    def intro(self):
        welcome =  ''
        welcome +=  'Welcome to tic-tac-toe!'
        
        tkMessageBox.showinfo('Welcome', welcome)
        
    def updateAlert(self):
        self.alert.set('hello')
        
    def updateBoard(self, row, column):
        # self.updatePlayer(row,column)
        # self.updateOpponent()
        pass

def game():
    from board import Board
    from string import lower
    import random
    
    #make a new, empty board
    b = Board()
    
    print b.toString()
    
    #continue placing until board is full, or someone has won
    while not b.hasWinner() and not b.isFull():
        #player goes first (is X)
        player = raw_input('\n\nWhat column and row do you want to put X in?\n(Use column,row format)\n')
        
        #make sure player entered something
        if len(player) == 0:
            print 'Please enter your column,row to place the X, or type quit to forfeit.'
            continue
            
        #see if the player quits
        if lower(player) == "quit": print 'You lost the game.  Thank you for playing!'; exit()
        
        #make sure the player input is formatted correctly
        if not len(player) == 3 and player[1] == ',':
            #incorrect format
            print 'Please enter column and row as column,row with no space and a comma separating the values'
            continue
        
        #make sure the user entered integers
        try:
            column = int(player[0]) -1 
            row = int(player[2]) -1
        except:
            print 'Please make sure your coordinates are numbers.'
            continue
        
        #make sure row and column are in bounds
        if not 0 <= row <= 2: print 'Row is out of bounds, please try again'; continue
        if not 0 <= column <= 2: print 'Column is out of bounds, please try again'; continue
        
        #make sure block is already empty
        if b.getBlock(row, column) == ' ':
            b.setBlock(row, column, 'X')
        else: 
            print 'Block already contains an X or O, please enter other coordinates.'
            continue
        
        print '\n\n' + b.toString()
        
        #check to see if the player's move won or filled the board
        if b.hasWinner(): break
        if b.isFull(): break
        
        print '\nNow the computer will place an O.'
        
        #find random empty square for computer's turn
        column = random.randint(0,2)
        row = random.randint(0,2)
        while not b.getBlock(row,column) == ' ':
            column = random.randint(0,2)
            row = random.randint(0,2)
            
        b.setBlock(row, column, 'O')
        
        print '\n\n' + b.toString()
        
    if b.hasWinner(): 
        #if player won
        if b.hasWinner() == 'X': print 'Congratulations! You won!'
        if b.hasWinner() == 'O': print 'Sorry, but you lost.'
        
    elif b.isFull():
        print '\nThere was no winner.'
        
        
    #ask the user if they want to play again
    playAgain = raw_input('\nDo you want to play again? (y/n)\n')
    if len(playAgain) == 0:
        return False
    if lower(playAgain[0]) == 'y':
        return True
    else:
        return False
        
    
if __name__ == '__main__':

    root = Tk()
    game = Game(root)
    root.mainloop()
    
    # keepPlaying = True
    # while keepPlaying:
        # keepPlaying = game()
    # print 'Thank you for playing!'
    