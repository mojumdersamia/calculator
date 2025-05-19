n = int(input("Enter your marks: "))
if n >= 80:
    print('A+')
elif n >=70 and n <=79:
    print('A')
elif n >= 60 and n <= 69:
    print('A-')
elif n >= 50 and n <= 59:
    print('B')
elif n >= 40 and n<= 49:
    print('C')
else:
    print('fail')