import os
class PolyNode:
    def __init__(self, coef, power, next=None):
        self.coef = coef
        self.power = power
        self.next = next


class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coef, power):
        curnode = self.head

        if curnode is None:
            self.head = PolyNode(coef, power)

        elif power > curnode.power:
            self.head = PolyNode(coef, power, self.head)

        elif power == curnode.power:
            curnode.coef += coef

        else:
            while curnode.next is not None:
                if power == curnode.next.power:
                    curnode.next.coef += coef
                    return
                elif power > curnode.next.power:
                    curnode.next = PolyNode(coef, power, curnode.next)
                    return
                else:
                    curnode = curnode.next
            curnode.next = PolyNode(coef, power)

    def display(self):
        curnode = self.head
        if curnode is None:
            print("\tNo Expression Found")
            return ""
        if curnode.coef==1 :
            if curnode.power ==0 : 
                print("\t1",end="")
            elif curnode.power ==1 :
                print("\tx", end='')
            else:
                print("\tx"+str(super(curnode.power)), end='')
        elif curnode.coef==-1 :
            if curnode.power ==0 : 
                print("\t-1",end="")
            elif curnode.power ==1 :
                print("\t-x", end='')
            else:
                print("\t-x"+str(super(curnode.power)), end='')
        elif curnode.coef>0 :
            if curnode.power ==0 : 
                print("\t1",end="")
            elif curnode.power ==1 :
                print("\t"+str(curnode.coef)+"x", end='')
            else:
                print("\t"+str(curnode.coef)+"x"+str(super(curnode.power)), end='')
        elif curnode.coef<0:
            if curnode.power ==0 : 
                print("\t-1",end="")
            elif curnode.power ==1 :
                print("\t"+str(curnode.coef)+"x", end='')
            else:
                print("\t"+str(curnode.coef)+"x"+str(super(curnode.power)), end='')
        curnode = curnode.next
        while curnode is not None:
            if curnode.coef==1 :
                if curnode.power ==0 : 
                    print("+1",end="")
                elif curnode.power ==1 :
                    print("+x", end='')
                else:
                    print("+x"+str(super(curnode.power)), end='')
            elif curnode.coef==-1 :
                if curnode.power ==0 : 
                    print("-1",end="")
                elif curnode.power ==1 :
                    print("-x", end='')
                else:
                    print("-x"+str(super(curnode.power)), end='')
            elif curnode.coef>0 :
                if curnode.power ==0 : 
                    print("+1",end="")
                elif curnode.power ==1 :
                    print("+"+str(curnode.coef)+"x", end='')
                else:
                    print("+"+str(curnode.coef)+"x"+str(super(curnode.power)), end='')
            elif curnode.coef<0:
                if curnode.power ==0 : 
                    print("-1",end="")
                elif curnode.power ==1 :
                    print(str(curnode.coef)+"x", end='')
                else:
                    print(str(curnode.coef)+"x"+str(super(curnode.power)), end='')
            curnode = curnode.next
        print()

def super(x):
    x = str(x)
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

def add(poly1, poly2):
    curnode1 = poly1.head
    curnode2 = poly2.head
    poly = Polynomial()
    while curnode1 is not None and curnode2 is not None:
        if curnode1.power == curnode2.power:
            poly.insert(curnode1.coef+curnode2.coef, curnode1.power)
            curnode1, curnode2 = curnode1.next, curnode2.next
        elif curnode1.power > curnode2.power:
            poly.insert(curnode1.coef, curnode1.power)
            curnode1 = curnode1.next
        else:
            poly.insert(curnode2.coef, curnode2.power)
            curnode2 = curnode2.next
    while curnode1 is not None:
        poly.insert(curnode1.coef, curnode1.power)
        curnode1 = curnode1.next
    while curnode2 is not None:
        poly.insert(curnode2.coef, curnode2.power)
        curnode2 = curnode2.next
    return poly


def multiply(poly1,poly2):
    curnode1 = poly1.head
    poly = Polynomial()
    while curnode1 is not None:
        curnode2 = poly2.head
        while curnode2 is not None:
            poly.insert(curnode1.coef*curnode2.coef,curnode1.power+curnode2.power)
            curnode2 = curnode2.next
        curnode1 = curnode1.next
    return poly
        
            
            


poly1 = Polynomial()
poly2 = Polynomial()


while True:
    os.system('cls')
    print("\n\n\t1. Add Terms to Polynomial 1 ")
    print("\t2. Add Terms to Polynomial 2 ")
    print("\t3. Display Polynomial 1 ")
    print("\t4. Display Polynomial 2 ")
    print("\t5. Add Two Polynomial ")
    print("\t6. Multiply Two Polynomial ")
    print("\t0. Exit")
    ch = int(input())
    if ch==1:
        print("\tPolynomial 1 : ",end='')
        poly1.display()
        poly1.insert(int(input("\n\tEnter Coefficient: ")),
                 int(input("\tEnter Power: ")))
        print()
        print("\tPolynomial 1 : ",end='')
        poly1.display()
    elif ch==2:
        print("\tPolynomial 2 : ",end='')
        poly2.display()
        poly2.insert(int(input("\n\tEnter Coefficient: ")),
                 int(input("\tEnter Power: ")))
        print()
        print("\tPolynomial 2 : ",end='')
        poly2.display()
    elif ch==3:
        print("\tPolynomial 1 : ",end='')
        poly1.display()
    elif ch==4:
        print("\tPolynomial 2 : ",end='')
        poly2.display()
    elif ch==5:
        poly3 = add(poly1,poly2)
        print("\n\t \t ",end='')
        poly1.display()
        print("\n\t \t+ ",end='')
        poly2.display()
        print("\n\t \t= ",end='')
        poly3.display()
    elif ch==6:
        poly3 = multiply(poly1,poly2)
        print("\n\t \t ",end='')
        poly1.display()
        print("\n\t \t* ",end='')
        poly2.display()
        print("\n\t \t= ",end='')
        poly3.display()
    elif ch==0:
        break
    input()
        