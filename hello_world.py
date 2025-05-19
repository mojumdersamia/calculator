
'''a = " hello python interpreter "
print (a.title().lstrip())
nostrach_url = "https:// nostrach.com"
print(nostrach_url.removeprefix("https://"))
n = 3 + (2.00005)
print (n)

#constants are written in capital letters
PLANC_CONST = 6.626



import this

bicycle = ['trek', 'redline', 'specialized']
print(bicycle[1].title())
print(bicycle.pop())
bicycle.sort(reverse=True)
print(bicycle)

# sorted function is used to sort temporarily

magician = ['alice', 'david', 'carolina']
for magician in magician:
    print(magician)'''





i = 10
print(type(i))

stud_list= ["kyle", 100, "fahim", "alice"]
#stud_list  = str(stud_list[1])
# stud_list = list("kyle", "bob", "fahim", "alice")
print(type(stud_list[1]))

stud_list.append("amena")

stud_list.insert(1, "sakib")
print(stud_list)

stud_list.pop(1)
print(stud_list)

#print(stud_list[1:3])

for x in stud_list:
    print(x)

[print(x) for x in stud_list]

size= len(stud_list)
for i in range(size):
    if stud_list[i] == 100:
        continue
    if stud_list[i] == "fahim":
        break
    print(stud_list[i])

