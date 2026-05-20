# Create a dictionary menu where Pizza is 15, Burger is 10, and Salad is 8. Set
# order = ‘Pizza’. Write a program that checks if the order exists as a key in
# the menu. If it does, print the price of that item; if not, print item not found.

menu = {
    'pizza':15,
    'burger':10,
    'salad':8
}

set_order = 'pizza'
if set_order in menu:
    print(f'The price of {set_order} is {menu[set_order]}')
else:
    print("Item not found in menu")
    