class queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if self.isEmpty():
            print("queue is empty")
            return
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()    
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
            return 
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def isEmpty(self):
        if not self.stack1 and not self.stack2:
            return True
        return False

queen = queue()
queen.push(1)
queen.push(2)
queen.push(3)
queen.push(4)
print(queen.pop())
print(queen.pop())
