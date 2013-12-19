import agent
from board import Board

preset = [
['X', 'X', ' '],
['O', 'O', ' '],
['O', 'X', ' ']]

nextpreset = [
['X',' ',' '],
[' ',' ',' '],
[' ',' ',' ']]

b = Board(nextpreset)

print agent.difficult(b, 'H', 'X')
