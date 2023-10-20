import random


def choose_random_word():
    words = ["python", "programming", "hangman", "computer", "developer", "code"]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    word_to_guess = choose_random_word()
    guessed_letters = []
    attempts = 6


    print ("Welcome to Hangman!")


    while True:
        print("\nWord to guess: " + display_word(word_to_guess, guessed_letters))
        print("Attemts left: " + str(attempts))


        if display_word(word_to_guess, guessed_letters) == word_to_guess:
            print("Congratulations! You guessed the word: " + word_to_guess)
            break


        if attempts == 0:
            print("Out of attempts! The word was: " + word_to_guess)
            break


        guess = input("Guess a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue


        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue


        guessed_letters.append(guess)


        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess!")


if __name__ == "__main__":
    main()

     