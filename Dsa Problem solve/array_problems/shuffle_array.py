class Solution:
    def ShuffleArray(self,nums):
        n=len(nums)//2
        shuffle=[]
        for i in range(n):
            shuffle.append(nums[i])
            shuffle.append(nums[n+i])
        if len(nums)%2==1:
            shuffle.append(nums[-1])
        return shuffle
nums=[3,2,4,1,5,3,4,3,2]    
object1=Solution()
print(object1.ShuffleArray(nums))

