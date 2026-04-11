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

