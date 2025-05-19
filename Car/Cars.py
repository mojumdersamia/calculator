# find the cars which have distance greater than 18

cars = [[1,4,2], [2,4,10],
[3,7,4],
[4,7,22],
[5,8,16]]

for i in cars:
    if i[2] > 18:
        print (i[0])