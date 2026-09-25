import heapq
class Solution:
    def isPossible(self, target: list[int]) -> bool:
        result=0
        total=sum(target)
        heap=[-x for x in target]
        heapq.heapify(heap)
        while True:
            largest=-heapq.heappop(heap)
            if largest==1:
                return True
            result=total-largest
            if result==1:
                return True
            if result==0 or largest<=result:
                return False
            previous=largest%result
            if previous==0:
                return False
            heapq.heappush(heap,-previous)
            total=result+previous
target=[9,3,5]
try1=Solution()
print(try1.isPossible(target))
