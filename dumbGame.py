'''
Author: Andy Shaw
Date:   12/13/2013

This is a dumb game.  
The game will output to the console each turn.
The game agent will select a random, empty square and place its move there.
'''

def game():
    from board import Board
    from string import lower
    import agent
    import random
    
    #make a new, empty board
    b = Board()
    
    #show player empty board
    print '\n\n'
    print 'Welcome to tic-tac-toe.\nHere is the board, when placing your move,\n', 
    print 'be sure to use the format column,row when specifying where to place your X.\n',
    print 'i.e. the top left square is 1,1 and the bottom right square is 3,3\n',
    print 'You can type Quit to forfeit at any time.\n\n\n'
    
    print b.toString()
    
    #continue placing until board is full, or someone has won
    while not b.hasWinner() and not b.isFull():
        #player goes first (is X)
        player = raw_input('\n\nWhat column and row do you want to put X in?\n(Use column,row format)\n')
            
        #see if the player quits
        if lower(player) == "quit" or lower(player[0]) == 'q': print 'You lost the game.  Thank you for playing!'; exit()
        
        #make sure player entered something
        if len(player) < 3:
            print 'Please enter your column,row to place the X, or type quit to forfeit.'
            continue
        
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
        row,column = agent.dumb(b)
            
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
    keepPlaying = True
    while keepPlaying:
        keepPlaying = game()
    print 'Thank you for playing!'
    