from game.player import Player
import random

class Dealer:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        card_1 (int): the value of the first card
        card_2 (int): the value of the second card
        can_deal (bool): weather or not to deal antother round
        player(player): the player object
    """


    def __init__(self):
        self.card_1 = 0
        self.card_2 = 0
        self.player = Player()
        self.guess = False
        self.can_deal = True

        
    
    def start_game(self):
        """
        runs the take turn function untill the game is over
        """
        while self.can_deal:
            self.take_turn()

    def take_turn(self):
        """ runs the main functions of the game in order
        1) draw first card
        2) show first card
        3) ask player higher or lower
        4) draw second card
        5) show second card 
        6) compare cards
        7) calculate score change and send to playerf
        8) has the player print their score
        9) ask player if they want to play again
        """
    
        self.card_1 = self.get_card()
        self.display_card_1()
        guess = self.player.higher_lower()
        self.card_2 = self.get_card()
        self.display_card_2()
        self.compare_cards(guess)
        self.player.print_score()
        if self.player.score > 0:
            self.can_deal = self.player.keep_playing()
            print("\n")
        else:
            self.can_deal = False
            print("Game overThanks for playing!")

    def get_card(self):
        """Generates a random card out of a deck.

        Args:
            self (Dealer): An instance of Dealer.
        """

        card = random.randint(1,13)
        return card

    #i made this 
    """streamline the printing of card 1"""
    def display_card_1(self):
        print(f"Your first card is {self.get_card_str(self.card_1)}")
    #i made this
    """streamline the printing of card 2"""
    def display_card_2(self):
        print(f"Your first card is {self.get_card_str(self.card_2)}") 

    #
    #note
    #I want to change this to be a little simpler
    #by not having inputs or outputs
    #
    def get_card_str(self, card):

        """
        gets the string for the card number
        Ace, 2-10, Jack, Queen, King
        """
        card_str = str(card)
        if card == 11:
            card_str = "Jack"
        if card == 12:
            card_str = "Queen"
        if card == 13:
            card_str = "King"
        if card == 1:
            card_str = "Ace"
            
        return card_str


        
       
    def get_guess(self):
        """gets input from player
        Args:
            self (Dealer): An instance of Dealer.
        """
        guess = self.player.higher_or_lower

    #
    #note
    #I want to change this to be mor simple
    #by not having inputs 
    # and instead of outputs just change the players score.
    #
    def compare_cards(self, guess):
        """guess is boolean, if input = lower then Guess = False
        if input = Higher then guess = True
        """
        
        """
        Compares cards to determine higher_lower, 
        compares result with guess
        Args: 
            self: : An instance of Dealer.
            self.card_1: int
            self.card_2: int
            guess: bool
        """
        card_str_1 = self.get_card_str(self.card_1)
        card_str_2 = self.get_card_str(self.card_2)
        if guess: 
            if self.card_1 == self.card_2:
                print(f"{card_str_1} is equal to {card_str_2}")
                self.player.score -= 75
            elif self.card_1 > self.card_2:
                print(f"{card_str_1} is higher than {card_str_2}")
                self.player.score -= 75
            elif self.card_1 < self.card_2:
                print(f"{card_str_1} is lower than {card_str_2}")
                self.player.score += 100
        if not guess:
            if self.card_1 == self.card_2:
                print(f"{card_str_1} is equal to {card_str_2}")
                self.player.score -= 75
            elif self.card_1 > self.card_2:
                print(f"{card_str_1} is higher than {card_str_2}")
                self.player.score += 100
            elif self.card_1 < self.card_2:
                print(f"{card_str_1} is lower than {card_str_2}")
                self.player.score -= 75