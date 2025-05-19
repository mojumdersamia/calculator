Numbers = list(range(1, 21))
for x in Numbers:
    print(x)


OneMillion = []
for i in range(1, 1000001):
    OneMillion.append(i)
    #print(OneMillion)

print(min(OneMillion))
print(max(OneMillion))
print(sum(OneMillion))

OddNumbers = list(range(1, 21, 3))
print(OddNumbers)

Multiples_of_threes = []
for value in range(3, 31, 3):
     Multiples_of_threes.append(value)
print(Multiples_of_threes)

Cubes = []
for num in range(1,11):
    cube = num ** 3
    Cubes.append(cube)
print(Cubes)

cubes = [value ** 3 for value in range(1, 11)]
print (cubes)
