class node:
    def __init__(self, value):
        self.data = value
        self.address = None
        self.previous = None


class dll:
    def __init__(self, head=None):
        self.head = head

    def insert_end(self, value):
        temp = node(value)
        if self.head == None:
            self.head = temp
            return
        t1 = self.head
        while t1.address != None:
            t1 = t1.address
        t1.address = temp
        temp.previous = t1

    def insert_beggining(self, value):
        temp = node(value)
        if self.head == None:
            self.head = temp
            return
        temp.address = self.head
        self.head.previous = temp
        self.head = temp

    def insert_mid(self, value, x):
        temp = node(value)
        t1 = self.head
        while t1.address != None:
            t1 = t1.address
            if t1.data == x:
                break
        temp.address = t1.address
        t1.address.previous = temp
        t1.address = temp
        temp.previous = t1

    def delete_dll(self, value):
        temp = node(value)
        t1 = self.head
        if t1.data == value:
            self.head = t1.address
            self.head.previous = None
            return
        while t1.address != None:
            if t1.data == value:
                t1.previous.address = t1.address
                t1.address.previous = t1.previous
                return
            else:
                t1 = t1.address
        if t1.data == value:
            t1.previous.address = None

    def printdll(self):
        t1 = self.head
        while t1.address != None:
            print(t1.data, end="  <--> ")
            t1 = t1.address
        print(t1.data)
obj1 = dll()
obj1.insert_end(33)
obj1.insert_end(44)
obj1.insert_end(45)
obj1.insert_end(46)
obj1.insert_end(47)
obj1.insert_end(48)
obj1.insert_beggining(32)
obj1.insert_mid(45.5, 45)
obj1.delete_dll(32)
obj1.delete_dll(45.5)
obj1.printdll()
