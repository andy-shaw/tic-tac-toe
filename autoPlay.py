'''
Author: Andy Shaw
Date:   12/27/2013

This method plays a round of tic-tac-toe with the computer vs the computer.
The game display will be in the command prompt, and text based.
'''

import agent
import random
from board import Board
from time import sleep

def autoPlay(player1, player2, error, silent):
    '''player1 difficulty, player2 difficulty, and error of placing in the wrong place'''
    
    b = Board()
    
    from random import randint
    
    #start player1 in a random spot for quicker calculation of first move
    b.setBlock(randint(0,2), randint(0,2), 'X')
    if not silent: print b.toString(), '\n'
    
    while not b.hasWinner() and not b.isFull():
        
        #player2 goes
        row, column = agent.difficult(b, player1, 'O')
        #if player error occurs, choose a random, empty place to put their move
        if random.random() < error:
            row = random.randint(0,2)
            column = random.randint(0,2)
            while b.getBlock(row, column) is not ' ':
                row = random.randint(0,2)
                column = random.randint(0,2)
            
        b.setBlock(row, column, 'O')
        if not silent: print b.toString(), '\n'
        
        if not silent: sleep(1)
        
        if b.hasWinner() or b.isFull(): continue
        
        #player1 goes
        row, column = agent.difficult(b, player2, 'X')
        #if player error occurs, choose a random, empty place to put their move
        if random.random() < error:
            row = random.randint(0,2)
            column = random.randint(0,2)
            while b.getBlock(row, column) is not ' ':
                row = random.randint(0,2)
                column = random.randint(0,2)
            
        b.setBlock(row, column, 'X')
        if not silent: print b.toString(), '\n'
        
        if not silent: sleep(1)

    if not silent:
        if b.hasWinner() is 'X': print 'X won this round'
        elif b.hasWinner() is 'O': print 'O won this round'
        elif b.isFull(): print 'There was no winner this round'
        
    return b.hasWinner()
        
if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    
    player1 = args[0]
    player2 = args[1]

    difficulties = ['E', 'M', 'H']
    
    if player1 not in difficulties: print "invalid difficulty: enter E, M, or H for difficulty"; exit()
    if player2 not in difficulties: print "invalid difficulty: enter E, M, or H for difficulty"; exit()
    
    try:
        errorRate = float(args[2])
        if not 0 <= errorRate < 1:
            raise Exception
    except:
        print 'invalid error rate: enter a number between 0 and 1'
        exit()
        
    try:
        tmp = args[3]
        if tmp == 'SILENT': silent = True
        else: raise Exception
    except:
        silent = False
        
    winner = autoPlay(player1, player2, errorRate, silent)