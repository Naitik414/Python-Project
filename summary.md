# Summary - Tic-Tac-Toe (PS 49)

**Name: Naitik Sahu 

**Class: SA-16
**ERP No. : RU-26-00824

## Project Overview

A two-player console Tic-Tac-Toe game in Python 3 on a 3 × 3 board. Players take turns (X first), the board is shown after every move, and the winner or a draw is announced. The board is a list of 9 cells, with separate functions for displaying the board, taking a move, and checking for a win or draw. All 8 winning lines are checked, and the game ends with "Play again? (y/n)".

## Difficulties and Solutions
- **Positions 1-9 vs list indexes 0-8:** converted with `board[pos - 1]`.
- **Invalid input crashing the game:** checked `isdigit()` and the 1-9 range before converting.
- **Turn changing after a wrong or taken move:** put the input check in a loop so the turn only changes after a valid move.
- **Eight separate win checks:** stored the lines in a `WINNING_LINES` list and looped over them.
- **Win on the 9th move reported as a draw:** check for a win first, then for a full board.

## Test Cases
Screenshots are in the `Screenshots/` folder (`testcase1.png` to `testcase4.png`).

| # | Moves / Input | Output |
|---|---------------|--------|
| 1 | X:1, O:4, X:2, O:5, X:3 | Player X wins! Winning line: 1-2-3 |
| 2 | X:1, O:2, X:3, O:5, X:4, O:6, X:8, O:7, X:9 | Board is full after 9 moves. It's a draw! No moves left. |
| 3 | `10`, `abc`, then O plays taken position 1 | Invalid position. Enter a number from 1 to 9. / Position 1 is already taken. Choose another position. |
| 4 | X:1, O:4, X:2, O:5, X:9, O:6, then `n` | Player O wins! Winning line: 4-5-6 / Thanks for playing! |

All four test cases give the expected output.
