# Write a script to check if the target key exists in inventory. If it exists, check
# if the target is not in restricted_zones and the value in inventory is greater
# than 0.
# Print dispatch item if all conditions pass. Print stock error if it fails the
# inner check, and invalid zone if it fails the outer check.

inventory = {
    'A1' : 50,
    'B2' : 0,
    'C3' : 10
}

restricted_zones = {'B2', 'Z9'}
target = 'B2'

if target in inventory:
    if not(target in restricted_zones) and inventory[target]>0:
        print("Dispatch item")
    else:
        print("Stock Error")
else:
    print("Invalid Zone")



