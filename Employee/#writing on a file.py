#writing on a file
f = open("d:\VScode\Employee\Employee.txt", "r")

f1 = open("d:\VScode\Employee\ctg_employees.txt", "w")
firstline = f.readline()
#print(firstline)
f1.write(firstline)
lines = f.readlines()


for i in lines:
    salary = i.split(',')
    
    if salary[2] == " 'CTG'\n":
        f1.write(i)

f.close()
f1.close()