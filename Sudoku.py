import random

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def is_valid_move(board, row, col, num):
    # Check if the number is already in the same row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        

        # Cheeck if the number is in the same 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
                

        return True
    

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0 # Backtrack
                return False
    return True


def generate_sudoku(difficulty):
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)


    num_to_remove = 0
    if difficulty == "easy":
        num_to_remove = 25
    elif difficulty == "medium":
        num_to_remove = 45
    elif difficulty == "hard":
        num_to_remove = 60


    while num_to_remove > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            num_to_remove -= 1


    return board


def main():
    print("Welcome to Sudoku!")


    while True:
        print("\nSelect the difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Quit")


        choice = input()
        if choice == "4":
            print("Thanks for playing!")
            break


        difficulties = {
            "1": "easy",
            "2": "medium",
            "3": "hard"
        }


        if choice in difficulties:
            difficulty = difficulties[choice]
            sudoku_board = generate_sudoku(difficulty)
            print("\nHere's you Sudoku puzzle:")
            print_board(sudoku_board)


            if solve_sudoku(sudoku_board):
                print("\nSolved Sudoku:")
                print_board(sudoku_board)
                print("Congratulations! You've solved it!")
            else:
                print("Sorry, there's no solution for this Sudoku.")
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()