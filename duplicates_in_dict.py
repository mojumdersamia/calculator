students = { 
    'alice': 101,
    'ben': 101,
    'robert':103,
    'lana':104
}

value_list = []
new = dict()

for key,value in students.items():
    #print('the value of', key, 'is', value)
    if value not in value_list:
        value_list.append(value)
        new[key] = value
print(new)





# another method by dict comprehension
new_value_list = {val:key for key,val in students.items() }
print(new_value_list)# making keys the value so that duplicates get dropped

final_list = {val:key for key, val in new_value_list.items()}
print(final_list)