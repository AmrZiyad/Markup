# Create store inventory
items = ["pencil", "eraser", "notebook", "sharpener", "glue"]
stock_counts = [12, 0, 8, 5, 3]
inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full Inventory:", inventory)

# Filter items using a cleaner dictionary check
in_stock_items = [item for item, count in inventory.items() if count > 0]
print("Items In Stock:", in_stock_items)

# Shopping check
chosen_item = input("Which item do you want to buy? ")
if inventory.get(chosen_item, 0) == 0:
    print(f"{chosen_item} is out of stock or does not exist!")
    exit()

# Create prices and ask for a markup amount
prices = [10,5, 40, 15, 50]
markup = int(input("Enter the markup amount to every price: "))

#Apply the markup to every price using map()
marked_up_prices = list(map(lambda price: price + markup, prices))
print("Marked up prices:", marked_up_prices)