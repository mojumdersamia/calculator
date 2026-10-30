# calculator

a= int(input("Enter first number: "))
b= int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = a + b
    print("Result: ", result)
elif operation == "-":
    result = a - b
    print("Result: ", result)
elif operation == "*":
    result = a * b
    print("Result: ", result)
elif operation == "/":
    result = a / b
    print("Result: ", result)