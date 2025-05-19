
# find the cars which have distance greater than 18 using file reading

#import os

f = open("d:\VScode\Car\Car details.txt", "r") # r for read mode

#file = f.read()
#print(type(file))
f.readline()
lines = f.readlines()

for i in lines:
    distance = i.split(',')
    if int(distance[2]) > 18:
        print (distance[0])