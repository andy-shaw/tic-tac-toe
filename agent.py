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
    movesAhead = {'E': 1, 'M': 3, 'H': 10}

    root = Node(board)
    bestMove = minimax(root, movesAhead[difficulty], True, computer)
    
    for child in root.children: print child.score, '\t',
    print ''
    
    #get child configuration that matches bestMove
    nextBoard = None
    for child in root.children:
        #prioritize winning
        if child.board.hasWinner() == computer:
            nextBoard = child.board
    
    #choose board that matches best move if win isn't possible
    if not nextBoard:
        for child in root.children:
            if child.score == bestMove:
                nextBoard = child.board

    #find the row,column changed from the previous board to now
    for row in range(3):
        for column in range(3):
            if board.getBlock(row, column) is not nextBoard.getBlock(row, column):
                return row, column

def minimax(node, depth, maxPlayer, computer):
    '''naive encoding for minimax.  Algorithm from wikipedia article on minimax'''
    if depth == 0 or node.board.hasWinner() or node.board.isFull():
        node.score = score(node.board, computer)
        return node.score

    if computer is 'O':
        if maxPlayer:
            #empty board is for a place holder
            bestValue = -99999
            node.children = successor(node, 'O')
            for child in node.children:
                value = minimax(child, depth-1, False, computer)
                bestValue = max(bestValue, value)
            node.score = bestValue
            return bestValue

        else:
            #empty board is for a place holder
            bestValue = 99999
            node.children = successor(node, 'X')
            for child in node.children:
                value = minimax(child, depth-1, True, computer)
                bestValue = min(bestValue, value)
            node.score = bestValue
            return bestValue

    elif computer is 'X':
        if maxPlayer:
            #empty board is for a place holder
            bestValue = -99999
            node.children = successor(node, 'X')
            for child in node.children:
                value = minimax(child, depth-1, False, computer)
                bestValue = max(bestValue, value)
            node.score = bestValue
            return bestValue

        else:
            #empty board is for a place holder
            bestValue = 99999
            node.children = successor(node, 'O')
            for child in node.children:
                value = minimax(child, depth-1, True, computer)
                bestValue = min(bestValue, value)
            node.score = bestValue
            return bestValue

'''
Local methods
'''

def score(board, computer):
    '''rate provided board on if there's a winner, or if it's full'''
    if computer is 'O':
        if board.hasWinner() is 'X':
            return -100
        elif board.hasWinner() is 'O':
            return 100
    if computer is 'X':
        if board.hasWinner() is 'X':
            return 100
        elif board.hasWinner() is 'O':
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