# OBJECTIVE: Implement a Warnsdorf's Rule algorithm to find a Knight Tour.

# Modules 

import numpy as np                  # Arrays and other numerical utilities
from typing import List, Tuple      # Typing

# Classes

# Represents a knight
class Knight:
    def __init__(self, start_row: int, start_col: int) -> None:
        """Instantiates a knight with a starting position (row, col)

        Args:
            start_row (int): starting row coordinate 
            start_col (int): starting col coordinate
        """
        self.row = start_row    # row of the starting coordinate 
        self.col = start_col    # column of the starting coordinate 
        # array of possible moves of a common knight (row, column)
        self.move_offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
    def get_possible_moves(self) -> List[Tuple[int, int]]:
        """Get all the possible positions resulting from a move/possible moves of the Knight

        Returns:
            List[Tuple[int, int]]: List of tuples of the possible positions/moves 
        """
        moves = []  # List of moves
        
        # Loops through all the moves, adding them to the current position of the knight
        for r_offset, c_offset in self.move_offsets:
            new_row = self.row + r_offset
            new_col = self.col + c_offset
            moves.append((new_row, new_col))
            
        # Returns the list of moves (valid or not, they're all the possible moves!)
        return moves

# Represents a chessboard -- also works as the environment for the Tour
class Board:
    def __init__(self, start_row: int, start_col: int) -> None:
        """Creates a chessboard and the environment of the Tour

        Args:
            start_row (int): starting row coordinates for the Knight
            start_col (int): starting col coordinates for the Knight
        """
        # "board" to store all the accessibility counting necessary to Warnsdorf's
        self.warnsdorf_board = np.zeros(shape=(8, 8), dtype=int)
        # "board" to store all the visited tiles
        self.already_visited = np.zeros(shape=(8, 8), dtype=bool)
        # stores the knight associated with the board 
        self.knight = Knight(start_row, start_col)
        # counter of visited sites, necessary for the main loop of the algorithm
        self.visited_count = 1 
        # marks the starting position of the knight as already visited
        self.already_visited[start_row, start_col] = True
        # adds the starting position of the knight as the first of it's tour path
        self.path = [(start_row, start_col)]
        
    def is_valid_move(self, row: int, col: int) -> bool:
        """Verifies if a possible move of the Knight is valid in the context of the board

        Args:
            row (int): row coordinate of the move 
            col (int): col coordinate of the move

        Returns:
            bool: True if valid, False if not
        """
        # A move is only valid if the Knight stays inside the board and doesn't visit 
        # a tile it already moved to
        return 0 <= row < 8 and 0 <= col < 8 and not self.already_visited[row, col]
        
    def get_accessibility(self, row: int, col: int) -> int:
        """

        Args:
            row (int): _description_
            col (int): _description_

        Returns:
            int: _description_
        """
        accessibility_count = 0
        temp_knight = Knight(row, col)
        for r, c in temp_knight.get_possible_moves():
            if self.is_valid_move(r, c):
                accessibility_count += 1
                
        return accessibility_count
        
    def run_tour(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        while self.visited_count < 64:
            current_pos = (self.knight.row, self.knight.col)
            valid_next_moves = []
            for r, c in self.knight.get_possible_moves():
                if self.is_valid_move(r, c): 
                    valid_next_moves.append((r, c))
                    
            if not valid_next_moves:
                print("Knight tour failed. Stuck.")
                return False
            
            best_move = None
            min_accessibility = 9
            
            for move in valid_next_moves:
                accessibility = self.get_accessibility(move[0], move[1])
                if accessibility < min_accessibility:
                    min_accessibility = accessibility
                    best_move = move
                    
            self.knight.row, self.knight.col = best_move
            self.already_visited[best_move[0], best_move[1]] = True
            self.path.append(best_move)
            self.visited_count += 1
            
        print("Knight tour completed.")
        return True