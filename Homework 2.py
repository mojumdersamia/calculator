n = int(input('Type the desire number: '))

# to make a square
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()

#left triangle
for i in range(n):
    n = i + 1
    for j in range(n):
       print('*', end= ' ')
    print()


print('    ')
#upside down left triangle
for i in range(n): 
    for j in range(i, n):
       print('*', end= ' ')
    print()


print('    ')
# right triangle
for i in range(n): 
    for j in range(n - i):
       print('  ', end= '')
    for j in range(i+1):
        print('*', end= ' ')
    print()


print('    ')
#upside down right triangle
for i in range(n): 
    for j in range(i + 1):
       print('  ', end= '')
    for j in range(n - i):
        print('*', end= ' ')
    print()


print('    ')
# hill
for i in range(n): 
    for j in range(i, n):
       print('  ', end= '')
    for j in range(i):
        print('*', end= ' ')
    for j in range(i + 1):
        print('*', end= ' ')
    print()

# reverse hill
for i in range(n): 
    for j in range(i + 1):
       print('  ', end= '')
    for j in range(i, n-1):
        print('*', end= ' ')
    for j in range(i, n):
        print('*', end= ' ')
    print()