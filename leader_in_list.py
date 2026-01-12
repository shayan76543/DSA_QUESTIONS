arr=[2000,43,13,28,98,54,32,1,32,76,45,923,4]
n=len(arr)
leader_elements=arr[-1]
reverse_num=0
print(leader_elements,end=" ")
for i in range(n-2,-1,-1):
    if leader_elements<arr[i]:
        leader_elements=arr[i]
        print(leader_elements,end=" ")
reverse_num
        

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)    