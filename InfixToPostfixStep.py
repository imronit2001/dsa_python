'''
Write a program to convert an Infix Expression into Postfix Expression (Show intermediate Step)
'''
from colorama import Fore,Back,Style

class Stack:
    def __init__(self):
        self.__list = []
    def isEmpty(self):
        if len(self.__list)==0:
            return 1
        else:
            return 
    def size(self):
        return len(self.__list)
    def push(self,n):
        self.__list.append(n)
    def pop(self):
        return self.__list.pop()
    def peek(self):
        return self.__list[-1]
    def display(self):
#         print(self.__list)
        for i in range(len(self.__list)-1, -1, -1):
            print("".center(10,' '),end='')
            print("|"+str(self.__list[i]).center(8," ")+"|")
            print("".center(10,' '))
            print("".center(10,' '),end='')
            print("".center(10,"-"))
            print("".center(10,' '))
        

def isOperand(ch):
    if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
        return True
    else:
        return False
def isOperator(ch):
    op = ('+','-','*','/','%','^')
    if ch in op:
        return True
    else:
        return False
def priority(ch):
    op = {'+':1,'-':1,'*':2,'/':2,'%':2,'^':3}
    if ch in op:
        return op[ch]
    else:
        return 0


s = Stack()
exp = input("Enter an infix expression : ")
# exp = "a+b*(c-d)-e"
infix = [x for x in exp]
postfix = []


print("\n"+"Scan Char".center(10,' ')+"Stack".center(15,' ')+"Target Str".center(10,' '))
for ch in infix:
    print("".center(10,'-')+"".center(20,'-')+"".center(10,'-'))
    print(ch.center(10,' '))
    if ch == '(':
        s.push(ch)
        s.display()
        print("".center(10,' ')+"".center(20,' ')+"".join(postfix).center(10,' '))
        
    elif ch == ')':
        while s.peek() != '(':
            postfix.append(s.pop())
            s.display()
            print("".center(10,' ')+"".center(20,' ')+"".join(postfix).center(10,' '))
            print("".center(10,'-')+"".center(20,'-')+"".center(10,'-'))
        s.pop()
        s.display()
        print("".center(10,' ')+"".center(20,' ')+"".join(postfix).center(10,' '))
    elif isOperand(ch):
        postfix.append(ch)
        s.display()
        print("".center(10,' ')+"".center(20,' ')+"".join(postfix).center(10,' '))
    elif isOperator(ch):
        while ((not s.isEmpty()) and (priority(s.peek())>=priority(ch)) and (not s.peek()=='(')):
            postfix.append(s.pop())
            s.display()
            print("".center(10,' ')+"".center(20,' ')+"".join(postfix).center(10,' '))
            print("".center(10,'-')+"".center(20,'-')+"".center(10,'-'))
        s.push(ch)
        s.display()
        print("".center(10,' ')+"".center(20,' ')+"".join(postfix).center(10,' '))
while not s.isEmpty():
    postfix.append(s.pop())
    s.display()
    print("".center(10,' ')+"".center(20,' ')+"".join(postfix).center(10,' '))
    print("".center(10,'-')+"".center(20,'-')+"".center(10,'-'))

print("Infix Expression : "+''.join(infix))
print("Postfix Expression : "+''.join(postfix))

        
    