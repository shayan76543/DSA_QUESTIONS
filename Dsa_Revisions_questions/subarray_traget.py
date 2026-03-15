def subarray_target(arr):
    target_list=[]
    n=len(arr)
    target=int(input("Entere number which sum you wanna found:"))
    current=0
    start=0
    start_index=-1
    end_index=-1
    max_lenght=0
    for i in range(0,n):
        current+=arr[i]
        if current>target:
            while current>target:
                current-=arr[start]
                start+=1
        if current==target:
            lenght=i-start+1
            if lenght>max_lenght:
                max_lenght=lenght
                start_index=start
                end_index=i
    if (start_index==-1) and (end_index==-1):
        return "not found"
    for i in range(start_index,end_index+1):
        target_list.append(arr[i])
    return target_list
arr=[3,3,3,9]
print(subarray_target(arr))

    

    
