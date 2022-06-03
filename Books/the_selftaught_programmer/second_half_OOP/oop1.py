# class Orange:
#   def __init__(self, w, c):
#     """weights are in oz"""
#     self.weight = w
#     self.color = c
#     self.mold = 0
#     print("Created!")
    
#   def rot(self, days, temp):
#     self.mold = days * temp


# orange = Orange(6,"orange")
# print(orange.mold)
# orange.rot(10, 98)
# print(orange.mold)


# class Rectangle():
#   def __init__(self, w, l):
#     self.width = w
#     self.length = l
    
#   def area(self):
#     return self.width * self.length
  
#   def change_size(self, w, l):
#     self.width = w
#     self.length = l
    
# rectangle = Rectangle(10,20)
# print(rectangle.area())
# rectangle.change_size(20,40)
# print(rectangle.area())

# class Circle:
#   def __init__(self, r):
#     """The radius is in cm"""
#     self.radius = r
    
#   def area(self):
#     return 3.14 * (self.radius ** 2)
  
  
# circle = Circle(6)
# print(circle.area())

# class Triangle:
#   def __init__(self, b, h):
#     self.base = b
#     self.height = h
    
#   def area(self):
#     return (self.base * self.height) * 0.5
  
# triangle = Triangle(5,3)
# print(triangle.area())

# class Hexagon:
#   def __init__(self, s1,s2,s3,s4,s5,s6):
# """This one works if the sides are all different lengths"""
#     self.s1 = s1
#     self.s2 = s2
#     self.s3 = s3
#     self.s4 = s4
#     self.s5 = s5
#     self.s6 = s6
    
  
#   def calc_perimeter(self):
#     return self.s1 + self.s2 + self.s2 + self.s4 + self.s5 + self.s6
  
# hexagon = Hexagon(1,2,3,4,5,6)
# print(hexagon.calc_perimeter())

# class Hex2:
#   def __init__(self, ls):
#     """This one works if the side lengths are all the same"""
#     self.length_sides = ls
    
#   def calc_perimeter(self):
#     return 6 * self.length_sides
  
# hex2 = Hex2(12)
# print(hex2.calc_perimeter())


