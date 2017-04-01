class Stack():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

x=input("Enter The Postfix Expression: ")
k=['1','2','3','4','5','6','7','8','9','0']
l=['+','-','*','/']
s=Stack()

for i in x:
    if i in k:
        s.push(i)
    elif i in l:
        r=int(s.pop())
        t=int(s.pop())
        print("LD ",t)
        if i=='+':
            temp=t+r
            print("AD ",r)
        elif i=='-':
            temp=t-r
            print("SB ", r)
        elif i=='*':
            temp=t*r
            print("ML ", r)
        else:
            temp=t/r
            print("DV ", r)

        s.push(temp)
    else:
        print("Your Input is not valied")


