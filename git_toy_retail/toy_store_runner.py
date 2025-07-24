from collectible import CollectibleToy
from toy_cart import ToyCart

print("🧸 Welcome to Collectible Toy Store!")

# Define some collectible toys
beyblade = CollectibleToy("Beyblade Burst", "Battle", "Rare", 79.99)
pokemon = CollectibleToy("Pokemon Plush", "Plush", "Common", 49.50)
bakugan = CollectibleToy("Bakugan Starter", "Strategy", "Epic", 64.25)

# Initialize the cart
cart = ToyCart()
cart.add_to_cart(beyblade)
cart.add_to_cart(pokemon)
cart.add_to_cart(bakugan)

# Display contents
cart.display_cart()