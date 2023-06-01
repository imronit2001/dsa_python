import os
class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
        
class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_beg(self,num):
        node = Node(num)
        if self.head is None:
            node.prev,node.next = node,node
        else:
            current_node = self.head
            current_node.prev.next = node
            node.prev = current_node.prev
            current_node.prev = node
            node.next = current_node
        self.head = node
        
    def insert_end(self,num):
        node = Node(num)
        if self.head is None:
            node.prev,node.next = node,node
            self.head = node
        else:
            current_node = self.head
            current_node.prev.next = node
            node.prev = current_node.prev
            node.next = current_node
            current_node.prev = node
            
    def insert_nth(self,pos,num):
        node = Node(num)
        if pos==1:
            self.insert_beg(num)
        else:
            current_node = self.head
            for i in range(pos-2):
                current_node = current_node.next
            node.prev = current_node
            current_node.next.prev = node
            node.next = current_node.next
            current_node.next = node
            
    def display(self):
        node = self.head
        print("\n\n")
        i=1
        if node is not None:
            # print(node.data,end='->')
            # print(node.prev.data,"<--",node.data,"-->",node.next.data)
            print("\t Node : ",i,"\t[{",id(node.prev),"}<--{(",node.data,"),(",id(node),")}-->","{",id(node.next),"}]")
            i+=1
            node = node.next
        while node is not self.head:
            # print(node.data,end='->')
            # print(node.prev.data,"<--",node.data,"-->",node.next.data)
            print("\t Node : ",i,"\t[{",id(node.prev),"}<--{(",node.data,"),(",id(node),")}-->","{",id(node.next),"}]")
            i+=1
            node = node.next
        if i==1:
            print(None,"\n\n")
            
    def count(self):
        i = 0
        node = self.head
        if node is not None:
            i+=1
            node = node.next
        while node is not self.head:
            i+=1
            node = node.next
        return i
        
    def delete_beg(self):
        if self.head is None:
            print("Empty List")
            return
        
        current_node = self.head
        if current_node.next is current_node:
            del current_node
            self.head = None
        else:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self.head = current_node.next
            del current_node
            
            
        
    def delete_end(self):
        if self.head is None:
            print("Empty List")
            return
        
        current_node = self.head
        if current_node.next is current_node:
            del current_node
            self.head = None
        else:
            node = current_node.prev
            current_node.prev.prev.next = current_node
            current_node.prev = current_node.prev.prev
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
            current_node.next = current_node.next.next
            current_node.next.prev = current_node
            del node
            
            
           
link = CircularDoubleLinkedList()
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

        