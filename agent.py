'''
Author: Andy Shaw
Date:   12/19/2014

This is the game agent.  The problem solving algorithms are located here.
'''

class Node:
    '''node for minimax tree'''
    def __init__(self, board):
        self.score = None
        self.board = board
        self.children = None
        
    def toString(self):
        s = 'score:\t' + str(self.score) + '\n'
        s += self.board.toString() + '\n'
        s += 'number of children:\t' + str(len(self.children))
        return s

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
    movesAhead = {'E': 2, 'M': 4, 'H': 10}

    root = Node(board)
    bestMove = minimax(root, movesAhead[difficulty], True, computer)

    print '\n\n', bestMove

    nextBoard = None
    
    #choose board that matches best move 
    for child in root.children:
        # print 'child:\t\n', child.board.toString()
        # print 'score:\t', child.score
        # print '-----------'
        if child.score == bestMove:
            nextBoard = child.board

    #find the row,column changed from the previous board to now
    for row in range(3):
        for column in range(3):
            if board.getBlock(row, column) is not nextBoard.getBlock(row, column):
                return row, column

def minimax(node, depth, maxPlayer, player):
    '''naive encoding for minimax with iterative deepening.  Algorithm from wikipedia article on minimax'''
    node.score = score(node.board, player)
    if depth == 0 or node.score != 0:
        if depth == 9:
            print node.board.toString(), '\n'
        return node.score

    if player is 'O': opposite = 'X'
    if player is 'X': opposite = 'O' 

    if maxPlayer:
        #empty board is for a place holder
        bestValue = -99999
        node.children = successor(node, player)
        for child in node.children:
            value = minimax(child, depth-1, False, player)
            bestValue = max(bestValue, value)
        node.score = bestValue
        return bestValue

    else:
        #empty board is for a place holder
        bestValue = 99999
        node.children = successor(node, opposite)
        for child in node.children:
            value = minimax(child, depth-1, True, player)
            bestValue = min(bestValue, value)
        node.score = bestValue
        return bestValue

'''
Local methods
'''

def score(board, player):
    '''rate provided board on if there's a winner, or if it's full'''

    if player is 'O': opposite = 'X'
    if player is 'X': opposite = 'O' 


    if board.hasWinner() is player:
        return 100
    elif board.hasWinner() is opposite:
        return -100

    #tied game is preferable to losing
    if board.isFull():
        return 50

    #board has no winner and is not full
    return 0

#-----------------------------------------------------------------------------------------------

def successor(node, move):
    '''returns set of possible board configurations for placing a single element'''

    set = []
    for row in range(3):
        for column in range(3):
            if node.board.getBlock(row, column) == ' ':
                newBoard = Board()
                copyBoard(node.board, newBoard)
                newBoard.setBlock(row, column, move)
                newNode = Node(newBoard)
                set.append(newNode)
    return set

#-----------------------------------------------------------------------------------------------

def copyBoard(board1, board2):
    '''copy the contents of board1 to board2. Note: does not return anything'''
    for row in range(3):
        for column in range(3):
            board2.setBlock(row, column, board1.getBlock(row,column))