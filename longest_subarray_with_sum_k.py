def sub_array():
    arr=[4,1,7,6,3,9,6,5,3,5,1,15,2,2]
    longest_subarray=[]
    n=len(arr)
    target=int(input("entere which number you want:"))
    current=0
    start=0
    end=0
    found=False
    starts=0
    max_subarray_target=0
    for i in range(0,n):
        current+=arr[i]
        if current>target:
            while current>target:
                current-=arr[start]
                start+=1
        if current==target:
            found=True
            if max_subarray_target<i-start:
                max_subarray_target=i-start
                starts=start
                end=i
    if not found:
        return "not found"
    found=False
    for j in range(starts,end+1): 
        longest_subarray.append(arr[j])
    return longest_subarray
print(sub_array())
        