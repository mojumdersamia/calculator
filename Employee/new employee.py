f = open("d:\VScode\Employee\Employee.txt", "r")


f.readline()
lines = f.readlines()
#print(lines)


for i in lines:
    salary = i.split(',')
    #print(salary)
    if int(salary[1]) >25000 and salary[2] == " 'CTG'\n":
        print (salary[0])



