'''
Author: Andy Shaw
Date:   12/13/2013

This class represents a tic-tac-toe board.
'''

class Board:
    '''class representing a tic-tac-toe board'''
        
    def __init__(self, preset=None):
        '''set each place to provided 2-D array'''
        
        if preset == None:         
            self.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]
        else: self.board = preset
        
        #verify that input board is formatted correctly
        if len(self.board) is not 3: raise Exception('Incorrect board format')
        for row in self.board:
            if len(row) is not 3: raise Exception ('Incorrect board format')

        #verify that the elements of the board are possibly entry values
        for row in self.board:
            for move in row:
                if move in ['X', 'O', ' ']:
                    #correct format
                    pass
                else:
                    #incorrect format
                    raise Exception('Incorrect board format')
                    
    def getBlock(self, row, column):
        '''return the element at row, column'''
        
        #verify dimensions are in bounds
        if not 0 <= row <= 2: raise Exception('row out of range in getBlock')
        if not 0 <= column <= 2: raise Exception('column out of range in getBlock')
        return self.board[row][column]

    def setBlock(self, row, column, move):
        '''set the block contents to the provided move'''
        
        #verify input
        if move not in ['X', 'O', ' ']: raise Exception('invalid block assignment')
        if not 0 <= row <= 2: raise Exception('row out of range in setBlock')
        if not 0 <= column <= 2: raise Exception('column out of range in setBlock')
        
        self.board[row][column] = move
        
    def toString(self):
        '''represent board in a string'''
        s = ''
        for row in range(3):
            list = []
            for column in range(3):
                list.append(str(self.board[row][column]))
            s += '|'.join(list) + '\n-----\n'
        return s[:-7] #remove last \n-----\n
        
    def isFull(self):
        '''return true if board has no empty spaces'''
        for row in range(3):
            for column in range(3):
                if self.board[row][column] == ' ':
                    return False
        return True
    
    def hasWinner(self):
        '''check to see if there are 3 of any kind in a row, returns None if not'''
        
        #check all rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2] and self.board[row][0] != ' ' and self.board[row][1] != ' ' and self.board[row][2] != ' ':
                return self.board[row][0]
                
        #check all columns
        for column in range(3):
            if self.board[0][column] == self.board[1][column] and self.board[1][column] == self.board[2][column] and self.board[0][column] != ' ' and self.board[1][column] != ' ' and self.board[2][column] != ' ':
                return self.board[0][column]
                
        #check diagonals
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[2][0] != ' ':
            return self.board[0][2]
            
        return None