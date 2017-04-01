#Start of Implementing Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

#End of Implementing Queue

#Start of Implementing Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def strnode(self):
        print(self.data)

class LinkedList:
    def __init__(self):
        self.numnodes = 0
        self.head = None

    def insertFirst(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        self.numnodes += 1

    def insertLast(self, data):
        newnode = Node(data)
        newnode.next = None
        if self.head == None:
            self.head == newnode
            return
        lnode = self.head
        while lnode.next != None:
            lnode = lnode.next
        lnode.next = newnode
        self.numnodes += 1

    def remFirst(self):
        cnode = self.head
        self.head = cnode.next
        cnode.next = None
        del cnode
        self.numnodes -= 1

    def remLast(self):
        lnode = self.head
        while lnode.next != None:
            pnode = lnode
            lnode = lnode.next
        pnode.next = None
        del lnode
        self.numnodes -= 1

    def getfirst(self):
        lnode = self.head
        return lnode.data

    def getLast(self):
        lnode = self.head

        while lnode.next != None:
            lnode = lnode.next
            return lnode.data

    def print_list(self):
        lnode = self.head
        while lnode:
            lnode.strnode()
            lnode = lnode.next

    def getSize(self):
        return self.numnodes

    def delete(self, value):
        head = self.node
        if head.getValue() == value:
            return LinkedList(head.next)
        temp = head
        while temp.next is not None:
            if temp.next.getValue() == value:
                temp = temp.next.next
                temp.next = None
                return LinkedList(head)
            temp = temp.next
        return "Sorry node is not here!"

#End of Linked list Implementation
q=Queue()
l=LinkedList()

#Discribe Car
class Car:
    def __init__(self,item):
        self.LP = item
        self.count = 0

#Define what happen when car is Arrived
def Arrive(scar):
    if q.size()<10 and l.getSize()==0:
        q.enqueue(scar)
        print("Free Room Available")
    elif q.size()<10 and l.getSize()!=0:
        q.enqueue(l.getfirst())
        l.remFirst()
        l.insertLast(scar)
        print("the Car is in the waiting List")
    else:
        l.insertLast(scar)
        print("the Car is in the waiting List")

#Define What Happen when car is Derived
def Derive(scar):
    steps = 0
    checker=0
    while steps!=q.size():
        x=q.dequeue()
        #This will run if wrong car is selected
        if x.LP!=scar.LP:
            q.enqueue(x)
            scar.count +=1
        #This will run if the Correct Car is Selected
        else:
            if l.getSize()!=0:
                y=l.getfirst()
                q.enqueue(y)
                l.remFirst()
            scar.count +=1
            checker +=1
        steps =steps + 1


#Read The Inputs in 'input.txt' and set them in a list named Data
f = open('input.txt', 'r')
line = f.readline()
while (line):
    data = line.strip('/n').split(',')
    scar = Car(data[1])
    if data[0]=='a':
        Arrive(scar)
        print("A car Arrived ",scar.LP)
    else:
        Derive(scar)
        print("The car Derived", scar.LP, "The Car has moved ",scar.count)

    line = f.readline()





