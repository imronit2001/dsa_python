import os
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
        self.show(num,"\033[0;32m")
    
    def delete(self,term):
        current_node = self.current_val
        for i in range(term-2):
            current_node = current_node.next  
        node = current_node.next
        self.show(node.data,"\033[0;31m")
        self.current_val = node.next
        current_node.next = node.next
        if self.head is node:
            self.head = node.next
        
        print("\033[0;31m\t",node.data,"\033[0;37m knocked out...")
        del node
        return True

    def show(self,n,color):
        current_node = self.current_val
        if current_node is None:
            print("\n \tNo tokens found\n")
            return
        print("\n")
        if current_node.data == n:
            print("\b\b",color,"\b\t",current_node.data,end='\033[0;37m  ')
        else:
            print("\t",current_node.data,end='  ')
        current_node = current_node.next
        while current_node is not self.current_val:
            if current_node.data == n:
                print("\b\b",color,"\b",current_node.data,end='\033[0;37m  ')
            else:
                print(current_node.data,end='  ')
            current_node = current_node.next
        print()

    # Function to display the linked list
    def display(self):
        current_node = self.current_val
        if current_node is None:
            print("\n \tNo tokens found\n")
            return
        print("\n\n\t",current_node.data,end='  ')
        current_node = current_node.next
        while current_node is not self.current_val:
            print(current_node.data,end='  ')
            current_node = current_node.next
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
flag = True
while flag:
    input()
    os.system("cls")
    print("\n\n\t\033[0;32mJosephus Problem\033[0;37m")
    print("\n\t\033[0;33m1. Insert the Token\033[0;37m")
    print("\t\033[0;33m2. Show Tokens\033[0;37m")
    print("\t\033[0;33m3. Find Result\033[0;37m")
    print("\t\033[0;33m4. Quit\033[0;37m")
    print("\t\033[0;33m5. Restart\033[0;37m")
    ch = int(input())
    if ch==1:
        link.insert(int(input("\tEnter the Token : ")))
    elif ch==2:
        link.display()
    elif ch==3:
        if link.count()==0:
            print("\n \tNo tokens found\n")
            continue
        flag = False
        term = int(input("\tEnter the passes to be removed : "))
        flag = True
        while flag:
            if link.count()>1:
                link.delete(term)
                input()
            else:
                flag = False
                
        if link.head is not None:
            print(" \t\033[0;32mWinner is ",link.head.data,"\033[0;37m")
        else:
            print(" \tNo tokens")
    elif ch==4:
        flag = False
    elif ch==5:
        link = CircularLinkedList()
