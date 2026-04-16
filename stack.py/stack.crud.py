class stack:
    def __init__(self):
        self.list1=[]
    def lenght(self):
        return len(self.list1)
    def push(self,value):
        self.list1.insert(0,value)
    def peek(self):
        if self.list1 is None:
            raise Exception("Stack is empty")
        else:
            return self.list1[0]
    def pop(self):
        if self.list1 is None:
            raise Exception("Stack is empty")
        else:
            return self.list1.pop(0)
obj1=stack()
obj1.push(33)
obj1.push(45)
print(obj1.peek())
print(obj1.lenght())
print("delete element from stack-->",obj1.pop())
print("Last added Element in Stack-->",obj1.peek())
print(obj1.lenght())
# they work on "LIFO"