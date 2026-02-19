def minimizing_height():
    arr=[1,2,3,4]
    k=2
    n=len(arr)
    arr.sort()
    ans=arr[-1]-arr[0]
    new_min=arr[0]+k
    new_max=arr[-1]-k
    if new_max<new_min:
        new_max,new_min=new_min,new_max
    for i in range(1,n-1):
        sub=arr[i]-k
        add=arr[i]+k
        if sub>=new_min or add<=new_max:
            continue
        if (new_max-sub)<=(add-new_min):
            new_min=sub
        else:
            new_max=add
    return min(ans,new_max-new_min)
print(minimizing_height())          
