A = int(input("Put the first number: "))
B = int(input("Put the second number: "))
C = int(input("Put the third number: "))

if A > B and A> C:
    largest = A
    if B >= C:
      second_largest = B
      smallest = C
    else:
      second_largest = C
      smallest = B
elif B >= A and B >= C:
    largest = B
    if A >= C:
      second_largest = A
      smallest = C
    else:
      second_largest = C
      smallest = A
else:  
    largest = C
    if A >= B:
      second_largest =A
      smallest = B
    else:
      second_largest = B
      smallest =A

print(f"\nThe largest number is {largest}")
print(f"The second largest number is {second_largest}")
print(f"The smallest number is {smallest}")