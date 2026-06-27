class Solution:
    def smallerNumbersThanCurrent(self, nums):
        n=len(nums)
        smaller=[0]*n
        for i in range(n):
            for j in range(n):
                if nums[i]>nums[j]:
                    smaller[i]+=1
        return smaller
nums=[1,5,3,2,1,7]
obj1=Solution()
print(obj1.smallerNumbersThanCurrent(nums))
        
        