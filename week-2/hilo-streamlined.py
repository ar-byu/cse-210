import random
# Imports "random" module

class GameRound:
    # Constructs new game
    def __init__(self, game_state):
        # Initializes attributes
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.first_num = int(random.choice(cards))
        cards.remove(self.first_num)
        self.second_num = int(random.choice(cards))
        self.game_state = game_state

    def get_guess(self):
        # Retrieves guess from player
        print(f"The first number is: {self.first_num}")
        self.guess = input("Higher or lower? [h/l] ")
        self.compare()

    def compare(self):
        # Determines if guess is correct or not
        if (self.guess == "h" and self.second_num > self.first_num) or (self.guess == "l" and self.second_num < self.first_num):
            print("That's correct!")
            self.game_state.calculate_score(True)
        else:
            print("That's incorrect.")
            self.game_state.calculate_score(False)
       
class GameState:
    def __init__(self):
        self.score = 300
        self.times_played = 0

    def calculate_score(self, won):
        self.times_played += 1
        # Calculates what the player's new score should be
        if won:
            self.score += 100
        else:
            self.score -= 75

class GameMaster:
    def __init__(self):
        # Generates GameState
        self.game_state = GameState()

    def runGame(self):
        print("Welcome to High Card, Low Card! You will be given two random numbers between 1 and 13. You won't be able to see the second number. You can then guess if the second number is higher or lower than the first. Have fun!")

        while True:
            # Generates a new game while cont_game is set to True. Retrieves guess from player. Adds 1 to the amount of rounds played.
            # Calculates the score. Retrieves input from player to see if the game should continue. If the player does not want to
            # continue playing, displays the rounds played and sets continue_game to False.
            print()
            GameRound(self.game_state).get_guess()
            print(f"Your score is: {self.game_state.score}")
            print()
            cont_game = input("Play again? [y/n] ")
            print()
            if cont_game == "n":
                break
        print("Thanks for playing!")
        print(f"Rounds Played: {self.game_state.times_played}")

if __name__ == "__main__":
    GameMaster().runGame()