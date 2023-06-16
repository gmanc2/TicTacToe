import numpy as np  # import numpy
import random  # import random
import time  # import time for dramatic effect
import colorama  # import colorma encase its not installed in my instance I preinstalled with conda
from colorama import Fore, Style, init  # from colorama import

init()  # initialize colorama


def create_board():
    return np.full((3, 3), " ")  # create a 3x3 array filled with empty strings


def print_board(board):
    print("    1   2   3")  # print column headers
    print("  " + "-" * 13)  # print horizontal line
    for i, row in enumerate(board):  # loop for board
        colored_row = [
            # apply colors to each cell with statement to check for X and O so the color matches the palyers and computers color
            Fore.BLUE + cell + Style.RESET_ALL if cell == "X" else Fore.YELLOW + cell + Style.RESET_ALL if cell == "O" else cell
            for cell in row]
        print(f"{i + 1} | " + " | ".join(colored_row) + " |")  # print row with colors
        if i < len(board) - 1:  # print horizontal line for each column to separate them
            print("  " + "-" * 13)
    print()  # print an empty line for spacing


def get_player_move():
    while True:  # get the player input
        row = input("Enter your row choice (1-3): ").strip()
        col = input("Enter your column choice (1-3): ").strip()

        if not row.isdigit() or not col.isdigit():  # check to make sure they follow the rules
            print(
                Fore.RED + "Invalid input. Please enter a number between 1 and 3." + Style.RESET_ALL)
            continue

        row, col = int(row), int(col)  # change input to integer
        if 1 <= row <= 3 and 1 <= col <= 3:  # check to make sure they follow the rules and
            return row - 1, col - 1  # return 0-2 based row and column
        else:
            print(
                Fore.RED + "Invalid input. Please enter a number between 1 and 3 for both row and column." + Style.RESET_ALL)


def get_computer_move(board):  # computers move
    empty_cells = np.argwhere(board == " ")  # find empty cells
    return tuple(random.choice(empty_cells))  # randomly select an empty cell


def is_valid_move(board, move):  # check if the cell is empty
    row, col = move
    return board[row, col] == " "


def make_move(board, move, player):
    row, col = move
    board[row, col] = player  # update the board with the players symbol


def check_win(board, player):  # check for a win in rows, columns, or diagonals with numpy for simplicity
    for row in board:  # iterate through each row in the board and check if all elements in the row are equal to the players symbol X or O
        if np.all(row == player):
            return True
    for col in board.T:  # iterate through each column in the board except this time transpose it making columns into rows and check for players symbol X or O
        if np.all(col == player):
            return True
    if np.all(
            np.diag(board) == player):  # check if all elements in the main diagonal are equal to the player's symbol X or O
        return True
    if np.all(np.diag(np.fliplr(
            board)) == player):  # check if all elements in the anti-diagonal are equal to the player's symbol X or O
        return True
    return False


def main():  # Main
    board = create_board()  # create the empty board
    players = ["X", "O"]  # player and computer symbols
    current_player = 0  # index of the current player (0: player, 1: computer)

    print(Fore.GREEN + "Welcome to Tic-Tac-Toe! Player v.s. Random Computer Generator!" + Style.RESET_ALL)
    print(Fore.BLUE + "Player...." + Style.RESET_ALL)
    time.sleep(1)  # sleep for 1 second for dramatic effect
    print(Fore.RED + "versus!!!!..." + Style.RESET_ALL)
    time.sleep(2)  # sleep for 2 seconds for dramatic effect
    print(Fore.YELLOW + "RANDOM NUMBER GENERATOR!!!" + Style.RESET_ALL)
    print(Fore.BLUE + "Player is 'X'" + Fore.YELLOW + "Computer is 'O'" + Style.RESET_ALL)
    print_board(board)  # print the board

    while True:
        if current_player == 0:  # players turn
            move = get_player_move()
        else:
            move = get_computer_move(board)  # computers turn and tell them where the computer moved
            print(Fore.YELLOW + f"Computer move: {move[0] + 1}, {move[1] + 1}" + Style.RESET_ALL)

        if is_valid_move(board, move):  # check for valid move
            make_move(board, move, players[current_player])  # make the move
            print_board(board)  # reprint the board
            if check_win(board, players[current_player]):  # check win condition after each move
                print(
                    Fore.RED + f"{Fore.BLUE + 'Player (X)' + Style.RESET_ALL if current_player == 0 else Fore.YELLOW + 'Computer (O)' + Style.RESET_ALL}" + Fore.RED + " wins!" + Style.RESET_ALL)
                break
            elif np.all(board != " "):  # after all spaces are filled and no win condition is met it's a draw
                print(Fore.GREEN + "It's a draw!" + Style.RESET_ALL)
                break
            else:
                current_player = (current_player + 1) % 2  # switch the players
        else:
            print(
                Fore.RED + "Invalid move. That position is already taken." + Style.RESET_ALL)  # check for taken position
    while True: # have player choose if they want to play again or not with input validation
        play_again = input("Do you want to play again? (Y/N): ").strip().lower()
        if play_again == "y":
            main()
            break
        elif play_again == "n":
            print(Fore.CYAN + "Thanks for playing!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid input. Please enter Y or N." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
