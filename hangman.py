import random

# Word categories and their corresponding words
word_categories = {
    "animals": ["lion", "tiger", "bear", "monkey", "giraffe"],
    "countries": ["usa", "canada", "mexico", "france", "germany"],
    "movies": ["starwars", "avengers", "inception", "interstellar", "the Shawshank Redemption"]
}

# Hangman graphics
hangman_graphics = [
    """
    +--------+
    |       |
            |
            |
            |
            |
    =========""",
    """
    +--------+
    |       |
    O       |
            |
            |
            |
    =========""",
    """
    +--------+
    |       |
    O       |
    |       |
            |
            |
    =========""",
    """
    +--------+
    |       |
    O       |
   /|       |
            |
            |
    =========""",
    """
    +--------+
    |       |
    O       |
   /|\\     |
            |
            |
    =========""",
    """
    +--------+
    |       |
    O       |
   /|\\     |
   /        |
            |
    =========""",
    """
    +--------+
    |       |
    O       |
   /|\\     |
   / \\     |
            |
    ========="""
]

def draw_hangman(graphic, word, guessed_letters):
    print(graphic)
    print(" ".join([letter if letter in guessed_letters else "_" for letter in word]))

def play_game():
    print("Welcome to Hangman!")
    print("Choose a category:")
    for i, category in enumerate(word_categories.keys()):
        print(f"{i+1}. {category}")
    category_choice = int(input("Enter the number of your chosen category: "))
    category = list(word_categories.keys())[category_choice - 1]
    word = random.choice(word_categories[category])
    word_length = len(word)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    score = 0

    while incorrect_guesses < max_incorrect_guesses and "_" in [letter if letter in guessed_letters else "_" for letter in word]:
        draw_hangman(hangman_graphics[incorrect_guesses], word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed this letter!")
        elif guess in word:
            guessed_letters.append(guess)
            score += 1
        else:
            incorrect_guesses += 1
            guessed_letters.append(guess)
            print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

    draw_hangman(hangman_graphics[incorrect_guesses], word, guessed_letters)
    if "_" not in [letter if letter in guessed_letters else "_" for letter in word]:
        print(f"Congratulations! You guessed the word '{word}' with a score of {score}!")
    else:
        print(f"Sorry, you didn't guess the word '{word}'. Better luck next time!")

def main():
    play_game()
    while True:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            play_game()
        elif play_again == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()