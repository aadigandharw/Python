# Area Of Circle
from abc import ABC ,abstractmethod

class Shape (ABC):
    @abstractmethod
    def area(self):
        pass

class Circle (Shape):
    def __init__(self,radius):
        self.radius = radius

    def area (self):
        return 3.14 * self.radius * self.radius
    
c = Circle(2)
print(c.area())
        