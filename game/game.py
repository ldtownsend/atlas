from .board import Board
from .territory import Territory
from .player import Player
from .turn_manager import TurnManager

import streamlit as st


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
        self.turn_manager = self._create_turn_manager()

        if "round_number" not in st.session_state:
            st.session_state["round_number"] = 0

    def _create_players(self):
        # Temporary Hardcode
        first_matchup = [
            Player(player_id=1, name="Ellie"),
            Player(player_id=2, name="Bo"),
        ]

        if "Players" not in st.session_state:
            st.session_state["Players"] = []

        for player in first_matchup:
            player.add_available_units(10)
            player.earn_income(10)

            if f"Player-{player.name}" not in st.session_state:
                st.session_state[f"Player-{player.name}"] = {
                    "name": player.name,
                    "available_units": player.available_units,
                    "coin_balance": player.coin_balance,
                }

                st.session_state["Players"].append(f"Player-{player.name}")

        if "current_player" not in st.session_state:
            st.session_state["current_player"] = st.session_state["Players"][0]

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

        board = Board("Mimal", mimal)

        if "Territories" not in st.session_state:
            st.session_state["Territories"] = []

        for territory in board.territories:

            if territory.name not in st.session_state["Territories"]:
                st.session_state["Territories"].append(territory.name)

            if f"Territory-{territory.name}" not in st.session_state:
                st.session_state[f"Territory-{territory.name}"] = {
                    "name": territory.name,
                    "neighbors": territory.neighbors,
                    "owner": territory.owner,
                    "units": territory.units,
                    "units_per_round": territory.units_per_round,
                }

        return board

    def _create_turn_manager(self):
        return TurnManager(players=self.players)

    # def _set_board(self):

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
