import random

def generate_code():
    return [random.choice(['A', 'B', 'C', 'D', 'E', 'F']) for _ in range(4)]

def evaluate_guess():
    correct_position = sum(1 for i, j in zip(secret_code, user_guess) if i == j)
    correct_elements = sum(min(secret_code.count(x), user_guess.count(x)) for x in set(user_guess))
    return correct_position, correct_elements - correct_position

def display_board(attempts, feedback):
    print(f"\nAttempts left: {10 - attempts + 1}")
    for fb in feedback:
        print(" ".join(fb))

def code_breaker_game():
    secret_code = generate_code()
    attempts = 0
    feedback_history = []

    print("Welcome to the Code Breaker Game!")
    print("Try to guess the secret code (A, B, C, D, E, F).")

    while attempts < 10:
        user_guess = list(input("Enter your guess (4 letters): ").upper())

        if len(user_guess) != 4 or any(letter not in ['A', 'B', 'C', 'D', 'E', 'F'] for letter in user_guess):
            print("Invalid input. Please enter a valid guess.")
            continue

        correct_position, correct_elements = evaluate_guess(secret_code, user_guess)
        feedback = ['X' if i < correct_position else '0' if i <correct_position + correct_elements else '-' for i in range(4)]
        feedback_history.append(feedback)

        display_board(attempts, feedback_history)


        if correct_position == 4:
            print("Congratulations! You cracked the code!")
            break

        attempts += 1

    if correct_position < 4:
        print(f"\nGame over. The secret code was {' '.join(secret_code)}")


code_breaker_game()