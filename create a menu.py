# Create a tuple containing the names of menu sections:
# snacks, meals, drinks, and dessert.
menu_selection =("snacks","meals","drinks","dessert")

# Print the tuple.
print(menu_selection)

# Create a list of items for one of the menu sections.
snacks = ["chips", "biscuts","waffers"]
meals = ["burger n fries", "pasta", "pizza"]
drinks = ["coke", "pepsi", "scotch"]
dessert = ["ice cream", "cake", "pastries"]

# Create a list of prices for each of the menu items in the previous list.
snacks_price = [3.99, 4.50, 3]

# Ask a user to input a new item and append it to the relevant list.
i = input("what is the new item to the menu: ")
snacks.append(i)

# Ask a user to input the price of the new item, referenced using list indexing
# and append it to the relevant list.
i = float(input("what is the price of the new item? "))
snacks_price.append(i)

# Print the menu and prices.
print(snacks)
print(snacks_price)

# Ask the user which item to remove from the menu.
remove_item = input("which item do you want to remove? ")

# Find the index of the item and save it as a variable.
index = snacks.index(remove_item)

# Remove the item from the menu list using remove().
snacks.remove(index)

# Remove the item from the prices list using pop().
snacks_price.pop(index)

# Print the menu and prices again to confirm removal.
print(snacks)
print(snacks_price)

# Find the most expensive price on the menu.
print(f"Most expensive: {max(snacks_price)}")

# Find the cheapest price on the menu.
print(f"Cheapest : {min(snacks_price)}")

# Find the cost if someone bought every item on the menu.
print(f"Total cost: {sum(snacks_price)}")

# Confirm that the menu and prices lists are the same length.
print(
    f"The menu length is {len(snacks)} and the prices length is"
    + str(len(snacks_price))
)