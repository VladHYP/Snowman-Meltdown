import random
from ascii_art import STAGES

WORDS = ["meltdown", "snowman", "winter", "frozen", "blizzard"]


def get_random_word():
    """Selects and returns a random secret word."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the hidden word."""
    print(STAGES[mistakes])

    display_word = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_word.append(letter)
        else:
            display_word.append("_")

    print("Word:", " ".join(display_word))
    print("Wrong guesses:", mistakes)
    print("Guessed letters:", " ".join(guessed_letters))


def play_game():
    """Runs one full game of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Incorrect!")

        word_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_guessed = False
                break

        if word_guessed:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations, you saved the snowman!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("The snowman melted! The word was:", secret_word)