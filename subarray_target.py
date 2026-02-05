def sub_array():
    arr=[4,1,7,6,3,9,6,5,3,5,1]
    n=len(arr)
    target=28
    current=0
    start=0
    for i in range(0,n):
        current+=arr[i]

        if current>target:
            while current>target:
                current-=arr[start]
                start+=1
        if current==target:
            return "find",start,i,n-1 
    return "not found"    
print(sub_array())
        