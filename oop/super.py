# super() - Function used to give access to the methods of a parent class

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    
    def __init__(self, width, height):
       super().__init__(height, width)

    def area(self):
        return self.height * self.width

class Cube(Rectangle):
    
    def __init__(self, width, height, length):
        super().__init__(height, width)
        self.length = length
    
    def volume(self):
        return self.height * self.width *self.length


square = Square(3,3)
cube = Cube(3,3,3)

print(cube.volume())
print(square.area())
