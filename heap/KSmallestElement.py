import heapq
class solution:
    def kSmallestElememt(self,num1,num2,k):
        result=[]
        heap=[]
        for i in range(min(len(num1),k)):
            heapq.heappush(heap,(num1[i]+num2[0],i,0))
        while heap and len(result)<k:
            total,i,j=heapq.heappop(heap)
            result.append((num1[i],num2[j]))
            if j+1<len(num2):
                heapq.heappush(heap,(num1[i]+num2[j+1],i,j+1))
        return result
num1=[5,6,7,8]
num2=[7,25,23,26]
try1=solution()
print(try1.kSmallestElememt(num1,num2,2))
# outcomes
# Given two arrays, find the k pairs with the smallest sums.
# Instead of generating every possible pair:
# 5+7
# 5+25
# 5+23
# 5+26
# 6+7
# 6+25
# ...
# you use a min-heap to continuously keep track of the smallest available pair
# General Pattern :

# Sorted/structured candidates
#         ↓
# Put initial candidates in Min Heap
#         ↓
# Remove smallest
#         ↓
# Use that candidate to generate its next candidate
#         ↓
# Put next candidate in heap
#         ↓
# Repeat K times
# Whenever you see a problem containing:

# K smallest
# K largest
# K closest
# K most frequent
# K cheapest
# K highest/lowest
# "Find the next smallest..."
# "Find top K..."

# 🚨 Think: Heap

# Especially when you don't want to process/sort everything.

# For example:

# K smallest elements       → Min Heap / Max Heap depending on approach
# K largest elements        → Min Heap of size K
# K closest points          → Heap
# K most frequent elements  → Heap
# K smallest pairs          → Min Heap
# Merge K sorted lists      → Min Heap
# Kth largest element       → Min Heap of size K
# Kth smallest element      → Max Heap of size K

# The exact heap direction depends on the problem.
# Time Complexity: O(k log k)
# Space Complecity: O(k)