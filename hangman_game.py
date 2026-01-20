import random

# List of words (original, not copied)
word_bank = [
    "algorithm",
    "function",
    "variable",
    "compiler",
    "internet"
]

# Select a random word
secret_word = random.choice(word_bank)

# Game state
correct_guesses = set()
wrong_guesses = set()
max_attempts = 6

print("Welcome to Hangman")
print("Guess the word one letter at a time.")

# Game loop
while len(wrong_guesses) < max_attempts:
    # Display current word progress
    progress = []
    for ch in secret_word:
        if ch in correct_guesses:
            progress.append(ch)
        else:
            progress.append("_")

    print("\nWord:", " ".join(progress))
    print("Wrong guesses:", ", ".join(sorted(wrong_guesses)))
    print("Attempts left:", max_attempts - len(wrong_guesses))

    # Check win condition
    if "_" not in progress:
        print("\nYou guessed the word correctly:", secret_word)
        print()
        break

    # Take input
    user_input = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(user_input) != 1 or not user_input.isalpha():
        print("Invalid input. Enter exactly one alphabet letter.")
        continue

    if user_input in correct_guesses or user_input in wrong_guesses:
        print("You already guessed that letter.")
        continue

    # Update guesses
    if user_input in secret_word:
        correct_guesses.add(user_input)
        print("Correct guess.")
    else:
        wrong_guesses.add(user_input)
        print("Wrong guess.")

# Lose condition
if len(wrong_guesses) == max_attempts:
    print("\nGame over. The correct word was:", secret_word)
    print()
