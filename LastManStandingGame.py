# Creating Node Class
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
# Creating Circular Linked List
class CircularLinkedList:
    # Creating head reference
    def __init__(self):
        self.head = None
        self.current_val = None
        
    def insert(self,num):
        node = Node(num)
        current_node = self.head
        if current_node is None:    # If List is Empty
            node.next = node
            self.head = node
            self.current_val = self.head
        else:
            while current_node.next is not self.head:   # Go to Last Node
                current_node = current_node.next
            current_node.next =  node   # Refer Last Node (Prev) to New Node (at end)
            node.next = self.head   # Refer New Node (at end) to 1st Node
    
    def delete(self,term):
        current_node = self.current_val
        for i in range(term-2):
            current_node = current_node.next  
        node = current_node.next
        self.current_val = node.next
        current_node.next = node.next
        if self.head is node:
            self.head = node.next
        del node
        return True

    # Function to display the linked list
    def display(self):
        current_node = self.head
        print(current_node.data,end='->')
        current_node = current_node.next
        while current_node is not self.head:
            print(current_node.data,end='->')
            current_node = current_node.next
        else:
            print("None")
        print()
        
    # Function to count the linked list
    def count(self):
        i = 0
        current_node = self.head
        if self.head is not None:
            i+=1
            current_node = current_node.next
            while current_node is not self.head:
                i+=1
                current_node = current_node.next
        return i
            
    
link = CircularLinkedList()
for i in range(1,7):
    link.insert(i)
    
link.display()

term = int(input("Enter term : "))
flag = True
while flag:
    if link.count()>1:
        link.delete(term)
        link.display()
        input()
    else:
        flag = False
        
print("Winner is ",link.head.data)