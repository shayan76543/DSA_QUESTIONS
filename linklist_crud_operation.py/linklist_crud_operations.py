class node:
    def __init__(self,data,address=None):
        self.data=data
        self.address=address
class linklist:
    def __init__(self,head=None):
        self.head=head
    def insert_beggining(self,value):
        temp=node(value)
        temp.address=self.head
        self.head=temp
    def insert_mid(self,value,x):
        temp=node(value)
        t1=self.head
        while (t1!=None):
            if (t1.data==x):
                temp.address=t1.address
                t1.address=temp
            t1=t1.address
    def insert_end(self,value):
        temp=node(value)
        if self.head!=None:
            t1=self.head
            while (t1.address!=None):
                t1=t1.address
            t1.address=temp
        else:
            self.head=temp
    def delete_ll(self,value):
        t1=self.head
        previous=t1
        if (t1.data==value): # this condition for delete first element from linklist 
            self.head=t1.address
            return 
        while (t1.address!=None):
            if (t1.data==value):
                previous.address=t1.address
                break
            else:
                previous=t1
                t1=t1.address
        if (t1.data==value):
            previous.address=None
    def print(self):
        t1=self.head
        while t1!=None: # here we used this to check wether our node is exit or not 
            print(t1.data,end="-->")
            t1=t1.address
    def lenght_counting(self): # for length counting of linklist
        t1=self.head
        length=0
        while t1 is not None:
            length+=1
            t1=t1.address
        return length

first_list=linklist()
first_list.insert_end(1)
first_list.insert_end(2)
first_list.insert_end(3)
first_list.insert_end(11)
first_list.insert_end(5)
first_list.insert_end(6)
first_list.insert_end(7)
first_list.insert_beggining(0)
first_list.insert_mid(4,3)
first_list.insert_mid(50,0)
first_list.delete_ll(7)
first_list.print()
print(first_list.lenght_counting())



    