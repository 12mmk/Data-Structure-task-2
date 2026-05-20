#  Write a program to change shyam salary to 8500 in the following dictionary.
# Given:

sample_dict = {
    'emp1' : {'name':'john','salary':7500},
    'emp2' : {'name':'emma','salary':8000},
    'emp3' : {'name':'shyam','salary':500}


}

sample_dict['emp3'].update({'salary':8500})

print(sample_dict)