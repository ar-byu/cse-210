import random
# Imports "random" module

class GameRound:
    # Constructs new game
    def __init__(self):
        # Initializes attributes
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.first_num = int(random.choice(cards))
        cards.remove(self.first_num)
        self.second_num = int(random.choice(cards))
        self.guess = None

    def get_guess(self):
        # Retrieves guess from player
        print(f"The first number is: {self.first_num}")
        self.guess = input("Higher or lower? [h/l] ")
        self.compare(self.guess)

    def compare(self, guess):
        # Determines if guess is correct or not
        if (guess == "h" and self.second_num > self.first_num) or (guess == "l" and self.second_num < self.first_num):
            print("That's correct!")
        else:
            print("That's incorrect.")
        print(f"The card was: {self.second_num}")
       
class GameState:
    continue_game = True
    def __init__(self):
        # Sets continue_game to true by default whenever a new GameState is constructed
        continue_game = True

def calculate_score(score, guess, number1, number2):
    # Calculates what the player's new score should be
    if (guess == "h" and number2 > number1) or (guess == "l" and number2 < number1):
        score += 100
        return score
    elif (guess == "h" and number2 < number1) or (guess == "l" and number2 > number1):
        score -= 75
        return score

        
def main():
    # Generates a GameState. Sets score to 300 and the amount of rounds played to 0.
    game_state = GameState()
    score = 300
    times_played = 0
    print("Welcome to High Card, Low Card! You will be given two random numbers between 1 and 13. You won't be able to see the second number. You can then guess if the second number is higher or lower than the first. Have fun!")

    while game_state.continue_game:
        # Generates a new game while continue_game is set to True. Retrieves guess from player. Adds 1 to the amount of rounds played.
        # Calculates the score. Retrieves input from player to see if the game should continue. If the player does not want to
        # continue playing, displays the rounds played and sets continue_game to False.
        print()
        new_game = GameRound()
        new_game.get_guess()
        times_played += 1
        score = calculate_score(score, new_game.guess, new_game.first_num, new_game.second_num)
        print(f"Your score is: {score}")
        print()
        cont_game = input("Play again? [y/n] ")
        print()
        if cont_game == "n":
            print("Thanks for playing!")
            print(f"Rounds Played: {times_played}")
            game_state.continue_game = False
            
    

if __name__ == "__main__":
    main()
