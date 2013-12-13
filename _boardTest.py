'''
Test board class
'''

from board import Board
import random

def main(debug):
    '''test suite for board class'''
    elements = ['X', 'O', ' ']
    
    #build valid and invalid boards
    presetGood = []
    
    for row in range(3):
        x = []
        for column in range(3):
            x.append(elements[random.randint(0,2)])
        presetGood.append(x)
        
    presetBad = [
    [' ','A',' '],
    [' ',' ',' '],
    [' ',' ',' ']]
    
    #test constructor
    if debug: print 'test constructor with no preset'
    b = Board()
    for row in range(3):
        for column in range(3):
            assert(' ' == b.board[row][column])
    if debug: print 'passed constructor with no preset\n'
    
    #----------------------------------------------------------------------------------
    
    if debug: print 'test constructor with preset'
    if debug: print '\ttest good board'
    b = Board(preset=presetGood)
    for row in range(3):
        for column in range(3):
            assert(elements.index(b.board[row][column]) in [0,1,2])
    if debug: print '\tpassed good board\n'
    
    if debug: print '\ttest bad board'
    try: b = Board(preset=presetBad)
    except: 
        if debug: print '\tcaught bad board'
    
    if debug: print 'passed constructor with preset\n'
    
if __name__ == '__main__':
    import sys
    debug = False
    try: 
        if sys.argv[1] == 'DEBUG': debug = True
    except: pass
    main(debug)