# Obstruction - AI vs Player
A Python implementation of the classic strategy game Obstruction, where a human player competes against an AI opponent on a grid-based board.

[Game Rules](http://www.papg.com/show?2XMX)


## Game Description

- Obstruction is a turn-based strategy game played on a grid. Players take turns placing a marker on empty cells.
- Once a move is made, the selected cell and all adjacent cells (including diagonals) become blocked.
- The player who cannot make a move loses.


## AI Strategy

The AI is implemented using a heuristic-based approach with move simulation and it applies a set of decision rules:

### Winning move detection
- The AI checks if there is a move that immediately leads to a win by simulating the board state.
### Blocking strategy
- If no winning move is found, the AI evaluates possible opponent moves and avoids positions that would allow the player to win.
### Fallback random move
- If no strategic move is available, the AI selects a valid move at random.

This approach ensures a balance between efficiency and intelligent gameplay.


## Features

- Player vs AI gameplay
- Heuristic-based AI opponent
- Move simulation for decision making
- Grid-based rule enforcement
- Turn-based system


## Technologies Used

- Python
- Object-Oriented Programming
- Game logic & state simulation
