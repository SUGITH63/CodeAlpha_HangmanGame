import random

class HangmanGame:
    def __init__(self):
        self.word_categories = {
            "PEAKY BLINDERS": ["arthur shelby", "thomas shelby", "john shelby", "fin shelby", "ada shelby", "polly "],
            "MOVIES": ["inception", "interstellar", "django unchained", "shawshank redemption", "pulp fiction"],
            
        }
        self.current_category = None
        self.word_to_guess = None
        self.guessed_letters = []
        self.lives = 6
        self.score = 0

    def choose_category(self):
        print("Choose a category:")
        for category in self.word_categories:
            print(category)
        selected_category = input().upper()

        if selected_category in self.word_categories:
            self.current_category = selected_category
            self.word_to_guess = random.choice(self.word_categories[selected_category])
        else:
            print("Invalid category. Choosing a default category.")
            self.current_category = "PEAKY BLINDERS"
            self.word_to_guess = random.choice(self.word_categories[self.current_category])

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter.lower() in self.guessed_letters or letter == " ":
                display += letter
            else:
                display += "_"
        return display

    def display_hangman(self):
        
        pass

    def play_round(self):
        guess = input("Guess a letter: ").lower()

        if guess == "hint":
            self.lives -= 1
            print(f"Hint: {random.choice(self.word_to_guess.split())}")
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            print("You've already guessed that letter. Try again.")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word_to_guess:
            self.lives -= 1
            print(f"Incorrect! Lives: {self.lives}")
            print(self.display_hangman())
        else:
            self.score += 10  
            print("Correct! Score:", self.score)

        current_display = self.display_word()
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You guessed the word.")
            print("Final Score:", self.score)
            return True

        return False

    def start_game(self):
        print("Welcome to Hangman!")
        self.choose_category()
        print(f"THEME: {self.current_category}")
        print(self.display_word())

        while self.lives > 0:
            if self.play_round():
                break

        if "_" in self.display_word():
            print(f"Sorry, you ran out of attempts. The word was '{self.word_to_guess}'.")
            print("Final Score:", self.score)

if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.start_game()
