# Creating Node Class
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class Queue:
    def __init__(self):
        self.tail = None
    
    def enqueue(self,data):
        node = Node(data)
        if self.tail is None:
            node.next = node
        else:
            current_node = self.tail
            node.next = current_node.next
            current_node.next = node
        self.tail = node
        
    def dequeue(self):
        current_node = self.tail
        if current_node.next is current_node:
            data = current_node.data
            del current_node
            return data
        else:
            temp = current_node.next
            current_node.next = current_node.next.next
            data = temp.data
            del temp
            return data
        
    def isEmpty(self):
        return self.tail is None
    
    def display(self):
        if self.tail is None:
            print("Queue Underflow")
        elif self.tail.next is self.tail:
            print(self.tail.data)
        else:
            temp = self.tail.next
            node = self.tail.next
            print(node.data,end=' ')
            node = node.next
            while node is not temp:
                print(node.data,end=' ')
                node = node.next
                
            
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