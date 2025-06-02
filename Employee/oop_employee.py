class employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def getname(self):
        return self.name
emp1 = employee(100,"alice", 45000)
emp2 = employee(101, "rihanna", 34000)

print(emp1.salary)
print(emp1.getname())
        