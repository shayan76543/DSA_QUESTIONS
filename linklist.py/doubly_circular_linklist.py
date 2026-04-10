class node:
    def __init__(self,data,address=None,previous=None):
        self.data=data
        self.address=address
        self.previous=previous
class circular_linklist:
    def __init__(self,head=None):
        self.head=head
    def insert_beggining(self,value):
        new_node=node(value)
        if self.head is None:
            new_node.address=new_node
            new_node.previous=new_node
            self.head=new_node
            return 
        temp=self.head
        while temp.address!=self.head:
            temp=temp.address
        temp.address=new_node
        new_node.previous=temp
        new_node.address=self.head
        self.head.previous=new_node
        self.head=new_node
    def print(self):
        if self.head is None:
            print("linklist are not created")
            return 
        t1=self.head
        while t1.address!=self.head:
            print(t1.data,end="<-->")
            t1=t1.address
        print(t1.data)
obj1=circular_linklist()
obj1.insert_beggining(43)
obj1.insert_beggining(3)
obj1.insert_beggining(91)
obj1.insert_beggining(12)
obj1.insert_beggining(90)
obj1.insert_beggining(23)
obj1.print()