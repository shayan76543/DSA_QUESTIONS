class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class singly_linklist:
    def __init__(self,head=None):
        self.head=head
    def insert_at_beginning(self,value):
        new_node=node(value)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def insert_at_mid(self,value,x):
        new_node=node(value)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while  temp is not None:
            if temp.data==x:
                new_node.next=temp.next
                temp.next=new_node
                return 
            temp=temp.next
    def insert_at_end(self,value):
        new_node=node(value)
        if self.head==None:
            self.head=new_node
            return 
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        return 
    def linklist_display(self):
        temp=self.head
        if temp==None:
            return "your linklist is empty"
        while temp!=None:
            print(temp.data,end=" -- ")
            temp=temp.next
obj1=singly_linklist()
obj1.insert_at_beginning(31)
obj1.insert_at_beginning(36)
obj1.insert_at_beginning(64)
obj1.insert_at_beginning(54)
obj1.insert_at_end(12)
obj1.insert_at_mid(4,64)
obj1.linklist_display()

