'''
Test board class
'''

from board import Board
import random

def main(debug):
    '''test suite for board class'''
    elements = ['X', 'O', ' ']
    
    #build valid and invalid boards
    presetGood = [
    ['X','X','X'],
    ['O','O','O'],
    [' ',' ',' ']]

        
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
    
    #----------------------------------------------------------------------------------
    
    if debug: print 'test getBlock'
    b = Board(presetGood)
    if debug: print '\ttest row out of range'
    try: x = b.setBlock(5,2)
    except:
        if debug: print '\tcaught row out of range\n'
        
    if debug: print '\ttest column out of range'
    try: x = b.setBlock(2,5)
    except:
        if debug: print '\tcaught column out of range\n'
    
    if debug: print '\ttest for correct retrieval'
    for row in range(3):
        for column in range(3):
            assert(presetGood[row][column] == b.getBlock(row, column))
    if debug: print '\tpassed correct retrieval'
    if debug: print 'passed getBlock\n'
    
    #----------------------------------------------------------------------------------
    
    if debug: print 'test setBlock'
    b = Board()
    
    if debug: print '\ttest invalid assignment'
    try: b.setBlock(2,2,'A')
    except:
        if debug: print '\tcaught invalid assignment\n'
        
    if debug: print '\ttest row out of range'
    try: b.setBlock(5,2,'X')
    except:
        if debug: print '\tcaught row out of range\n'
        
    if debug: print '\ttest column out of range'
    try: b.setBlock(2,5,'X')
    except:
        if debug: print '\tcaught column out of range\n'
    
    if debug: print '\ttest for correct assignemtnt'
    for row in range(3):
        for column in range(3):
            b.setBlock(row, column, 'X')
            
    for row in range(3):
        for column in range(3):
            assert(b.board[row][column] == 'X')
    if debug: print '\tpassed correct assignemtnt'
    
    if debug: print 'passed setBlock\n'
    
    #----------------------------------------------------------------------------------
    
    if debug: print 'test toString'
    b = Board(presetGood)
    assert('X|X|X\n-----\nO|O|O\n-----\n | | ' == b.toString())
    if debug: print b.toString()
    if debug: print 'passed toString\n'
    
    #----------------------------------------------------------------------------------
    
    if debug: print 'test isFull'
    full = [
    ['X','X','X'],
    ['O','O','O'],
    ['X','X','X']]
    
    notFull = [
    ['X','X','X'],
    ['O',' ','O'],
    ['X','X','X']]
    
    b = Board(full)
    assert(True == b.isFull())
    b = Board(notFull)
    assert(False == b.isFull())
    if debug: print 'passed isFull\n'
    
    #----------------------------------------------------------------------------------
    
    if debug: print 'test hasWinner'
    
    xwin = [
    ['X',' ',' '],
    ['X','O',' '],
    ['X',' ','O']]
    
    b = Board(xwin)
    assert('X' == b.hasWinner())
    
    owin = [
    ['O','X',' '],
    ['O',' ',' '],
    ['O','X','X']]
    
    b = Board(owin)
    assert('O' == b.hasWinner())
    
    nowin = [
    ['X','O','O'],
    ['O','X','X'],
    ['X','O','O']]
    
    b = Board(nowin)
    assert(None == b.hasWinner())
    if debug: print 'passed hasWinner'
    
if __name__ == '__main__':
    import sys
    debug = False
    try: 
        if sys.argv[1] == 'DEBUG': debug = True
    except: pass
    main(debug)