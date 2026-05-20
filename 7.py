banned_items = {'scissors', 'knife', 'lighter'}

baggage_weight = int(input("Enter the weight of your baggage : "))
items_in_baggage = input("Enter the name of the item in your baggage : ")
status = not items_in_baggage in banned_items
if  status and baggage_weight>=7: 
    print("You are allowed.")
else:
    print(f'The item {items_in_baggage} is a banned item. You are now allowed.')