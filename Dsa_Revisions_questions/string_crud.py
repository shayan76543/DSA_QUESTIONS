def string_create():
    string=input("Entere your string:")
    return string 
def string_read():
    string="hello jan"
    for i in range(0,len(string)):
        print(string[i],end=" -- ")
def string_update():
    string="khan jan"
    n=len(string)
    replace="jan"
    if replace in string:
        index=string.index(replace)
    list1=list(string)
    for i in range(index,n):
        list1[i]=input("Entere new string:")
    string="".join(list1) 
    return string  
def string_delete():
    string="hello jan"
    n=len(string)
    replace="jan"
    index=string.find(replace)
    list1=list(string)
    for i in range(0,index):
        print(list1[i],end="")
def string_delete():
    string = "hello jan"
    replace = "jan"
    index = string.find(replace)
    if index != -1:
        string = string[:index] + string[index + len(replace):]
    return string
class string_crud:
    def __init__(self):
        self.string=""
    def string_create(self):
        variable=input("Entere your string:")
        self.string+=variable
    def string_read(self):
        return self.string
    def string_update(self):
        replace=input("Entere strings you wanna update")
        update=int(input("Entere How much numbers you want to update:"))
        index=self.string.find(replace)
        if index!=-1:
            list1=list(self.string)
            for i in range(index,index+update):
                list1[i]=input("Entere new integer:")
            self.string="".join(list1)    
    def delete_string(self):
        delete=input("Entere your replace string:")
        index=self.string.find(delete)
        if index!=-1:
            self.string=self.string[:index]+self.string[index+len(delete):]
obj1=string_crud()
obj1.string_create()
obj1.string_update()
obj1.delete_string()
print(obj1.string_read())



    

        





