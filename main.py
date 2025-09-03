# OBJECTIVE: simulate many knights moving through a chessboard until it visits all 
# sites of the board. 

# imports 

import numpy as np

# functions 

def move_knight():
    moves = [np.array([-2, 1]),
             np.array([-1, 2]),
             np.array([1, 2]),
             np.array([2, 1]),
             np.array([2, -1]),
             np.array([1, -2]), 
             np.array([-1. -2]),
             np.array([-2, -1])]
    
    available_moves = []
            
    for move in moves:
        if knight[0] + move[0] < 7 and knight[0] + move[0] > 0:
            available_moves.append(move)
        if knight[1] + move[1] < 7 and knight[1] + move[1] > 0:
            available_moves.append(move)
            
    chosen_move = np.random.choice(available_moves, 1)
    
    return chosen_move

    
# main code

# the matrix represents a normal board, 8x8
board = np.zeros(shape=(8, 8), dtype=bool)

# represents a knight with coordinates (row, column)
# assigns it to a random spot
knight = np.array([np.random.randint(0, 7), np.random.randint(0, 7)])

