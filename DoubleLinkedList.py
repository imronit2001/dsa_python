import os
class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_beg(self,num):
        node = Node(num)
        if self.head is not None:
            self.head.prev = node
        node.next = self.head
        self.head = node
        
    def insert_end(self,num):
        node = Node(num)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            node.prev = current_node
            current_node.next = node
            
    def insert_nth(self,pos,num):
        node = Node(num)
        if pos==1:
            self.insert_beg(num)
        else:
            current_node = self.head
            for i in range(pos-2):
                current_node = current_node.next
            node.next = current_node.next
            node.prev = current_node
            if current_node.next is not None:
                current_node.next.prev = node
            current_node.next = node
            
    def display(self):
        node = self.head
        print("\n\n")
        while node is not None:
            print(node.data,end='->')
            node = node.next
        print(None,"\n\n")
            
    def count(self):
        i = 0
        node = self.head
        while node is not None:
            i+=1
            node = node.next
        return i
        
    def delete_beg(self):
        if self.head is None:
            print("Empty List")
            return
        
        current_node = self.head
        node = current_node
        if current_node.next is not None:
            current_node.next.prev = None
        self.head = current_node.next
        del node
        
    def delete_end(self):
        if self.head is None:
            print("Empty List")
            return
        
        current_node = self.head
        if current_node.next is None:
            self.head = None
            del current_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            node = current_node
            current_node.prev.next = None
            del node
            
    def delete_nth(self,pos):
        if self.head is None:
            print("Empty List")
            return
        
        current_node = self.head
        if pos == 1:
            self.delete_beg()
        else:
            for i in range(pos-2):
                current_node = current_node.next
            node = current_node.next
            current_node.next = node.next
            node.next.prev = current_node
            del node
            
            
           
link = DoubleLinkedList()
while True:
    os.system('cls')
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
        link.display()
    elif ch == 2:
        link.display()
    elif ch==3:
        link.insert_end(int(input("Enter a number you want to insert: ")))
        link.display()
    elif ch==4:
        pos = int(input("Enter the position: "))
        if pos>0 and pos<=link.count()+1:
            link.insert_nth(pos, int(input("Enter a number you want to insert: ")))
            link.display()
        else:
            print("Out of bound position")
            link.display()
    elif ch==5:
        print("Count: ",link.count())
    elif ch==6:
        link.delete_beg()
        link.display()
    elif ch==7:
        link.delete_end()
        link.display()
    elif ch==8:
        pos = int(input("Enter the position: "))
        if pos>0 and pos<=link.count():
            link.delete_nth(pos)
            link.display()
        else:
            print("Out of bound position")
            link.display()
    elif ch == 0:
        break
    input()    

        