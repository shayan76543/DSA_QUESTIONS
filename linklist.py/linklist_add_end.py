class node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
class linklist:
    def __init__(self,head=None):
        self.head=head
    def insert_end(self,value):
        temp=node(value)
        if (self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next 
            t1.next=temp
        else:
            self.head=temp
    def print_linklist(self):
        t1=self.head
        while(t1!=None):
            print(t1.data)
            t1=t1.next
first=linklist()
first.insert_end(30)
first.insert_end(20)
first.print_linklist()