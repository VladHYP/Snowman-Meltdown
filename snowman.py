import random

words = ["meltdown", "snowman", "winter", "frozen", "blizzard"]
secret_word = random.choice(words)

display_word = ["_"] * len(secret_word)

print("Word:", " ".join(display_word))