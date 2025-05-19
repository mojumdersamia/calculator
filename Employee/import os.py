import os

f = open("d:\\VS code\\Employee\\Employee.txt", "r")
f.readline()
lines = f.readlines()

for i in lines:
    salary = i.split(',')
    if int(salary[1]) >25800 and salary[2] == "DHK":
        print (salary[0])