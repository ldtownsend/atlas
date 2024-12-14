from .board import Board
from .territory import Territory
from .player import Player
from .turn_manager import TurnManager


class Game:
    def __init__(self):
        self.players = []
        self.board = None
        self.turn_manager = None
        self.round_number = 0
        self.game_type = "TOTAL CONTROL"

    def initialize_game(self):
        self.players = self._create_players()
        self.board = self._create_board()

    def _create_players(self):
        # Temporary Hardcode
        first_matchup = [
            Player(player_id=1, name="Luke"),
            Player(player_id=2, name="Steve"),
        ]

        for player in first_matchup:
            player.add_available_units(10)
            player.earn_income(10)

        return first_matchup

    def _create_board(self):
        # Temporary Hardcode
        mimal = [
            Territory(name="Minnesota", neighbors=["Iowa"]),
            Territory(name="Iowa", neighbors=["Minnesota", "Missouri"]),
            Territory(name="Missouri", neighbors=["Iowa", "Arkansas"]),
            Territory(name="Arkansas", neighbors=["Missouri", "Louisiana"]),
            Territory(name="Louisiana", neighbors=["Arkansas"]),
        ]

        return Board("Mimal", mimal)

    def start(self):
        self.main_loop()

    def main_loop(self):
        while not self.check_winner():
            self.round_number += 1
            current_player = self.turn_manager.get_current_player()

            # other stuff happens
            self.turn_manager.next_player()

        self.end_game()

    def check_winner(self):
        # if self.game_type == "TOTAL CONTROL":
        # Implement logic to if a player has won
        # If all of the territories are owned by 1 player,
        pass

    def end_game():
        # Implement End Game logic
        pass
