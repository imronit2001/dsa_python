'''
Implement Queue using Header Linked List
'''
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self,data):
        if self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            
    def dequeue(self):
        currrent_node = self.head
        if currrent_node.next is None:
            self.head = None
            self.tail = None
            data = currrent_node.data
            del currrent_node
            return data
        else:
            self.head = currrent_node.next
            data = currrent_node.data
            del currrent_node
            return data
        
    def isEmpty(self):
        return self.head is None
    
    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data,end='->')
            current_node = current_node.next
    
s = Queue()
n = 0
while(n!=4):
    print("\n Choose an option : ")
    n = int(input("1. Enqueue \t 2. Dequeue \t 3. Display \t 4. Exit\n"))
    if n == 1:
        s.enqueue(int(input("Enter the number to be enqueued : ")))
        s.display()
    elif n == 2:
        if(s.isEmpty()):
            print("Queue Underflow")
        else:
            print("Dequeued Element =",s.dequeue())
            s.display()
    elif n == 3:
        s.display()
    elif n != 4:
        print("Invalid Choice")