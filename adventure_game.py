import time


def introduction():
    print("Welcome to the adventure game!")
    time.sleep(1)
    print("You find yourself in a dark forest.")
    time.sleep(1)
    print("Your goal is to make it through the forest safely.")
    time.sleep(1)
    print("Let's begin...\n")
    time.sleep(1)


def choose_path():
    print("You come to a fork in the road.")
    time.sleep(1)
    print("Will you go left or right? (Type 'left' or 'right')")


    choice = input().lower()


    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        choose_path()


def left_path():
    print("You chose to go left.")
    time.sleep(1)
    print("You come across a river. Do you swim across or look for a bridge? (Type 'swim' or 'bridge')")


    choice = input().lower()


    if choice == "swim":
        print("You attempt to swim across the river...")
        time.sleep(2)
        print("Oops! You got swept away by the current and drowned.")
        game_over()
    elif choice == "bridge":
        print("You find a bridge, cross it safely, and continue your journey.")
        continue_journey()
    else:
        print("Invalid choice. Please type 'swim' or 'bridge'.")
        left_path()

        #Add more options here


def right_path():
    print("You chose to go right.")
    time.sleep(1)
    print("You encounter a pack of wolves. Do you run or try to scare them away? (Type 'run' or 'scare')")


    choice = input().lower()


    if choice == "run":
        print("You run as fast as you can...")
        time.sleep(2)
        print("The wolves catch up to you, and you become their dinner.")
        game_over()
    elif choice == "scare":
        print("You make loud noises and try to scare the wolves away successfully.")
        continue_journey()
    else:
        print("Invalid choice. Please type 'run' or 'scare'.")
        right_path()


def continue_journey():
    print("You continue your journey deeper into the forest.")
    time.sleep(1)
    print("You encounter a friendly group of travelers who offer you food and guidance.")
    time.sleep(2)
    print("Congratulations! You have successfully made it through the forest. You win!")


def game_over():
    print("\nGame Over. Play again?")
    restart = input("Type 'yes' to play again or any other key to exit: ").lower()


    if restart == "yes":
        introduction()
        choose_path()
    else:
        print("Thank you for playing!")


if __name__ == "__main__":
    introduction()
    choose_path()