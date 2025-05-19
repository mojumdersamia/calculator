age = int(input("enter your age: "))
if age >= 11:
    print("You're eligible to see the football match")
    if age <= 12 or age >= 60:
        print("Ticket price is $12. ")
    else:
        print("Ticket price is $20. ")
else:
    print("You're not eligible to buy a ticket.")