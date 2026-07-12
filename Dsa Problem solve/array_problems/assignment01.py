class Solution(object):
    def plusOne(self, digits):
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
        return digits
digits=[1,2,4,3,9,9]
obj1=Solution()
print(obj1.plusOne(digits))