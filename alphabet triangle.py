n = 5


ascii_value = 65
for i in range(n):
    alphabet = chr(ascii_value)
    #ascii_value += 1  
    for j in range(i+1):
        print(alphabet, end=' ')
    ascii_value += 1 
    print()

for i in range(1, n):
    for j in range(ascii_value, ascii_value+i):
        a = chr(j)
        print(a, end=' ')
    print()
