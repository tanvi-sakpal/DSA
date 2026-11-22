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
        self.Rear.next = self.Front # Added line for circular queue/ Create a linl b/w a front and last node
    def dequeue(self):
        if self.Front:
            temp = self.Front
            self.Front = self.Front.next
            if self.Front == self.Rear: # This is updated for circular queue
                self.Front = self.Rear = None
                print("NOW QUEUE IS EMPTY")
            else:
                self.Frot = self.Front.next
                self.Rear.next = self.Front
            temp = None
        else:
            print("QUEUE IS EMPTY")

    def print(self):
        temp = self.Front
        while True:
            print(temp.data, end="")
            temp = temp.next
            if temp == self.Front:
                break
        print()

Q1 = queue()
Q1.enqueue( Node(10))
Q1.enqueue(Node(30))
Q1.enqueue(Node(40))
Q1.print()
Q1.dequeue()
Q1.print()

