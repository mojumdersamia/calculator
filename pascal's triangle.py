rows = int(input('Enter the expected pascal pyramid number: '))
n = 1
for i in range(rows + 1):
    for k in range(1, rows - i + 1):
        print('', end= ' ')
    for j in range(0, i):
        if j==0 or i==1:
            n = 1
        else:
            n = n * (i - j)//j
        print(n, end = " ")
    print()