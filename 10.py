list_data = [10,20,30]
tuple_data = (10,20,30)
set_data = {10,20,30}
dict_data = {'b': 'zone b', 'a': 'zone a'}

val = 20 
 
if val in list_data and val in tuple_data:
    if 'b' in dict_data and not(val in set):
        print("Path A")
    else:
        print("Path B")
else:
    print("Path C")
