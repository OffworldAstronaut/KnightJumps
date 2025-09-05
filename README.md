# ♞ KnightJumps

This repository explores the classic Knight's Tour problem:  
**Can a knight visit all chessboard squares exactly once?**  
It implements Warnsdorf's Rule to efficiently find a complete knight's tour on a standard 8x8 chessboard.

## ♞ Features

- **Warnsdorf's Rule Algorithm:**  
  Uses a heuristic to always move the knight to the square with the fewest onward moves, maximizing the chance of a complete tour.
- **Step-by-step Visualization:**  
  Watch the knight's progress in your terminal, with a live-updating board.
- **Customizable Start:**  
  Choose any starting position for the knight.

## ♞ Usage

After cloning this repository:

1. **Install dependencies:**
   ```bash
   pip install numpy tabulate
   ```

2. **Run the tour:**
   ```bash
   python main.py
   ```

   By default, the knight starts at the top-left corner (0, 0).  
   You can modify `main.py` to change the starting position.

## ♞ Files

- `main.py` — Entry point to run the knight's tour.
- `classes.py` — Contains the `Knight` and `Board` classes and the Warnsdorf's Rule implementation.
- `README.md` — This file.

## ♞ How it Works

- The knight moves according to chess rules.
- At each step, it chooses the next move with the fewest onward possibilities (Warnsdorf's Rule).
- The board is printed in the terminal, updating after each move.

## ♞ Example Output

```
Knight tour completed.
```
(You will see the board update in your terminal as the knight moves.)
