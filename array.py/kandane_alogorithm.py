# Kandane's Algorithm to find the maximum sum of a contiguous subarray
arr=[9,8,4,-19,-7,5,8,2,4,5,-2,3]
n=len(arr)
largest_sum=float("-inf")
current_sum=0
for i in range(n):
    current_sum+=arr[i]
    if current_sum>largest_sum:
        largest_sum=current_sum
    elif current_sum<0:
        current_sum=0
print(largest_sum)
# Time Complexity: O(n)
# Space Complexity: O(1)
