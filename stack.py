class Node:
    def __init__(self,data):
      self.data = data
      self.next = next
class Stack:    
 def __init__(self,value):
    self.data = value
    self.next = None
class Stack:
  def __init__(self):
    self.top = None
  def isempty(self):
    return self.top is None
  def push(self, new_node):
    new_node.next = self.top
    self.top = new_node
  def pop(self):
    if self.isempty():
      print("STack is empty")
    else:
      temp = self.top
      print("Popped element:", temp.data)
      self.top = self.top.next
      temp = None
  def reverse(self):
        temp = self.top
        while temp:
          st1.push(Node(temp.data))
          temp = temp.next
  def print(self):
    temp = self.top
    print("Stack elements")
    while temp:
      print(temp.data)
      temp = temp.next 

 

st = Stack()
st1 = Stack()
st.push(Node(10))
st.push(Node(45))
st.push(Node(23))
st.push(Node(36))
st.push(Node(20))
st.push(Node(21))
st.print()
st.pop()
st.print()
st1.print()
st1.reverse()
st1.print()