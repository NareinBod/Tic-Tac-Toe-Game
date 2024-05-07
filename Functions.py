import random
# Creating a function to display the board
def display_board(board):
    print('\n' * 100)
    print(board[0], '|', board[1], '|', board[2])
    print('----------')
    print(board[3], '|', board[4], '|', board[5])
    print('----------')
    print(board[6], '|', board[7], '|', board[8])
# This Function takes a player input and assigns markers
def player_input():
    choice = ''
    while (choice != 'X') and (choice != 'O'):
        choice = input('Player 1, choose your marker (X or O): ').upper()
    player1 = choice
    player2 = 'O' if player1 == 'X' else 'X'
    return (player1, player2)
# This function places a marker on the board
def place_marker(board, marker, position):
    board[position] = marker
# This function checks if a player has won
def win_check(board, mark):
    # Check rows for a win
    if (board[0] == board[1] == board[2] == mark):
        return True
    elif (board[3] == board[4] == board[5] == mark):
        return True
    elif (board[6] == board[7] == board[8] == mark):
        return True
    # Check columns for a win
    elif (board[0] == board[3] == board[6] == mark):
        return True
    elif (board[1] == board[4] == board[7] == mark):
        return True
    elif (board[2] == board[5] == board[8] == mark):
        return True
    # Check diagonals for a win
    elif (board[0] == board[4] == board[8] == mark):
        return True
    elif (board[2] == board[4] == board[6] == mark):
        return True
    # If no winning pattern is found
    else:
        return False
# This function decides who goes first
def choose_first():
    return 'Player 1' if random.randint(0, 1) == 1 else 'Player 2'
# This function checks if a given space is available
def space_check(board, position):
    return board[position] == ' '
# This function checks if the board is full
def full_board_check(board):
    return all(not space_check(board, i) for i in range(9))
# This function asks for a player's choice and checks if it's valid
def player_choice(board):
    position = None
    while True:
        try:
            position = int(input('Choose a position from 0 to 8: '))
            if position in range(9) and space_check(board, position):
                break
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 8.")
    return position
# This function asks the player if they want to play again
def replay():
    choice = input('Do you want to play again? : ')

    return choice == 'Yes'

