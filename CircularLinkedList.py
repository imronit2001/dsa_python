"""
Created on Tue Mar 22 11:20:00 2023
@author: RONIT SINGH
Statement: Circular Linked List
"""

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
    
    # Function to create a node at begining
    def insert_beg(self,num):
        node = Node(num,self.head)
        current_node = self.head
        if current_node is None:    # If List is Empty
            node.next = node
        else:
            while current_node.next is not self.head:    # Go to Last Node
                current_node = current_node.next
            current_node.next = node    # Refer Last Node to New Node (at beg)
            node.next = self.head   # Refer New Node to 1st Node (Prev)
        self.head = node    # Refer head to New Node (at bef)
        
    # Function to create a node at end
    def insert_end(self,num):
        node = Node(num)
        current_node = self.head
        if current_node is None:    # If List is Empty
            node.next = node
            self.head = node
        else:
            while current_node.next is not self.head:   # Go to Last Node
                current_node = current_node.next
            current_node.next =  node   # Refer Last Node (Prev) to New Node (at end)
            node.next = self.head   # Refer New Node (at end) to 1st Node
    
    # Function to create a node at nth
    def insert_nth(self,pos,num):
        node=Node(num)
        if pos==1:
            self.insert_beg(num)
        else:
            current_node = self.head
            for i in range(pos-2):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node

    # Function to display the linked list
    def display(self):
        current_node = self.head
        if self.head is not None:
            print("Head",end='->')
            print(current_node.data,end='->')
            current_node = current_node.next
            while current_node is not self.head:
                print(current_node.data,end='->')
                current_node = current_node.next
            print("Head")
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
            
    # Function to delete the node at beginning
    def delete_beg(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            current_node = self.head
            if current_node.next is self.head:  # If there is only one Node
                del current_node
                self.head = None
            else:
                temp = current_node # Storing first node in temp
                while current_node.next is not self.head:    # Go to Last Node
                    current_node = current_node.next
                current_node.next = temp.next   # Refer Last Node to 2nd Node (Prev)
                self.head = temp.next   # Refer head to 2nd Node (Prev)
                del temp # Delete 1st Node
            
    # Function to delete the node at end
    def delete_end(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            current_node = self.head
            if current_node.next is self.head:  # If there is only one Node
                del current_node
                self.head = None
            else:
                while current_node.next.next is not self.head:    # Go to Last Node
                    current_node = current_node.next
                temp = current_node.next    # Storing Last node in temp
                current_node.next = temp.next   # Refer LastNode->next to current node (2nd last node)
                del temp    # Delete Last Node
                
    # Function to delete a node from nth Position
    def delete_nth(self,pos):
        if self.head is None:
            print("Linked List is Empty")
        else:
            current_node = self.head
            if pos==1:
                if current_node.next is self.head:  # If there is only one Node
                    del current_node
                    self.head = None
                else:
                    temp = current_node # Storing first node in temp
                    while current_node.next is not self.head:    # Go to Last Node
                        current_node = current_node.next
                    current_node.next = temp.next   # Refer Last Node to 2nd Node (Prev)
                    self.head = temp.next   # Refer head to 2nd Node (Prev)
                    del temp # Delete 1st Node
            else:
                for i in range(pos-2):  # Go to pos-1 node
                    current_node = current_node.next
                temp = current_node.next    # Store pos node in temp
                current_node.next = temp.next   
                del temp
            
            
link = CircularLinkedList()
while True:
    print("1. To insert at Begining")
    print("2. To display")
    print("3. To insert at end")
    print("4. To insert at nth")
    print("5. To count the nodes")
    print("6. To delete from begining")
    print("7. To delete from end")
    print("8. To delete from nth")
    print("0. To Exit")
    ch = int(input("Enter your choice : "))
    if ch==1:
        link.insert_beg(int(input("Enter a number you want to insert: ")))
    elif ch == 2:
        link.display()
    elif ch==3:
        link.insert_end(int(input("Enter a number you want to insert: ")))
    elif ch==4:
        pos = int(input("Enter the position: "))
        if pos>0 and pos<=link.count()+1:
            link.insert_nth(pos, int(input("Enter a number you want to insert: ")))
        else:
            print("Out of bound position")
    elif ch==5:
        print("Count: ",link.count())
    elif ch==6:
        link.delete_beg()
    elif ch==7:
        link.delete_end()
    elif ch==8:
        pos = int(input("Enter the position: "))
        if pos>0 and pos<=link.count():
            link.delete_nth(pos)
        else:
            print("Out of bound position")
    elif ch == 0:
        break
        

        