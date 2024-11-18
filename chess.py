from chess_utils import *

def main():
    print("Choose a white piece (pawn or rook) and place it on the chessboard.")
    
    board = create_chessboard()

    # White piece and position
    while True:
        white_input = input("Enter white piece and position: ").strip().lower()
        try:
            white_piece, white_pos = white_input.split()
            if white_piece not in ("pawn", "rook"):
                print_message("Only 'pawn' and 'rook' are allowed as white pieces.", "red")
                continue
            if not is_valid_position(white_pos):
                print_message("Invalid position. Use format 'a1', 'h8', etc.", "red")
                continue
            break
        
        except ValueError:
            print_message("Input has to be in format '<piece> <position>', like: 'pawn a1'.", "red")
            
        except EOFError:
            print("\nGame canceled.")
    
    print_message(f"White {white_piece} placed at {white_pos}.", "green")
    
    # Black pieces and positions
    all_pieces = [[white_piece, white_pos, "blue"]]
    print("Add black pieces to the board. Enter 'done' to finish.")
    print("Use '<piece> <position>', like: 'rook b2'.")
    
    while len(all_pieces) < 17:
        black_input = input("Enter black piece and position: ").strip().lower()
        if black_input == "done":
            if len(all_pieces) == 1:
                print_message("You have add at least one black piece before finishing.", "red")
                continue
            break
        
        try:
            black_piece, black_pos = black_input.split()
            if not is_valid_piece(black_piece, CHESS_PIECES.keys()):
                print_message(f"Invalid chesspiece. Use: {list(CHESS_PIECES.keys())}", "red")
            
            if not is_valid_position(black_pos):
                print_message("Invalid position. Use format 'a1', 'h8', etc.", "red")
                continue
                
                continue
            if any(pos == black_pos for _, pos, _ in all_pieces):
                print_message("Another piece is already at this position.", "red")
                continue
            
            if not is_maximum_piece_reached(black_piece, CHESS_PIECES):
                print_message(f"Cannot add {black_piece}: maximum {black_piece}s is used.", "red")
                continue
            
            all_pieces.append([black_piece, black_pos, "regular"])
            CHESS_PIECES[black_piece][0] += 1
            print_message(f"Added {black_piece}({CHESS_SYMBOLS[black_piece]}) at {black_pos}", "green")
            

            all_pieces = get_possible_captures(all_pieces)
            print_board(board, all_pieces, CHESS_SYMBOLS)
            
        except ValueError:
            print_message("ValueError: Input has to be in format '<piece> <position>', like: 'pawn a1'.", "red")
            
        except EOFError:
            print("\nGame canceled.")
    
    print_message("\n Final board setup:", "green")
    print_board(board, all_pieces, CHESS_SYMBOLS)

    possible_takeoffs = []
    possible_takeoffs = [(piece, position) for piece, position, color in all_pieces if color == "red"]

    if len(possible_takeoffs) > 0:
        print_message("White can take these black positions:", "green")
        for piece, position in possible_takeoffs:
            print(f"  {piece} at {position}")
    else:
        print_message("There is no takeoffs for white.", "green")

if __name__ == "__main__":
    main()
