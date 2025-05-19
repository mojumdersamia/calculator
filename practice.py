#print("samia")
##print("""hello world, 
##Samia, 
##hope you are fine today""")

#new line indicator \n
##print("hello world, \n"  + "Samia,  \n" + "hope you are fine today")

##print("SAMIA \n" * 5)

#input 
##print(input("Hello, what's your name? "))

name = input("What is your name?\n")

if name == "Ben" :
    print ("Youre not welcome here.... ! Get out...!")
else: 
    menu = ("Mocha, espresso, black coffee, latte")
    print("Hello, "+name +" Here's the menu of our coffeeshop. " + menu)
    order = input("What would you like?\n")
    price = 8
    print("Each item costs 8 dollars, how many " + order + " would you want?")
    quantity = input()
    total = price* int(quantity)
    print("Your total is $" +  str(total) + ". Your " + quantity + " " +order + " would be ready just in a moment")

#number
number = 7
actual_age = 22.13
print(type(number))
print(type(name))
print(type(actual_age))
print(5*4/5+6-4)
# anything in the "" is string
math = 9**8 # exponent
print(math)


