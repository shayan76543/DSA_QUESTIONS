class node:
    def __init__(self,data,address=None):
        self.data=data
        self.address=address
        
class circular_linklist:
    def __init__(self,head=None):
        self.head=head
    def insert_at_beggining(self,value):
        new_node=node(value)
        if self.head is None:
            new_node.address=new_node
            self.head=new_node
            return 
        temp=self.head
        while temp.address!=self.head:
            temp=temp.address
        new_node.address=self.head
        temp.address=new_node
        new_node=self.head
    def print(self):
        temp=self.head
        while temp.address!=self.head:
            print(temp.data,end="-->")
            temp=temp.address
        print(temp.data)
        print("reach at the end this is circular linklist")
obj1=circular_linklist()
obj1.insert_at_beggining(32)
obj1.insert_at_beggining(56)
obj1.insert_at_beggining(86)
obj1.insert_at_beggining(26)
obj1.insert_at_beggining(46)
obj1.print()