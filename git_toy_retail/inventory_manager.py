# Inventory Manager – Controls collectible stock logic

class InventoryManager:
    def __init__(self):
        self.collectibles = []

    def add_collectible(self, collectible):
        self.collectibles.append(collectible)

    def display_info(self):
        for item in self.collectibles:
            print(item.display_info())

    def total_value(self):
        return sum(item.price * item.quantity for item in self.collectibles)

    def remove_collectible(self, name):
        self.collectibles = [item for item in self.collectibles if item.name != name]
        print(f"Collectible '{name}' has been removed.")