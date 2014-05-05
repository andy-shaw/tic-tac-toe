from board import Board
import itertools

possibleValues = ['X', 'O', ' ']

boardConfigurations = []

a = []
b = []
c = []

r = itertools.product(possibleValues, repeat=3)
for e in r:
	a.append(e)
	b.append(e)
	c.append(e)

for x in a:
	for y in b:
		for z in c:
			base = []
			base.append(list(x))
			base.append(list(y))
			base.append(list(z))
			boardConfigurations.append(Board(base))

print 'All possible board configurations are calculated'
print 'n:\t\t', len(boardConfigurations)

numWinners = 0
numFull = 0
numBoth = 0
xwin = 0
owin = 0
for b in boardConfigurations:
	if b.hasWinner():
		numWinners += 1
		if b.hasWinner() == 'X':
			xwin += 1
		else:
			owin += 1
	if b.isFull():
		numFull += 1
		if b.hasWinner():
			numBoth += 1

print 'numWinners:\t', numWinners
print 'numFull:\t', numFull
print 'numBoth:\t', numBoth
print 'Xwin:\t\t', xwin
print 'Owin:\t\t', owin