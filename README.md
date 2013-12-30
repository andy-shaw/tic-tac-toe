tic-tac-toe
===========

Tic Tac Toe game with an opponent.  There is a text based and GUI version of the dumb opponent, and only a GUI version of the minimax opponent.

## Running the program

#### Python

This program is written and executed in Python.  

#### Execution

Use the command prompt, and navigate to the directory where all of the python modules are contained.  blank.gif, O.gif, and X.gif must also be present.  Any file starting with an underscore is a test file and is not necessary for the program to run.

Use the following commands to start the program.

#### Dumb

$ python dumbGame.py        -> text based version
$ python dumbGameGUI.py     -> GUI based version

#### Minimax

$ python minimaxGameGUI.py

#### Autoplay

$ python autoPlay.py Player1Difficulty Player2Difficulty ErrorRate

Player1Difficulty -> E M or H corresponding to Easy, Medium, or Hard
Player2Difficulty -> E M or H corresponding to Easy, Medium, or Hard
ErrorRate -> a number in [0,1) that is the probability that each player will have of "messing up" and placing their move in a random square.

## Opponents

#### Dumb

This opponent has no intelligence behind its decisions.  It places an O in a random blank position.

#### Minimax

This opponent has a difficulty selection.  The Easy opponent can plan ahead 1 move.  The Medium opponent can plan ahead 2 moves.  The Hard opponent plans ahead to the end of the game.

With the hard opponent for minimax, every possible board configuration after the player's first position of X is calculated.  There is a slight delay (~2-3 seconds on testing computers) for the computer to finish its calculations.

## Minimax Algorithm

#### Pseudo-code from [wikipedia article](http://en.wikipedia.org/wiki/Minimax#Pseudocode)

'''
function minimax(node, depth, maximizingPlayer)
    if depth = 0 or node is a terminal node
        return the heuristic value of node
    if maximizingPlayer
        bestValue := -∞
        for each child of node
            val := minimax(child, depth - 1, FALSE))
            bestValue := max(bestValue, val);
        return bestValue
    else
        bestValue := +∞
        for each child of node
            val := minimax(child, depth - 1, TRUE))
            bestValue := min(bestValue, val);
        return bestValue

(* Initial call for maximizing player *)
minimax(origin, depth, TRUE)
'''

#### Conversion for use in tic tac toe

At each point of calculation, the root of the minimax tree will have resulted from the player (X) having just placed their piece.  The minimax calculation determines where the computer (O) should place their piece.

The score or heuristic applied to terminal nodes depends on if there is a winner, if the board is full (a tie), or if neither of those qualities are met.  
The scores for each board (if computer goes second) are as follows:
    Tie     -  50
    X wins  - -100
    O wins  -  100
    Neither -  0
    
Also, there is an implementation for the minimax tree to be computed from the standpoint that the computer is X and X is trying to win.

