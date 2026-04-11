def array_create():
    array=[]
    n=int(input("Entere number of array you want to entere:"))
    for i in range(0,n):
        i=int(input("Entere Number:"))
        array.append(i)
    return array
def array_read():
    arr=[4,6,7,1,2,4]
    n=len(arr)
    for i in range(0,n):
        print(arr[i],end=" array Elements -->")
    print("Stop")
def update_array():
    arr=[3,6,7,3,11,9]
    arr[3]=23
    return arr
def delete_array():
    arr=[4,6,7,8,9,23,56]
    n=len(arr)
    value=int(input("Entere your value:"))
    if value in arr:
        index=arr.index(value)
        for i in range (index,n-1):
            arr[i]=arr[i+1]
        arr.pop()
    return arr
class array_crud:
    def __init__(self):
        self.list=[]
    def add_value_array(self):
        n=int(input("Entere how many numbers you wanna insert in list:"))
        for i in range(0,n):
            value=int(input("Entere array Elements:"))
            self.list.append(value)
    def read_array(self):
        for i in range(0,len(self.list)):
            print(self.list[i],end="<-->")
    def update_array(self):
        i=int(input("Entere index of the value:"))
        if 0<=i<len(self.list):
            value=int(input("entere value which you want to insert:"))
            self.list[i]=value
        else:
            print("index out of range:")
    def delete_array(self):
        value=int(input("Entere number which you want to delete:"))
        if value in self.list:
            index=self.list.index(value)
            for i in range(index,(len(self.list))-1):
                self.list[i]=self.list[i+1]
            self.list.pop()
        else:
            print("value are not found in list")
        # return self.list
l1=array_crud()
l1.add_value_array()
l1.update_array()
l1.delete_array()
l1.read_array()



