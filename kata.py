import numpy as np
import gol_utils as gol
import matplotlib.pyplot as plt

# objective: create the  function of evolution for the game of life,
# given a world state, return the next one.
# first world: 3*3
# second world: n*n

# rules.
# 1 - if it has 2 neighbours, leave it the same
# 2 - if it has 3 neighbours, it's always alive
# 3 - otherwise, it's always dead.

def environtment(world, x, y, N = 3):
	total = - world[x][y]
	for i in range(max(x - 1, 0), min(x + 2, N)):
		for j in range(max(y - 1, 0), min(y + 2, N)):
			total += world[i][j]
	return total

def evolve_world(world = [], N = 3):
	newworld = np.zeros((N, N), dtype=int)
	for i in range(N):
		for j in range(N):
			neighbours = environtment(world, i, j, N)
			if neighbours == 2:
				newworld[i][j] = world[i][j]
			if neighbours == 3:
				newworld[i][j] = 1
	return newworld
