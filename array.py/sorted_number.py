def jump(arr):
    n=len(arr)
    count0=0
    count1=0
    count2=0
    count=0
    for i in range(0,n):
        if arr[i]==0:
            count0+=1
        if arr[i]==1:
            count1+=1
        if arr[i]==2:
            count2+=1
    while count0>0:
        arr[count]=0
        count+=1
        count0-=1
    while count1>0:
        arr[count]=1
        count+=1
        count1-=1
    while count2>0:
        arr[count]=2
        count+=1
        count2-=1
    return arr
arr=[2,1,0,0,1,1,2,1,2]
print(jump(arr))

    
