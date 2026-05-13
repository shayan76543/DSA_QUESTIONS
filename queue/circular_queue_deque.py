class circular_list:
    def __init__(self):
        self.size=5
        self.array=[None]*self.size
        self.front=self.rear=-1
    def enqueue(self,value):
        if (self.rear+1) % self.size == self.front:
            print("queue is full") 
        elif self.rear == -1:
            self.rear=self.front=0
            self.array[self.rear]=value
        else:
            self.rear=(self.rear+1) % self.size
            self.array[self.rear]=value
    def deque(self):
        if self.rear==-1:
            print("your queue is empty")
        elif self.rear==self.front:
            print(self.array[self.front])
            self.front=self.rear=-1
        else:
            print(self.array[self.front])
            self.front=(self.front+1) % self.size
obj1=circular_list()
obj1.enqueue(73)
obj1.enqueue(2)
obj1.enqueue(12)
obj1.enqueue(54)
obj1.enqueue(234)
obj1.enqueue(21)






