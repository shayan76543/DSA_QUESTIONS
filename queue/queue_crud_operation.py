class queue:
    def __init__(self):
        self.array=[]
    def isempty(self):
        return len(self.array)==0
    def insert(self,value):
        self.array.append(value)
    def delete(self):
        if self.isempty():
            raise Exception("your list is empty")
        else:
            return self.array.pop(0)
obj1=queue()
obj1.insert(23)
obj1.insert(43)
obj1.insert(53)
print(obj1.delete())
# they work on "FIFO"