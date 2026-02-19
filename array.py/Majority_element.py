# Function to find the majority element in an array
def majority():
    arr=[7,3,7,2,2,7,7,7,7,7,9]
    frequency=0
    n=len(arr)
    majority_element=arr[0]
    count=1
    for i in range(1,n):
        if count==0:
            majority_element=arr[i]
            count=1
        elif arr[i]==majority_element:
            count+=1
        else:
            count-=1
    for i in range(0,n):
        if arr[i]==majority_element:
            frequency+=1
    if frequency>n//2:
        return majority_element,frequency,n,count
    else:
        return -1
print(majority())
# Time Complexity: O(n)
# Space Complexity: O(1)
