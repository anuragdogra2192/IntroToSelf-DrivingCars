import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []

    #
    # TODO - implement this in part 2
    #
    height = len(beliefs)
    width = len(beliefs[0])
    s = 0
    for i in range(height):
        row=[]
        for j in range(width):
            if color == grid[i][j]:
                cell = beliefs[i][j]*p_hit
                row.append(cell)
                s+=cell
            else:
                cell = beliefs[i][j]*p_miss
                row.append(cell)
                s+=cell
        new_beliefs.append(row)
    #print(new_beliefs)
    #print(s)
    for i in range(height):
        for j in range(width):
            new_beliefs[i][j] = new_beliefs[i][j]/s
    #print(new_beliefs)
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            #pdb.set_trace()
            new_G[int(new_j)][int(new_i)] = cell
    return blur(new_G, blurring)