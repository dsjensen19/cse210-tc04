class Player():
    """A code template for the player of the game. Decisons are made by whoever is playing the game.
    """
    def __init__(self):
        self.score = 300

    def keep_playing(self):
        return False
        
        
    def higher_lower(self):
        """This program recieves input from the user of their guess and returns True is their guess is 
        higher and False if their guess is lower"""
        while True:
            guess = str(input("Higher or Lower? [h/l]"))
            if (guess == "h"):
                return True
            elif (guess == "l"):
                return False
            else:
                print("Please enter a valid guess")
                
        return True
        
    def print_score(self):
        """This program prints the score to the user
        """
        print(f"Your score is {self.score}")
