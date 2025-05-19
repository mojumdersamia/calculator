# map (function, iterator)
name = ['1', '2', '3']
print(list(map(int, name)))

#filter filtrates what is wanted
even_number = list(filter(lambda x: x % 2 == 0, name))
print(even_number)