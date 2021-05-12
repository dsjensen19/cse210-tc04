class Player():
    def __init__(self):
        self.score = 300
    def keep_playing(self):
        return False
    def higher_lower(self):
        return True
    def print_score(self):
        print(self.score)