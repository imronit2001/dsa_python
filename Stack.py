'''
Write a python program to implement stack using class
'''
class Stack:
    def __init__(self):
        self.__list = []
    def isEmpty(self):
        if len(self.__list)==0:
            return 1
        else:
            return 
    def push(self,n):
        self.__list.append(n)
    def pop(self):
        return self.__list.pop()
    def display(self):
#         print(self.__list)
#         i = len(self.__list)-1
        for i in range(len(self.__list)-1, -1, -1):
            print("".center(10,' '),end='')
            print("|"+str(self.__list[i]).center(8," ")+"|")
            print("".center(10,' '))
            print("".center(10,' '),end='')
            print("".center(10,"-"))
            print("".center(10,' '))

s = Stack()
n = 0
while(n!=4):
    print("\n Choose an option : ")
    n = int(input("1. Push \t 2. Pop \t 3. Display \t 4. Exit\n"))
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
    elif n != 4:
        print("Invalid Choice")
