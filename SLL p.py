#Singly linked list
#p.py

#Singly linked list

class Node:
    """docstring for Node"""
    def __init__(self, arg):
        self.data=arg
        self.next=None

class SLL:
    """docstring for SLL"""
    def __init__(self, arg):
        self.head=Node(arg)
        self.tail=self.head

    def listprint(self):
        printval=self.head
        while printval is not None:
            print(printval.data)
            printval=printval.next

    def AtBegining(self,arg):
        newNode=Node(arg)
        newNode.next=self.head
        self.head=newNode

    def Atlast(self,arg):
        newNode=Node(arg)
        self.tail.next=newNode
        self.tail=newNode

    def Inbetween(self,pos,val):
        newNode=Node(val)
        current=self.head
        p=pos
        if p>1:
            for x in range(1,p):
                if p-x==1:
                    newNode.next=current.next
                    current.next=newNode
                else:
                    current=current.next
        else:
            newNode.next=self.head
            self.head=newNode

    def delete(self,pos):
        temp=self.head
        if pos==0:
            self.head=temp.next
            temp=None
        else:
            for x in range(pos-1):
                temp=temp.next
            if temp.next.next==None:
                temp.next=None
            else:
                temp.next=temp.next.next
    def delete_duplicates(self):
        temp=self.head
        de=self.head
        a=[]
        p=0
        while temp!=None:
            if temp.data in a:
                temp=temp.next
                for x in range(p-1):
                    de=de.next
                de.next=de.next.next
                p=0

            else:
                a.append(temp.data)
                p+=1
                print(a,p)
                temp=temp.next

    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            n=current.next
            current.next=prev
            prev=current
            current=n
        self.head=prev
    
    def kthtolast(self,n):
        current=self.head
        for x in range(1,n):
            current=current.next
        self.head=current

    def printrecurssivereverse(self,n):
        current=n
        if current!=None:
            self.printrecurssivereverse(current.next)
            print(current.data)

    def recurssivereverse(self,prev,curr):
        if curr!=None:
            self.recurssivereverse(curr,curr.next)
            curr.next=prev
        else:
            self.head=prev


s=SLL("2")

s.AtBegining('6')
s.AtBegining('5')
s.AtBegining('4')
s.AtBegining('3')
s.AtBegining('2')
s.AtBegining('1')
s.Atlast('3')
s.Inbetween(1,"3")
s.AtBegining('1')
print('SLL')
s.listprint()

s.delete(3)
print("After Delete")
s.listprint()

s.delete_duplicates()
print("After delete_duplicates")
s.listprint()

s.reverse()
print('reverse')
s.listprint()

s.kthtolast(3)
print('kthtolast')
s.listprint()

print('printrecurssivereverse')
s.printrecurssivereverse(s.head)

print("recurssivereverse")
s.recurssivereverse(None,s.head)
s.listprint()
