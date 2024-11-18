CHESS_PIECES = {
    "pawn": [0, 8],
    "rook": [0, 2],
    "knight": [0, 2],
    "bishop": [0, 2],
    "queen": [0, 1],
    "king": [0, 1],
}


CHESS_SYMBOLS = {
    "pawn": 'p',
    "rook": 'r',
    "knight": 'k',
    "bishop": 'b',
    "queen": 'q',
    "king": 'K',
}


COLORS = {
    "regular": "\033[0m",
    "blue": "\033[34m",
    "red": "\033[31m",
    "green": "\033[32m",
}


def is_valid_position(pos):

    if len(pos) == 2 and pos[0] in 'abcdefgh' and pos[1] in '12345678':
        return True
    return False


def is_valid_piece(piece, chess_pieces):
    if piece in chess_pieces:
        return True
    return False

def get_possible_captures(all_pieces):
    white_piece = all_pieces[0][0]
    white_pos = all_pieces[0][1]
    black_pieces = all_pieces[1:]
    
    # reset chesspieces color
    for index, piece in enumerate(all_pieces[1:]):
        all_pieces[index + 1][2] = "regular"

    col, row = ord(white_pos[0]), int(white_pos[1])
    
    if white_piece == "rook":
        # Vertical, Up (1) and Down (-1)
        for direction in [1, -1]:
            for r in range(row + direction, 9 if direction == 1 else 0, direction):
                pos = f"{chr(col)}{r}"
                for index, (_, b_pos, _) in enumerate(black_pieces):
                    if b_pos == pos:
                        all_pieces[index + 1][2] = "red"
                        break
                else:
                    continue
                break
        
        # Horizontal, Right (1) and Left (-1)
        for direction in [1, -1]: 
            for c in range(col + direction, ord('h') + 1 if direction == 1 else ord('a') - 1, direction):
                pos = f"{chr(c)}{row}"
                for index, (_, b_pos, _) in enumerate(black_pieces):
                    if b_pos == pos:
                        all_pieces[index + 1][2] = "red"
                        break
                else:
                    continue
                break

    elif white_piece == "pawn":
        for index, (_, pos, _) in enumerate(black_pieces):
            b_col, b_row = ord(pos[0]), int(pos[1])
            if abs(b_col - col) == 1 and (b_row - row) == 1:
                all_pieces[index + 1][2] = "red"

    return all_pieces


def is_maximum_piece_reached(piece, chess_pieces):
    used, total = chess_pieces[piece]
    if used < total:
        return True
    else:
        return False
    

def create_chessboard():
    board = [["." for _ in range(8)] for _ in range(8)]
    return board


def print_board(board, pieces, symbols):

    for piece, pos, color in pieces:
        col = ord(pos[0]) - ord('a')
        row = int(pos[1]) - 1
        board[row][col] = COLORS[color] + symbols[piece] + COLORS["regular"]

    for row in reversed(board):
        print("  ", " ".join(row))
    print()


def print_message(text, color):
    print(f"{COLORS[color]} {text}{COLORS['regular']}")