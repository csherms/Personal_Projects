# class PublicPrivateExample():
#   def __init__(self):
#     self.public = "safe"
#     self.private = "unsafe"

#   """The underscore makes it a 'private' method."""
    
#   def public_method(self):
#     """clients can use this"""
#     pass
  
#   def _unsafe_method(self):
#     """clients shouldn't use this"""
#     pass
    
    

# class Shape():
#   def __init__(self, w, l):
#     self.width = w
#     self.len = l
    
#   def print_size(self):
#     print("{} by {}".format(self.width, self.len))
    

# class Square(Shape):
#   """The 'square' class inherates the 'shape' class's attributes and methods"""
#   def area(self):
#     print("My area is: ")
#     return self.width * self.len

#   def print_size(self):
#     print("I am {} by {}".format(self.width, self.len))
    
# a_square = Square(20, 20)
# a_square.print_size()
# print(a_square.area())

# class Dog():
#   def __init__(self, name, breed, owner):
#     self.name = name
#     self.breed = breed
#     self.owner = owner
    
# class Person():
#   def __init__(self, name):
#     self.name = name
    
# # Now the stan object "Stanley" has an owner -- a Person object named "Mick Jagger"-- stored in the owner instance variable
# mick = Person("Mick Jagger")
# stan = Dog("Stanley", "Bulldog", mick)
# print(stan.owner.name)


# It appears that inheritance is passed down through multiple children -- rectange takes shape and square takes rectangle so square also gets shape.
# class Shape():
#   def what_am_i(self):
#     print("I am a shape")


# class Rectangle(Shape):
#   def __init__(self, w, l):
#     self.width = w
#     self.len = l
    
#   def perimeter(self):
#     return (self.width * 2) + (self.len * 2)


# class Square(Rectangle):
#   def change_size(self, n):
#     return self.width + n, self.len + n


# a_square = Square(10,20)
# print(a_square.perimeter())


# class Horse():
#   def __init__(self, name, rider):
#     self.name = name
#     self.rider = rider
    
# class Rider():
#   def __init__(self, name):
#     self.name = name
    
# a_rider = Rider("Jim Jones")
# a_horse = Horse("Davey", a_rider)
# print(a_horse.rider.name)
# print(a_horse.name)

# class Square():
#   """This will make the square_list variable accessable to all instances of the Square objects"""
#   square_list = []
  
#   def __init__(self, s1):
#     self.s1 = s1
#     self.square_list.append(s1 * 4)
    
#   """This will change the name of the object when printed to whatever I say"""  
#   def __repr__(self):
#       return ("{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1))
    
#   """This will check if two objects are the same and print true or false"""  
#   def check_if_same(self, o1, o2):
#     print(o1 is o2)
  
# a_square1 = Square(10)
# a_square2= Square(20)
# a_square3 = Square(30)

# print(Square.square_list)
# print(a_square3)
# a_square1.check_if_same(a_square1, a_square2)
