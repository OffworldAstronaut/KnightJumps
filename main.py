# OBJECTIVE: Implement a Warnsdorf's Rule algorithm to find a Knight Tour.

# Modules 
import numpy as np

# Classes 
class Knight:
    def __init__(self, start_row, start_col):
        self.row = start_row
        self.col = start_col
        self.move_offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
    def get_possible_moves(self):
        moves = []
        for r_offset, c_offset in self.move_offsets:
            new_row = self.row + r_offset
            new_col = self.col + c_offset
            moves.append((new_row, new_col))
        return moves

class Board:
    def __init__(self, start_row, start_col):
        self.warnsdorf_board = np.zeros(shape=(8, 8), dtype=int)
        self.already_visited = np.zeros(shape=(8, 8), dtype=bool)
        self.knight = Knight(start_row, start_col)
        self.visited_count = 1 
        self.already_visited[start_row, start_col] = True
        self.path = [(start_row, start_col)]
        
    def is_valid_move():
        ...
        
    def get_accessibility():
        ...
        
    # Carries on with the simulation, moving the knight according to the rule
    def run_tour():
        ...