arr=[33,2,1,4,5,7,12,0,-1,-5,100,23,100]
largest_num=float('-inf')
n=len(arr)
for i in range(0,n):
    if arr[i]>largest_num:
        largest_num=arr[i]
print(f"the largest number is: {largest_num} at index:{arr.index(largest_num)}")
