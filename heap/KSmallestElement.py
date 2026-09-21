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