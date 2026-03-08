import random

words = ["meltdown", "snowman", "winter", "frozen", "blizzard"]
secret_word = random.choice(words)

display_word = ["_"] * len(secret_word)
wrong_guesses = 0
max_wrong = 6

while "_" in display_word and wrong_guesses < max_wrong:

    print("Word:", " ".join(display_word))
    print("Wrong guesses:", wrong_guesses)

    guess = input("Guess a letter: ")

    if guess in secret_word:
        for index, letter in enumerate(secret_word):
            if letter == guess:
                display_word[index] = guess
    else:
        wrong_guesses += 1
        print("Incorrect!")

if "_" not in display_word:
    print("You won! The word was:", secret_word)
else:
    print("The snowman melted! The word was:", secret_word)
    