class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
        self.owned_territories = []
        self.available_units = 0
        self.coin_balance = 0

    def add_available_units(self, count):
        self.available_units += count

    def deploy_units(self, territory, count):
        # Logic to deploy n_units to some owned territory
        pass

    def choose_attack(self):
        # Logic for selecting which territory to attack
        pass

    def add_territory(self, territory):
        # Logic to add territory to owned list
        pass

    def remove_territory(self, territory):
        # Logic to remove territory from owned list
        pass

    def earn_income(self, amount):
        self.coin_balance += amount

    def spend_coin(self, amount):
        if self.coin_balance >= amount:
            self.coin_balance -= amount
            return True
        return False

    def describe(self):
        print("*****")
        print(
            f"Player {self.player_id}: {self.name} has {self.available_units} avilable units and {self.coin_balance} coins."
        )
