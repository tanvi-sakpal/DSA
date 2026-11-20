class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class queue:
    def __init__(self):
        self.Front = self.Rear = None
    def enqueue(self,new_node):
        if self.Rear:
            self.Rear.next = new_node
            self.Rear = new_node
        else:
            self.Front = self.Rear = new_node
    def dequeue(self):
        if self.Front:
            temp = self.Front
            self.Front = self.Front.next
            if self.Front == None:
                self.Rear = None
            
            temp = None
        else:
            print("QUEUE IS EMPTY")
    def print(self):
        temp = self.Front
        while temp:
            print(temp.data, "->")
            temp = temp.next

Q1 = queue()
Q1.enqueue( Node(10))
Q1.enqueue(Node(30))
Q1.enqueue(Node(40))
Q1.print()

Q1.dequeue()
print("DEQUEUE")
Q1.print()

Q1.enqueue(Node(56))
Q1.enqueue(Node(60))
print("ENQUEUE")
Q1.print()



