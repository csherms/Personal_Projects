class Stack:
  def __init__(self):
    self.items = []
    
  def is_empty(self):
    return self.items == []
  
  def push(self, item):
    return self.items.append(item)
  
  def pop(self):
    return self.items.pop()
  
  def peek(self):
    last = len(self.items) - 1
    return self.items[last]
  
  def size(self):
    return len(self.items)
  
  def look(self):
    return self.items
  

# This is a common interview question using a Stack to reverse a list
stack = Stack()
for letter in "Hello":
  stack.push(letter)
  
reverse = ""

for i in range(len(stack.items)):
  reverse += stack.pop()
  
print(reverse)




class Queue:
  def __init__(self):
    self.items = []
    
  def is_empty(self):
    return self.items == []
  
  def enqueue(self, item):
    self.items.insert(0, item)
    
  def dequeue(self):
    return self.items.pop()
  
  def size(self):
    return len(self.items)
    
    
a_queue = Queue()
for i in range(5):
  a_queue.enqueue(i)   
  
print(a_queue.size())
    
print()

for i in range(5):
  print(a_queue.dequeue())
  
print()
print(a_queue.size())