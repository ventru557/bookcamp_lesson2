# Take input of an item the user wants to purchase
item = input("what is the iteam you want to purchase?")

# Ask how much the item costs and cast it as a number.
# What type of number should it be cast as?
cost = float(input("what is cost of the" + item + "?"))

# Ask what quantity of the item should be purchased and cast it as a number.
# What type of number should it be cast as?
quantity = int(input("How many" + item + "do you want to buy?"))

# Print the item cost along with its data type
print("Cost of each item is", cost, "data type of cost",type(cost))

# Print the item quantity along with its data type
print("how many items are we purchasing", quantity, "data type of quantity is ", type(quantity))

# Print results
print(
    "Item I want to buy is ", item, 
    "How many I want to buy", quantity, 
    "cost of each item", cost
)