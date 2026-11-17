
# Node class
class Node:
    def __init__(self, data):
        self.data = data       # Store data
        self.next = None       # Reference to next node


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None       # Initially empty list

    # Insert at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:  # If list is empty
            self.head = new_node
            return

        last = self.head

        while last.next:       # Traverse to the end
            last = last.next

        last.next = new_node

    # Print the list
    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")
    # insert node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Insert a node after a given position
def insert_after(self, prev_data, new_data):
    temp = self.head

    while temp:
        if temp.data == prev_data:
            break
        temp = temp.next

    if temp is None:
        print(f"Node with data {prev_data} not found.")
        return

    new_node = Node(new_data)
    new_node.next = temp.next
    temp.next = new_node

# Delete a node by key
def delete_node(self, key):
    temp = self.head

    # Case 1: Head node itself is to be deleted
    if temp and temp.data == key:
        self.head = temp.next
        temp = None
        return

    # Case 2: Search for the key
    prev = None

    while temp and temp.data != key:
        prev = temp
        temp = temp.next

    # If key not found
    if temp is None:
        return

    # Unlink the node
    prev.next = temp.next
    temp = None



# Usage
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

ll.print_list()
ll = LinkedList()
ll.prepend(100)

ll.append(10)
ll.append(20)
ll.append(30)

ll.insert_after(20, 25)

ll.print_list()
ll = LinkedList()
ll.delete_node(20) # Delete node with value 20
print("After deletion:")
ll.print_list()