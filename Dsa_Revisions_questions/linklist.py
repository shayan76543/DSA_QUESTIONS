class node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class linklist:
    def __init__(self,head=None):
        self.head=head
    def insert_at_beggining(self,value):
        temp=node(value)
        if self.head is None:
            self.head=temp
        else:
            temp.next=self.head
            self.head.previous=temp
            self.head=temp
    def after_value(self,value,x):
        temp=node(value)
        if self.head is None:
            self.head=temp
            return
        else:
            mover=self.head
            while mover is not None:
                if mover.data == x:
                    temp.next=mover.next
                    if mover.next is not None:
                        mover.next.previous=temp       
                    temp.previous=mover
                    mover.next=temp
                    return 
                mover=mover.next
            return False


            
    
            
            
