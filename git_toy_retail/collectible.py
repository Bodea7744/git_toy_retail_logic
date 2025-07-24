class CollectibleToy:
    def __init__(self, name, category, rarity, price):
        self.name = name
        self.category = category
        self.rarity = rarity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.category}, {self.rarity}) – {self.price} RON"