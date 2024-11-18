# Chess Capture Program

## Description

This program allows users to simulate a simple chess scenario where a single white chess piece attempts to capture one or more black chess pieces on a standard 8x8 chessboard. The program determines and displays which black pieces the white piece can potentially capture based on standard chess movement rules.

---

## Features

- **Interactive Input:**

  - User selects a white chess piece (`rook` or `pawn`) and places it on the board.
  - User adds up to 16 black regular chess pieces and positions them on the board.

- **Capture Calculation:**

  - The program determines which black pieces the white piece can capture based on its position and movement rules.
  - It highlights capturable pieces dynamically as the user adds them.

- **Board Visualization:**
  - The program displays the chessboard in the terminal, showing the positions of all pieces, including the white piece(blue color) and black pieces with different colors for easy identification(red color - can take, regular color - can not take).

---

## How to Use

1. Run the program.
2. **Input the White Piece:**
   - Enter the white piece's type and position in the format: `piece position`
     - Example: `rook a1` or `pawn d4`
   - The piece is placed on the board.
3. **Add Black Pieces:**

   - Enter black pieces one by one in the format: `piece position`
     - Example: `rook a5` or `bishop f7`
   - The program updates the board and displays the black pieces that the white piece can potentially capture.
   - The program does not allow to place piece in an already occupied position.
   - Enter `done` when you’ve finished adding black pieces.
   - At least one black piece has to be placed

4. **Capture Results:**
   - The program will highlight the black pieces that are capturable and display them in the terminal.

---

Board:
8 . . . . . . . .
7 . . . . . . . .
6 . . . . . . . .
5 r . . . . . . .
4 . . . . . . . .
3 . . . . . . . .
2 . . . . . . . .
1 . . . . . . . .
a b c d e f g h
