class Player:
    def __init__(self, letter):
        """Player: O or X"""
        self.letter = letter
    def get_move(self, game):
        pass
class RandomComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
    def get_move(self, game):
        pass
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        pass