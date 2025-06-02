original_list = { 
    "gfg": 10,
    "for": 10,
    "geeks": 20,
    "is": 15,
    "best": 20
}

value_list = []
new = dict()

for key,value in original_list.items():
    
    if value not in value_list:
        value_list.append(value)
        new[key] = value
print(new)