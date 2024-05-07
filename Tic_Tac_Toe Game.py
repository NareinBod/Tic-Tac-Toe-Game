#Importing code from Functions file
import Functions as Func
# Main Code
print("WELCOME TO TIC TAC TOE")

while True:
    # Setup new board and players
    board = [' '] * 9
    player1_marker, player2_marker = Func.player_input()

    # Decide who goes first
    turn = Func.choose_first()
    print(f"{turn} goes first.")

    # Determine if the game should start
    game_ready = input("Are you ready to play the game? (Y or N): ").strip().upper()
    game = game_ready == "Y"

    # Main game loop
    while game:
        if turn == 'Player 1':
            # Player 1's turn
            Func.display_board(board)
            position = Func.player_choice(board)
            Func.place_marker(board, player1_marker, position)

            if Func.win_check(board, player1_marker):
                Func.display_board(board)
                print("PLAYER 1 HAS WON! CONGRATULATIONS!")
                break  # Exit the game loop
            elif Func.full_board_check(board):
                Func.display_board(board)
                print("IT'S A TIE!")
                break  # Exit the game loop
            else:
                turn = 'Player 2'  # Switch turn
        else:
            # Player 2's turn
            Func.display_board(board)
            position = Func.player_choice(board)
            Func.place_marker(board, player2_marker, position)

            if Func.win_check(board, player2_marker):
                Func.display_board(board)
                print("PLAYER 2 HAS WON! CONGRATULATIONS!")
                break  # Exit the game loop
            elif Func.full_board_check(board):
                Func.display_board(board)
                print("IT'S A TIE!")
                break  # Exit the game loop
            else:
                turn = 'Player 1'  # Switch turn

    if not Func.replay():
        break  
