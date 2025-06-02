sentence = 'this is a python file'
print(type(sentence))
upper = sentence.upper()
print(upper)



#anything that has a physical existence is called object, includes feature and function
#class doesnt have any physical existence, its a virtual thing or framework
class dog:
    color = "black"
    name = 'cal'
dog1 = dog()#constructor
dog1.color = 'white'
dog1.name = 'tommy'
print(dog1.color)


class Dog:
    def __init__(self,name,age):
        self.name = name  #instance var
        self.age = age
    def bark(self):
        print(f'{self.name} is barking!')
    def __str__(self):
        return f'{self.name} is { self.age} years old'

dog2 = Dog('Buddy', 4)
dog2.bark()
print(dog2.age)
print(dog2)