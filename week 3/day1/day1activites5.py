shopping_list = [
    "cheese",
    "beans",
    "crisps",
    "milk",
    "apples"
]

at_the_shops = [
    "pears",
    "jams",
    "cheese",
    "apples",
    "bread", 
    "tuna",
    "crisps"
]

# Iterate over each item in the shopping list
for item in shopping_list:
    # Check if the item is in the at_the_shops list
    if item in at_the_shops:
        print(f"{item} is available at the shops.")
    else:
        print(f"{item} is not available at the shops.")

