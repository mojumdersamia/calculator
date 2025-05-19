dict1 = {1: 'Bob', 2:'Alice', 3: 'Rayne'}
print(dict1[2])

name = dict1.get(3)
print(name)

for i in dict1.values():
    print(i)
for i in dict1.keys():
    print(i)
for i in dict1.items():
    print(i)



dict2 = {1 : ['bob', 5, '45kg'], 2 : ['alice', 6, '60kg']}
weight = dict2.get(int(input('Enter participant number: ')))
print (weight[2])

# key must be unique

