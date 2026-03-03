# Second revision of question
# minimizing_height
def minimizing_height():
    arr=[2,5,4,3,2,1,6,7,30]
    k=3
    n=len(arr)
    arr.sort()
    first_height=arr[-1]-arr[0]
    new_min_height=arr[0]+k
    new_max_height=arr[-1]-k
    if new_min_height>new_max_height:
        new_min_height,new_max_height=new_max_height,new_min_height
    for i in range(1,n-1):
        add=arr[i]+k
        sub=arr[i]-k
        if sub>=new_min_height or add<=new_max_height:
            continue
        if add-new_min_height<new_max_height-sub:
            new_max_height=add
        else:
            new_min_height=sub 
    last_height=new_max_height-new_min_height
    return  f"First Height={first_height}",f"Last Height={last_height}" 
print(minimizing_height())