
import random

# Word list
WORDS = [
    "PYTHON", "COMPUTER", "PROGRAMMING", "DEVELOPER",
    "KEYBOARD", "INTERNET", "SOFTWARE", "DATABASE",
    "SECURITY", "NETWORK", "HANGMAN", "NOTEBOOK"
]

# Hangman stages
HANGMAN_STAGES = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

MAX_ATTEMPTS = 6

def show_word(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("\n===== HANGMAN GAME =====")
    print("Guess the hidden word!")
    print("You have 6 incorrect attempts.")
    print("Type EXIT to quit.\n")

    while wrong_guesses < MAX_ATTEMPTS:

        print(HANGMAN_STAGES[wrong_guesses])
        print("Word:", show_word(secret_word, guessed_letters))
        print("Guessed letters:", sorted(guessed_letters))
        print("Remaining attempts:", MAX_ATTEMPTS - wrong_guesses)

        guess = input("\nEnter one letter: ").strip().upper()

        if guess == "EXIT":
            print("Thanks for playing!")
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won!")
            print("The word was:", secret_word)
            return

    print(HANGMAN_STAGES[MAX_ATTEMPTS])
    print("\nGame Over!")
    print("The correct word was:", secret_word)

if __name__ == "__main__":
    while True:
        play_game()

        again = input("\nPlay again? (yes/no): ").strip().lower()

        if again not in ("yes", "y"):
            print("Thank you for playing Hangman!")
            break