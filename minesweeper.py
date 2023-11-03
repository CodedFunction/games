import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def create_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mine_positions = random.sample(range(rows * cols), mines)

    for position in mine_positions:
        row, col = divmod(position, cols)
        board[row][col] = '*'

        return board


def count_adjacent_mines(board, row, col):
    mines = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == '*':
                mines += 1
    return mines

def reveal(board, revealed, row, col):
    if revealed[row][col]:
        return

    revealed[row][col] = True
    if board[row][col] == ' ':
        for r in range(row - 1, row + 2):
            for c in range(col - 1, row + 2):
                if 0 <= r < len(board)and 0 <= c < len(board[0]):
                    reveal(board, revealed, r, c)

def main():
    rows, cols, mines = 8, 8, 10
    board = create_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]

    print_board(revealed)
    while True:
        try:
            row, col = map(int, input("Enter row and column (e.g, 2 3): ").split())
        except ValueError:
            print("Invalid input. Please enter row and column as space-seperated integers.")
            continue
    
        if not (0 <= row < rows and 0 <= col < cols):
            print("Row and column must be within the board boundaries.")
            continue

        if revealed[row][col]:
            print("You've already revealed this cell.")

        if board[row][col] == '*':
            print("Game over! You hit a mine.")
            break

    num_mines = count_adjacent_mines(board, row, col)
    revealed[row][col] = True
    print_board(revealed)

    if num_mines == 0:
        reveal(board, revealed, row, col)
        print_board(revealed)


if __name__ == "__main__":
    main()