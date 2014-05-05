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

generated = [
[' ', ' ', ' '], 
[' ', ' ', 'X'], 
[' ', 'O', 'X']]

a = Board(preset=generated)
print a.toString(), '\n\n'

move = agent.difficult(a, 'H', 'O')

a.setBlock(move[0], move[1], '+')

print a.toString()