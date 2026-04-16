class dequeue:
    def __init__(self):
        self.array=[]
    def insert_at_front(self,value):
        self.array.insert(0,value)
    def delete_at_end(self):
        return self.array.pop()
    def insert_at_end(self,value):
        self.array.append(value)
    def delete_at_front(self):
        return self.array.pop(0)
obj1=dequeue()
obj1.insert_at_end(33)
obj1.insert_at_front(32)
obj1.insert_at_end(65)
print(obj1.delete_at_front())
print(obj1.delete_at_end())
    

