class Stack():
  def __init__(self):
    self.stack = list()

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    self.stack.pop()

  def pop(self,size):
    for i in range(0,size):
      self.stack.pop()

  def get(self):
    return self.stack
  def top(self):
    return self.stack[-1]