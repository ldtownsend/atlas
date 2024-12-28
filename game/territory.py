class Territory:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.owner = None
        self.units = 0
        self.units_per_round = 1
        self.coins_per_round = 1
        # self.buildings = []

    def add_units(self, count):
        self.units += count

    def remove_units(self, count):
        self.units -= count

    def change_owner(self, new_owner):
        self.owner = new_owner

    def add_building(self, building):
        pass
