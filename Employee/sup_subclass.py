class shape:
    def __init__(self, color):
        self.color= color
    
    def area(self):
        raise NotImplementedError('subcls must implement this')

class circle(shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return 3.1416* self.radius**2
        
    

s = shape("red")
c = circle('blue', 4)
print(s.color)
print(c.area())
print(c.radius)