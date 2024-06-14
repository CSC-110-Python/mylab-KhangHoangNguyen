class GroceryItemOrder:
    def __init__(self, quantity, price_per_unit):
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def cost(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"{self.quantity} items at ${self.price_per_unit} each"


class GroceryList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    @property
    def total_cost(self):
        return sum(item.cost() for item in self.items)


# Example items
item1 = GroceryItemOrder(4, 3.5)
item2 = GroceryItemOrder(2, 2.0)
item3 = GroceryItemOrder(1, 10.0)

# Create a GroceryList
my_list = GroceryList()

# Add items to the list
my_list.add(item1)
my_list.add(item2)
my_list.add(item3)

# Print out the items and their details
for idx, item in enumerate(my_list.items, start=1):
    print(f"Item {idx}: {item} - Total Cost: ${item.cost()}")

# Print total cost of all items
print("\nTotal Cost of all items:", my_list.total_cost)
