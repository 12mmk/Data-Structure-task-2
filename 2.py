# define shopping list and bought assests
# compute the set difference to identify un bought items. 
# if items remain print them 
# if the idfference is empty print shopping 

shopping_list = {"milk", "bread", "eggs"}
bought_assets =  {"bread", "eggs"}


bought = shopping_list.difference(bought_assets)

if bought:
    print("You still need to buy: ", bought)
else:
    print("You have bought everything on your shopping list!")

    