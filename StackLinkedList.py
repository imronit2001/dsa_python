class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    def push(self,num):
        self.head = Node(num,self.head)

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        
    def pop(self):
        current_node = self.head
        self.head = current_node.next
        data = current_node.data
        del current_node
        return data
    
    def isEmpty(self):
        return self.head is None
    
    def peek(self):
        return self.head.data
            
   
s = Stack()
n = 1
while(n!=0):
    print("\n Choose an option : ")
    n = int(input("1. Push \t 2. Pop \t 3. Display \t 4. Peek \t 0. Exit\n"))
    if n == 1:
        s.push(int(input("Enter the number to be pushed : ")))
        s.display()
    elif n == 2:
        if(s.isEmpty()):
            print("Stack Underflow")
        else:
            print("Popped Element =",s.pop())
            s.display()
    elif n == 3:
        s.display()
    elif n==4:
        if(s.isEmpty()):
            print("Stack Underflow")
        else:
            print("Peek Element",s.peek())
    elif n != 4:
        print("Invalid Choice")