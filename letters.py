n = 7
ascii_value = 65
for i in range(1, n):
    for j in range(ascii_value, ascii_value+i):
        a = chr(j)
        print(a, end=' ')
    print()