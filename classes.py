# OBJECTIVE: Implement a Warnsdorf's Rule algorithm to find a Knight Tour.

# Modules 

import numpy as np                  # Arrays and other numerical utilities
from typing import List, Tuple      # Typing
from tabulate import tabulate       # Pretty-printing
import os                           # System utilies
import time                         # time utilies

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
    def __init__(self, start_row: int=0, start_col: int=0) -> None:
        """Creates a chessboard and the environment of the Tour

        Args:
            start_row (int): starting row coordinates for the Knight. Defaults to 0
            start_col (int): starting col coordinates for the Knight. Defaults to 0
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
        """Calculates and return the accessible moves number for each tile

        Args:
            row (int): tile row coordinate
            col (int): tile col coordinate 

        Returns:
            int: accessible moves count
        """
        accessibility_count = 0
        temp_knight = Knight(row, col)
        # Get all possible moves, only counts the valid ones
        for r, c in temp_knight.get_possible_moves():
            if self.is_valid_move(r, c):
                accessibility_count += 1
                
        return accessibility_count
        
    def run_tour(self, all_visited: bool=True) -> bool:
        """Runs the Knight's Tour, stores in the path atribute all the Knight's moves

        Args:
            all_visited (bool): if True, prints all the visited tiles; False returns only the current 
            tile visited by the Knight; Defaults to True.

        Returns:
            bool: Returns True if the Tour's completed. False if not.
        """
        # The tour is for every tile in the board
        while self.visited_count < 64:
            # Stores the valid next moves
            valid_next_moves = []
            for r, c in self.knight.get_possible_moves():
                if self.is_valid_move(r, c): 
                    valid_next_moves.append((r, c))
                    
            # If there are none, the tour failed. 
            if not valid_next_moves:
                print("Knight tour failed. Stuck.")
                return False
            
            # Calculates the best move according to the Rule -- the one with smaller accessibility
            best_move = None
            min_accessibility = 9
            
            for move in valid_next_moves:
                accessibility = self.get_accessibility(move[0], move[1])
                if accessibility < min_accessibility:
                    min_accessibility = accessibility
                    best_move = move
                    
            # Moves the knight to the best tile found 
            self.knight.row, self.knight.col = best_move
            # Marks the visited tile as already visited
            self.already_visited[best_move[0], best_move[1]] = True
            # Registers the new tile in the path 
            self.path.append(best_move)
            # Updates the visited count
            self.visited_count += 1
            
            if all_visited:
                self.print_visited_board()
            else:
                self.print_current_board()
            
        # Tour completed
        print("Knight tour completed.")
        return True
    
    def print_current_board(self):
        time.sleep(0.5)
        os.system("clear")
        empty_board = np.zeros(shape=(8, 8), dtype=bool)
        empty_board[self.knight.row, self.knight.col] = True
        print(tabulate(empty_board, tablefmt="fancy_grid"))
        
    def print_visited_board(self):
        time.sleep(0.5)
        os.system("clear")
        print(tabulate(self.already_visited, tablefmt="fancy_grid"))