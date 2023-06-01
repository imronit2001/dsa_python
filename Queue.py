class Queue:
    def __init__(self):
        self.__list = []
    def isEmpty(self):
        if len(self.__list)==0:
            return 1
        return 0
    def enqueue(self,n):
        self.__list.append(n)
    def dequeue(self):
        return self.__list.pop(0)
    def display(self):
        print(self.__list)

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