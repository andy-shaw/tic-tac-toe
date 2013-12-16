'''
Author: Andy Shaw
Date:   12/15/2013

This is a minimax tree that will have a board at each node.
'''

from board import Board

class MinimaxTree():
    '''Minimax tree with tic-tac-toe board at each node'''
    
    class Node():
        '''Node to hold board, score, and parent'''
        
        def __init__(self, board, player):
            self.board = board
            
            self.score = 0
            #good if player wins
            if board.hasWinner() == player:
                self.score = 100
            #if another winner is on board, it has to be opponent
            elif board.hasWinner():
                self.score = -100
                
            self.parent = None
            self.children = []
            
    def __init__(self, root, player):
        self.root = self.Node(root, player)
        self.expand(self.root, player)
        
    def expand(self, node, maxPlayer):
        '''expand tree, code dependent on 'X' and 'O' being player'''
        
        #get opposite of max player
        if maxPlayer == 'X': minplayer = 'O'
        elif maxPlayer == 'O': minPlayer = 'X'
        
        successors = self.successor(node.board, maxPlayer)
        for board in successors:
            node.children.append(Node(board, minPlayer))
        
        #recursively expand each node, terminating if board is full or 
        print len(node.children)
        if len(node.children) > 0:
            for each in node.children:
                print each.board.toString() + '\n\n'
                if not each.board.isFull() and not each.board.hasWinner():
                    self.expand(each, minPlayer)
                
#-----------------------------------------------------------------------------------------------
    '''
    Local methods
    '''
    def successor(self, board, move):
        '''returns set of possible board configurations for placing the element passed by move'''
        
        set = []
        
        for row in range(3):
            for column in range(3):
                if board.getBlock(row, column) == ' ':
                    newBoard = Board()
                    self.copyBoard(board, newBoard)
                    set.append(newBoard.setBlock(row,column,move))
        return set
        
#-----------------------------------------------------------------------------------------------

    def copyBoard(self, board1, board2):
        '''copy the contents of board1 to board2. Note: does not return anything'''
        for row in range(3):
            for column in range(3):
                board2.setBlock(row, column, board1.getBlock(row,column))