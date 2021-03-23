class Rectangle:
    def __init__(self, length,breadth):
        self.length = length
        self.breadth= breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return (2 * (self.length + self.breadth))
R1 = Rectangle(2,4)
R2 = Rectangle(3,5)
print("area of rectangle 1:", R1.area())
print("perimeter of rectangle 1:", R1.perimeter())
print("area of rectangle 2:", R2.area())
print("perimeter of rectangle 2:", R2.perimeter())
if (R1.area() > R2.area()):
    print("Area of rectangle 1 is greater than area of rectangle 2")
else:
    print("Area of rectangle 2 is greater than area of rectangle 1")
