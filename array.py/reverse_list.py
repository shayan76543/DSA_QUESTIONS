# Reversing a list
arr=[4,5,3,6,7,1,2,4,7,6]
n=len(arr)
j=n-1
for i in range(0,n//2):
    arr[i],arr[j]=arr[j],arr[i]
    j-=1     
print(arr,end="")
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)


