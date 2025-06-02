''' function is something which must return a value, even if it doesnt have any it will return 
none. in python, procedure and function are the same. Max, read, write, etc. are building function. 
they are already built. now we are going to define a user function'''

def average (x, y):
    print('the average is', (x+y)/2)

average(23, 25)

def fileread (path):
    x = open(path, "r")
    lines = x.readlines()
    for line in lines:
        print(line)

fileread("d:\VScode\Employee\Employee.txt")




#  return the sum of squares
def nsquare(x,y):
    return(x*x + 2*x*y + y*y)
print("the sum of square  of 7 and 8 is:", nsquare(7,8))

# keyword 
def marks ( english, math = 85, science = 80):
    print('marks in: enlish is ', english, 'math is ', math, 'science is ', science)
marks(71, 77)
marks (65, science= 74)
marks(math= 90, science= 70, english= 75)

#arbitraty
def sum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(sum(1,2,3,4,5))

# anonymous function = lambda
add = lambda x, y: x+y
print(add(5,3))

numbers = [1,2,3,4,5,6]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)