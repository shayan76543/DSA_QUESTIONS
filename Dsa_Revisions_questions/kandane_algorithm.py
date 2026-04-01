def kandane_algorithm(arr):
    n=len(arr)
    current_sum=0
    max_sum=0
    for i in range(0,n):
        current_sum+=arr[i]
        if current_sum>max_sum:
            max_sum=current_sum
        if current_sum<0:
            current_sum=0 
    return max_sum 
arr=[3,4,6,5,1,-9,4]
print(kandane_algorithm(arr))