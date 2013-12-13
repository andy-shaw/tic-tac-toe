'''
Author: Andy Shaw
Date:   12/13/2013

This class represents a tic-tac-toe board.
'''

class Board:
    '''class representing a tic-tac-toe board'''
        
    def __init__(self, preset=None):
        '''set each place to provided 2-D array'''
        
        elements = ['X', 'O', ' ']
        
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
                if move in elements:
                    #correct format
                    pass
                else:
                    #incorrect format
                    raise Exception('Incorrect board format')

    def setBlock(self, move):
        '''set the block contents to the provided move'''
        
        if move not in elements: raise Exception('invalid block assignment')
        
        self.