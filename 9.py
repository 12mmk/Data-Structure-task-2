ram_items = {'ball', 'bat', 'wicket'}
laxman_items = {'bat'}

common_items = ram_items.intersection(laxman_items)

if common_items:
    print(f'{common_items} is the common item between ram and laxam')
else:
    print('Ram and Laxman do not have any common items')
    