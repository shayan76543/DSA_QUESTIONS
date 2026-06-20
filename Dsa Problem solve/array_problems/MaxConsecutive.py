class Solution:
    def findMaxConsecutiveOnes(self,nums):
        Count=0
        MaxCount=0
        for i in range(len(nums)):
            if nums[i]==1:
                Count+=1
                MaxCount=max(Count,MaxCount)
            else:
                Count=0
        return MaxCount
obj1=Solution()
nums=[1,0,1,0,1,1]
print(obj1.findMaxConsecutiveOnes(nums))
