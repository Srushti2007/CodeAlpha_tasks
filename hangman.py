import random

# List of predefined words
words = ["apple", "chair", "robot", "snake", "plant"]

# Choose a random word
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {max_incorrect} incorrect guesses allowed.\n")

# Create the hidden version of the word (e.g., "_ _ _ _ _")
display_word = ["_"] * len(secret_word)

while incorrect_guesses < max_incorrect and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    # Check if letter is in the secret word
    if guess in secret_word:
        print("Correct!\n")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display_word[i] = guess
    else:
        print("Incorrect!\n")
        incorrect_guesses += 1

# Final outcome
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game over! The word was:", secret_word)
