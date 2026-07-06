class Solution:
    def finalPrices(self,prices):
        stack=[]
        discount=[0]*len(prices)
        for i in range(0,len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                index=stack.pop()
                discount[index]=prices[index]-prices[i]
            stack.append(i)
        while stack:
            index=stack.pop()
            discount[index]=prices[index]
        return discount
prices=[8,4,6,2,3]
obj=Solution()
print(obj.finalPrices(prices))
        
        