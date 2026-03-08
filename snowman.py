import random

words = ["meltdown", "snowman", "winter", "frozen", "blizzard"]
secret_word = random.choice(words)

display_word = ["_"] * len(secret_word)
wrong_guesses = 0
max_wrong = 6
guessed_letters = []

snowman_stages = [
    """
     _===_
    (.,.)
    ( : )
    ( : )
    """,
    """
     
    (.,.)
    ( : )
    ( : )
    """,
    """
     
    (.,.)
    ( : )
     
    """,
    """
     
    (.,.)
     
     
    """,
    """
     
     
     
     
    """,
    """
     
     
     
     
    """,
    """
     
     
     
     
    """
]

while "_" in display_word and wrong_guesses < max_wrong:
    print(snowman_stages[wrong_guesses])
    print("Word:", " ".join(display_word))
    print("Wrong guesses:", wrong_guesses)
    print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for index, letter in enumerate(secret_word):
            if letter == guess:
                display_word[index] = guess
    else:
        wrong_guesses += 1
        print("Incorrect!")

if "_" not in display_word:
    print("Congratulations, you saved the snowman!")
    print("The word was:", secret_word)
else:
    print(snowman_stages[wrong_guesses])
    print("The snowman melted! The word was:", secret_word)