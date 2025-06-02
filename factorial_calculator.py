def factcal(n):
    fact = 1
    while n > 0:
        fact *= n
        n = n-1
        if (n <= 1):
            break
    else: # in n is not positive integer
        print('Input a correct number....')
        return
    return fact

print(factcal(6))
print(factcal(-6))