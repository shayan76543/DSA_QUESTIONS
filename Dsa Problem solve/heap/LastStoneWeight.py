import heapq
class solution:
    def lastStoneWeight(self,stones:list[int]) ->int:
        Stones=[-stone for stone in stones]
        heapq.heapify(stones)
        while len(Stones)>1:
            x=-heapq.heappop(Stones)
            y=-heapq.heappop(Stones)
            if (x!=y):
                heapq.heappush(Stones,-(x-y))
        if Stones:
            return -Stones[0]
        return 0
stones=[3,2,1,6,16,2]
try1=solution()
print(try1.lastStoneWeight(stones))
