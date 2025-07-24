class ToyCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, toy):
        self.items.append(toy)

    def display_cart(self):
        print("\n🧸 Cart Contents:")
        for toy in self.items:
            print(f"• {toy}")
        print(f"Total: {self.calculate_total():.2f} RON")

    def calculate_total(self):
        return sum(toy.price for toy in self.items) 