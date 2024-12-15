class TurnManager:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0
        self.phases = ["ECONOMY", "REINFORCEMENT", "UNIT_MOVEMENT"]
        self.current_phase_index = 0

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_phase_index = 0

    def next_phase(self):
        self.current_phase_index = (self.current_phase_index + 1) % len(self.phases)

    def get_current_player(self):
        return self.players[self.current_player_index].name

    def get_current_phase(self):
        return self.phases[self.current_phase_index]
