'''
Author: Andy Shaw
Date:   12/19/2014

This is the game agent.  The problem solving algorithms are located here.
'''

from board import Board

def dumb(board):
    '''find viable move on board, and return row,column coordinates for placement'''
    
    import random
    
    row = random.randint(0,2)
    column = random.randint(0,2)
    
    while board.getBlock(row,column) is not ' ':
        row = random.randint(0,2)
        column = random.randint(0,2)
    
    return row, column
    
def difficult(board, difficulty, computer='O'):
    if difficulty is 'E':
        movesAhead = 1
    elif difficulty is 'M':
        movesAhead = 2
    elif difficulty is 'H':
        movesAhead = 10

    nextBoard = minimax(board, movesAhead, True, computer)[1]
    
    #find the row,column changed from the previous board to now
    for row in range(3):
        for column in range(3):
            if board.getBlock(row, column) is not nextBoard.getBlock(row, column):
                return row, column
    
    
def minimax(board, depth, maxPlayer, computer='O'):
    '''naive encoding for minimax.  Algorithm from wikipedia article on minimax'''
    if depth == 0 or board.hasWinner() or board.isFull():
        return (score(board, computer), board)

    if computer is 'O':
        if maxPlayer:
            #empty board is for a place holder
            bestValue = (-99999, Board())
            for child in successor(board, 'O'):
                value = minimax(child, depth-1, False)
                bestValue = max(bestValue, value)
            return bestValue
                
        else:
            #empty board is for place holder
            bestValue = (99999, Board())
            for child in successor(board, 'X'):
                value = minimax(child, depth-1, True)
                bestValue = min(bestValue,value)
            return bestValue
            
    elif computer is 'X':
        if maxPlayer:
            #empty board is for a place holder
            bestValue = (-99999, Board())
            for child in successor(board, 'X'):
                value = minimax(child, depth-1, False, 'X')
                bestValue = max(bestValue, value)
            return bestValue
                
        else:
            #empty board is for place holder
            bestValue = (99999, Board())
            for child in successor(board, 'O'):
                value = minimax(child, depth-1, True, 'X')
                bestValue = min(bestValue,value)
            return bestValue

'''
Local methods
'''
    
def score(board, computer):
    if computer is 'O':
        if board.hasWinner() is 'X':
            return -100
        elif board.hasWinner() is 'O':
            return 100
    elif computer is 'X':
        if board.hasWinner() is 'X':
            print 'win'
            return 100
        elif board.hasWinner() is 'O':
            return -100
            
    #tied game is preferable to losing
    elif board.isFull():
        return 50
    #board has no winner
    else:
        return -1

#-----------------------------------------------------------------------------------------------
        
def successor(board, move):
    '''returns set of possible board configurations for placing the element passed by move'''
    
    set = []
    for row in range(3):
        for column in range(3):
            if board.getBlock(row, column) == ' ':
                newBoard = Board()
                copyBoard(board, newBoard)
                newBoard.setBlock(row, column, move)
                set.append(newBoard)
    return set
    
#-----------------------------------------------------------------------------------------------

def copyBoard(board1, board2):
    '''copy the contents of board1 to board2. Note: does not return anything'''
    for row in range(3):
        for column in range(3):
            board2.setBlock(row, column, board1.getBlock(row,column))