def build_board():
    board = [str(i) for i in range(1, 10)]
    return board


def print_board(board):
    """ Prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = board.copy()

    for i in range(len(board)):
        if board[i] == 'x':
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif board[i] == 'o':
            new_board[i] = BLUE + board[i] + LIGHT_GRAY

    row_format = ' {0} | {1} | {2} '
    print(LIGHT_GRAY)
    print(row_format.format(*new_board[:3]))
    print('-' * 11)
    print(row_format.format(*new_board[3:6]))
    print('-' * 11)
    print(row_format.format(*new_board[6:]))
    print(reset)


def is_legal(board, position):
    return board[position - 1] not in ['x', 'o']


def fill_spot(board, position, character):
    character = character.lower().strip()
    if character in ['x', 'o'] and is_legal(board, position):
        board[position - 1] = character


def winning_game(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    return any(board[a] == board[b] == board[c] for a, b, c in win_conditions)


def game_over(board):
    return winning_game(board) or all(space in ['x', 'o'] for space in board)


def get_winner(board):
    return "Player 1 (X)" if board.count('x') > board.count('o') else "Player 2 (O)" if winning_game(board) else None


def play(board):
    player1, player2 = 'x', 'o'
    turn = 1

    while not game_over(board):
        print_board(board)
        position = input(f"Player {1 if turn % 2 != 0 else 2}, choose a position (1-9): ")

        if position.isdigit():
            position = int(position)
            if 1 <= position <= 9 and is_legal(board, position):
                fill_spot(board, position, player1 if turn % 2 != 0 else player2)
                turn += 1
            else:
                print("Invalid move. Try again.")
        else:
            print("Please enter a number between 1 and 9.")

    print_board(board)
    winner = get_winner(board)
    print(f"Game over! {winner} wins!" if winner else "It's a tie!")

    if input("Do you want to play again? (yes or no) ").lower().startswith('y'):
        play(build_board())


def main():
    board = build_board()
    play(board)


if __name__ == '__main__':
    main()
