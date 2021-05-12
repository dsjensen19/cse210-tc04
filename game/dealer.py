from game.player import Player
import random

class Dealer:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        card_1 (int): Whether or not the player wants to keep playing.
        card_2 (int): The total number of points earned.
        can_has_player (bool)
        can_deal (bool): An instance of the class of objects known as player.
    """


    def __init__():
        self.card_1 = self.card_2 = 0
        self.player = player()
        

    def start_game(self):
        """ runs the main functions of the game in order
        1) draw first card
        2) show first card
        3) ask player higher or lower
        4) draw second card
        5) show second card 
        6) compare cards
        7) calculate score change and send to player
        8) ask player if they want to play again
        """
        while self.can_deal():

        

    def get_card(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Dealer): An instance of Dealer.
        """

        card = random.randint(1,13)
        return card

    def display_card(self, card, card_num):
        if card_num == 1:
            card_num_str = "first"
        else:
            card_num_str = "Second"
        card_str = card.String()
        if card == 11:
            card_str == "Jack"
        if card == 12:
            card_str == "Queen"
        if card == 13:
            card_str == "King"
        if card == 1:
            card_str == "Ace"

        print(f"The {card_num_str} card is a {card_str}.")
        
    def get_guess(self):
        """gets input from player
        Args:
            self (Dealer): An instance of Dealer.
        """
        guess = self.player.higher_or_lower

    def compare_cards(self, card_1,card_2, guess):
        #guess is boolean, if input = lower then Guess = False
        # if input = Higher then guess = True
        """
        Compares cards to determine higher_lower, 
        compares result with guess
        Args: 
            self: : An instance of Dealer.
            card_1: int
            card_2: int
            guess: bool
        """

        if guess:
            if card_1 == card_2:
                print(f"{card_1} is equal to {card_2}")
                return False
            elif card_1 > card_2:
                print(f"{card_1} is bigger than {card_2}")
                return False
            elif card_1 < card_2:
                print(f"{card_2} is bigger than {card_1}")
                return True
        if not guess:
            if card_1 == card_2:
                print(f"{card_1} is equal to {card_2}")
                return False
            elif card_1 > card_2:
                print(f"{card_1} is bigger than {card_2}")
                return True
            elif card_1 < card_2:
                print(f"{card_2} is bigger than {card_1}")
                return False
    def can_deal():
        return true