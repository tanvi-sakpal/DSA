# 1. Define the Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to nothing initially

# 2. Define the Linked List manager
class LinkedList:
    def __init__(self):
        self.head = None  # List is empty at the start

    # Method to add a node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Method to display the full list+
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# --- How to Create and Use It ---
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

my_list.print_list()  # Output: 10 -> 20 -> 30 -> None


