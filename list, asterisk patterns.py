Numbers = [5, 10, 15, 20, 25]

for i in Numbers :
    sqr = i ** 2
    print(f'the square of {i} is : {sqr}' )

sqrlist = []
for x in Numbers:
    sqrlist.append(x*x)
print (sqrlist)

#(from, to, step)
Numbers2 = list(range(1,6,2))
print (Numbers2)


sqr2 = []
for value in range(5, 36, 5):
    square = value**2
    sqr2.append(square)
print(sqr2)

#list comprehension
squares = [value ** 2 for value in range(5, 36, 5)]
print (squares)




Stu_list = ['bob', 'alice', 'amena']
i = 0
while i< len(Stu_list):
    print (Stu_list[i])
    i = i + 1
    if Stu_list[i] == "alice":
        break
    else:
        continue
    
n = int(input('Type the desire number: '))
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()


for i in range(n):
    n = i + 1
    for j in range(n):
       print('*', end= ' ')
    print()

for i in range(n): 
    for j in range(i, n):
       print('*', end= ' ')
    print()

for i in range(n): 
    for j in range(n - i):
       print('  ', end= '')
    for j in range(i+1):
        print('*', end= ' ')
    print()

