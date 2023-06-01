'''
Write a program to implement Circular Queue using Array in Python
'''
import numpy as np
class Queue:
    def __init__(self):
        self.size = 10
        self.__list = np.array([0 for i in range(self.size)])
        self.front = -1
        self.rear = -1
    def isEmpty(self):
        if self.front==-1 and self.rear==-1 :
            return True
        return False
    def isFull(self):
        if (self.front==0 and self.rear==self.size-1) or (self.rear==self.front-1):
            return True
        return False
    def enqueue(self,n):
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        elif self.rear==self.size-1:
            self.rear=0
        else:
            self.rear+=1
        self.__list[self.rear] = n
    def dequeue(self):
        x = self.__list[self.front]
        if self.front==self.size-1:
            self.front=0
        elif self.front==self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front+=1
        return x
    def display(self):
        if self.front<self.rear:
            for i in range(self.front,self.rear):
                print(self.__list[i],end=' ')
        else:
            for i in range(self.front,self.size-1):
                print(self.__list[i],end=' ')
            for i in range(0,self.rear):
                print(self.__list[i],end=' ')
        
s = Queue()
n = 0
while(n!=4):
    print("\n Choose an option : ")
    n = int(input("1. Enqueue \t 2. Dequeue \t 3. Display \t 4. Exit\n"))
    if n == 1:
        if not s.isFull():
            s.enqueue(int(input("Enter the number to be enqueued : ")))
            s.display()
        else:
            print("Queue Overflow")
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