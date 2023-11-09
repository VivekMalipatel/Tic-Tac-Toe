# Tic-Tac-Toe
Tic-Tac-Toe in Python the following adversarial search algorithms

# CS 480 Fall 2023 Programming Assignment #01

## Problem Description

This assignment involves implementing adversarial search algorithms in Python to play the game of Tic-Tac-Toe. The algorithms to be implemented are:

- MiniMax
- MiniMax with alpha-beta pruning

The game is played against the computer.

## Usage

To execute the program, use the following command:

```bash
python cs480_P01_AXXXXXXXX.py <ALGO> <FIRST> <MODE>
```

cs480_P01_AXXXXXXXX.py is the filename of your Python code.
<ALGO> specifies the algorithm used by the computer player:
1 for MiniMax.
2 for MiniMax with alpha-beta pruning.
<FIRST> specifies who begins the game:
X for the human player.
O for the computer player.
<MODE> is the mode in which the program operates:
1 for human (X) versus computer (O).
2 for computer (X) versus computer (O).

#Program Details

The Tic-Tac-Toe board is a 3x3 grid, with the cells numbered as follows:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Players can make a move corresponding to the number of the cell they want to mark.

When the program starts, it will display initial information including the algorithm chosen, who makes the first move, and the game mode.

The program will prompt the user for a move with a message like:

```bash
X's move. What is your move (possible moves at the moment are: <list of possible moves> | enter 0 to exit the game)?
```

If a human player's turn, an empty board will be displayed first. The user will be prompted to pick a move.

When the computer's turn, the program will display the chosen move and the number of search tree nodes generated, followed by the updated game board.

When the game ends, the program will display whether it's a win, loss, or tie.



