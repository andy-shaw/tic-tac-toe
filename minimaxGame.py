'''
Author: Andy Shaw
Date:   12/15/2013

This game uses a minimax tree to decide which moves the computer will take.
Difficulties rely on a probability to for the computer to choose the best next move 
from the successors.
'''

def game(difficulty):
    pass
    
if __name__ == '__main__':
    import sys
    
    #get difficulty from arguments
    try:
        difficulty = sys.argv[1]
        if not difficulty in ['E','M','H']: raise Exception
    except:
        print 'Invalid difficulty.  Enter E M or H as difficulty for easy, medium, or hard.'
        exit()
        
    game(difficulty)

#----------------------------------------------------------------------------------------------
    
#----------------------------------------------------------------------------------------------

def 

#----------------------------------------------------------------------------------------------
                
def copyBoard(board1, board2):
    '''copy the contents of board1 to board2. Note: does not return anything'''
    for row in range(3):
        for column in range(3):
            board2.setBlock(row, column, board1.getBlock(row,column))