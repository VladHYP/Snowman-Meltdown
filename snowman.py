import random

words = ["meltdown", "snowman", "winter", "frozen", "blizzard"]
secret_word = random.choice(words)

display_word = ["_"] * len(secret_word)

while "_" in display_word:

    print("Word:", " ".join(display_word))

    guess = input("Guess a letter: ")

    for index, letter in enumerate(secret_word):
        if letter == guess:
            display_word[index] = guess

print("Congratulations! You guessed the word:", secret_word)