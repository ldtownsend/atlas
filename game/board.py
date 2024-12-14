from .territory import Territory


class Board:
    def __init__(self, name, territories):
        self.name = name
        self.territories = territories
        self._name_to_territory = {}
        self.adjacency_map = {}
        self._initialize_territories()

    def _initialize_territories(self):
        self._name_to_territory = {t.name: t for t in self.territories}
        self.adjacency_map = self._build_adjacency_map()

    def _build_adjacency_map(self):
        adjacency = {}
        for territory in self.territories:
            adjacency[territory.name] = territory.neighbors
        return adjacency

    def get_territory(self, name):
        return self.territories.get(name)

    def are_adjacent(self, territory_a, territory_b):
        # Check adjacency in adjacency map
        pass

    def list_adjacent_territories(self, territory):
        # Return a list of adjacent terrritory objects
        pass

    def describe(self):
        print("*****")
        print(f"Board Name: {self.name}")
        print(f"Territory Adjacency Map: {self.adjacency_map}")
