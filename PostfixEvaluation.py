'''
Write a python program to Evaluate a Postfix Expression (Postfix Evaluation)
'''
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
        print(self.__list)
        
def isOperator(ch):
    op = ('+','-','*','/','%')
    if ch in op:
        return True
    else:
        return False
    
def operation(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    elif op=='%':
        return a%b
    elif op=='^':
        return a^b
    
exp = input("Enter a Postfix Expression : ")
postfix = list([x if isOperator(x) else int(x) for x in exp])
s = Stack()
for ch in postfix:
    if not isOperator(ch):
        s.push(ch)
    else:
        b = s.pop()
        a = s.pop()
        c = operation(a,b,ch)
        s.push(c)

print("Answer : "+str(s.pop()))
