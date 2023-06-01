'''
Write a python program to check parenthesis properly placed or not in an expression
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
        return self.__list[len(self.__list)-1]
    def display(self):
        for i in range(len(self.__list)-1, -1, -1):
            print("".center(10,' '),end='')
            print("|"+str(self.__list[i]).center(8," ")+"|")
            print("".center(10,' '))
            print("".center(10,' '),end='')
            print("".center(10,"-"))
            print("".center(10,' '))                
                
def getOpenParenthesis(ch):
    if ch == ']':
        return '['
    if ch == '}':
        return '{'
    if ch == ')':
        return '('
    return False

def openParenthesis(ch):
    if ch=='[' or ch=='{' or ch=='(':
        return True
    return False
    
def closeParenthesis(ch):
    if ch==']' or ch=='}' or ch==')':
        return True
    return False    
    
s = Stack()  
# exp = input("Enter an arithmetic expression : ")
# print("Expression : "+exp)
exp = '[a+b*{c-(d*e)}]'
# exp = '5{3 − 2[1 − (−4)}]'
print(exp)
flag = True

for ch in exp:
    if openParenthesis(ch):
        s.push(ch)
        print("Pushed : "+ch)
    if closeParenthesis(ch):
        print("Close Para : "+ch)
        peekStack = s.peek()
        print("Stack Peek : "+peekStack)
        if peekStack == getOpenParenthesis(ch):
            s.pop()
        else:
            flag = False
            break

if flag:
    print("Parenthesis are properly closed")
else:
    print("Parenthesis are not properly closed")

