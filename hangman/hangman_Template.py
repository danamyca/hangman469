import random

# ASCII Art stages for Hangman
stages = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

print("Hangman game started successfully!")

word_list = ["python", "hangman", "challenge", "code", "programming", "developer"]
word = random.choice(word_list)
attempts = 6
guessed_letters = []

while attempts > 0:
    display_word = ""
    for letter in word:
        display_word += (letter if letter in guessed_letters else "_") + " "

    print(stages[attempts])
    print(f"Word: {display_word.strip()}")

    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You've correctly guessed '{word}'!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("Letter already guessed.")
        else:
            guessed_letters.append(guess)
            if guess not in word:
                attempts -= 1
                print(f"'{guess}' is not in the word. Attempts left: {attempts}")
            else:
                print(f"Good! '{guess}' is correct.")
    else:
        print("Invalid input. Enter a single letter.")
else:
    print(stages[0])
    print(f"Game Over! The word was '{word}'.")

print("Thanks for playing!")
