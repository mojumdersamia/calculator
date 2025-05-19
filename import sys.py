import sys
print (sys.version)

#multi var
fruit = ["apple", "banana", "cherry", "kiwi", "mango"]
juicy =  ["pineapple", "papaya"]
thetuple =("guava", "fig")


fruit[2]= "peach"
fruit.append("avocado")
# fruit.insert(2, "melon")
print(fruit)
fruit.extend(juicy)
print(fruit)
fruit.extend(thetuple)
print(fruit)
fruit.remove("fig")
print(fruit)
fruit.pop(2) #del fruit[2]
print(fruit)
fruit.clear() #del fruit
print(fruit)


if "apple" in fruit:
    print("yes, apple is in the fruit")
#x, y, z, u, v= fruit


m=n=o= "Orange"
print(m)
print(n)
print(o)


p, q, r= "Python", "is", "fun"
print(p)
print(p, q, r)
print(p+q+r)

k=20
i=60
print(k+i)

# in function
def myFunc():
    global x  # global keyword means every x is same, try removing and see the magic
    x = "fantastic"
    print("python is " + x)

myFunc()
print("python is" + x)

import random
print(random.randrange(1,10))


for x in "fantastic":
    print(x)

print (len(x))


txt = f" The best things in life are free!     "
print("lorem" in txt)
print("free" in txt)
print(txt[2:5])
print(txt[:5]) # 5 not included
print(txt[-5:-2]) #from last to front
print(txt.upper()) 
print(txt.lower())
print(txt.strip()) # removes whitespaces from begiinning to end
print(txt.replace("free", "paid")) # replaces word
print(txt.split())
print(txt.capitalize())

##age = input("age = ")
age= 34
text = f"i am {age}"
print(text)

if "free" in txt:
    print ("yes, 'free' is present")
if "lorem" not in txt:
    print("no, lorem is not present.")

t=200
s=30
print(isinstance(t, str))

if t > s:
    print("t is greater than s")
else:
    print("t is less than s")

print (bool(t)) 
print (10 > 9)  


# boolean
class myclass():
    def __len__(self):
        return 0
    
myobj  = myclass()
print (bool(myobj))

#boolean value  function
def myFunction():
    return True
print (myFunction())

if myFunction():
    print("Yes")
else:
    print("no")


thelist = ["chair", "table", "sofa", "cot", "cupboard"]
for i in range(len(thelist)):
    print(thelist[i])

i = 0
while i < len(thelist):
    print(thelist[i])
    i = i+1

[print(i) for i in thelist]

foods = ["baklava", "Juice", "burger", "masala chicken", "Falafel", "Asparagas", "almonds"]
newList = [] #foods containing a
for j in foods:
    if "a" in j:
        newList.append(j)
print(newList)

newList2 = [x for x in foods if "e" in x]
print(newList2)


newList3 = [x for x in foods if x !="burger"] # only accept items like NOT burger
print(newList3)

iterable = [x for x in range(10) if x <6]
print(iterable)

newList4 = [x if x != "burger" else "pasta" for x in foods] #exchange
print(newList4)

foods.sort()
print(foods)

foods.sort(reverse=True)
print(foods)

#sort the list based on how close the num is to 50
def myfunc(n):
    return abs(n - 50)
numlist = [100, 52, 65, 82, 23, 11, 74, 93]
numlist.sort(key = myfunc)
print(numlist)

#default sort is small letter after capital, but if you want case insenitive,
foods.sort(key= str.lower)
print(foods)

foods.reverse()
print(foods)

#copy list
mylist= thelist.copy()
print(mylist)

mylist2 = foods[:]
print(mylist2)

#join two list
#also foods.extend(thelist) and print foods
joinlist = foods + thelist
print(joinlist)

for x in foods:
    thelist.append(x)
print(thelist)

mytuple = ("psychology", "english", "biology", "chemistry", "physics")
print(len(mytuple))
print(type(mytuple))

#changing tuple values, can be done by other list adding method
y = list(mytuple)
y[1] = "philosophy"
mytuple = tuple(y)
print(mytuple)

# or make another tuple and add
Y = ("bangla",) # of course the comma is important
mytuple += Y
print(mytuple)
 ## removing items are easy by making it a list

#indexing
for i in range (len(mytuple)):
    print(mytuple[i])

i=0
while i < len(thetuple):
    print(thetuple[i])
    i = i+1

othertuple = mytuple * 3
print(othertuple)

a_set = {True, 1}
print(a_set)
b_set= set((34, 1, 2, 3, 5, 54, 4))
c_set = {7, 8, 9,3,4, 10}
print(b_set)

for x in b_set:
    print(x)

print("5" in b_set)
b_set.add(5)
print(b_set)

b_set.update(c_set)
print(b_set)
b_set.pop()
print(b_set)

set1 = b_set.union(c_set, a_set) #or
set_1 = b_set | c_set
print(set1)
print(set_1)
# intersection () can be &

car = {
    "brand" : "ford",
    "year" : 1964,
    "model" : "mustang",
    "electric" : False,
    "colors" : ["red", "white", "blue"]
}
print(car)
print(len(car))

p = car.get("model")
p1 = car.keys()
print(p)
print(p1)
car["color"] = "maroon"
print(p1)
p1 = car.values()
print(p1)
p1 = car.items()
print(p1)
if "model" in car:
    print("yay. it's in the dictionary")

#loop in dictionary
for x in car:
    print(x)

#printing all values
for x in car:
    print(car[x])
for x in car.values():
    print(x)
# for keys only type keys

#for both keys and values
for x, y in car.items():
    print(x, y)

#copying dictionary
newdict = car.copy()  # or newdict = dict(car)
print(newdict)

child1 = {
    "name": "ben",
    "age" : 45
}
child2 = {
    "name":"ross",
    "age": 30
}
child3 = {
    "name": "rachel",
    "age": 31
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)
print(myfamily["child1"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
a= 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

x = 43
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a = 33
b = 200

if b > a:
  pass  #when nothing to return

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

y= 45
if y > 10:
   print("Above ten, ")
   if y> 20:
     print("and also above twenty, ")
   else:
     print("but not above 20.") 