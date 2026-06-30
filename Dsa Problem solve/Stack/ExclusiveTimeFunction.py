class Solution:
    def ExclusiveFunction(self,n:int,logs:list[str])->list[int]:
        result=[0]*n
        stack=[]
        previousTime=0
        for log in logs:
            functionId,status,timeStamp=log.split(":")
            functionId=int(functionId)
            timeStamp=int(timeStamp)
            if status=="start":
                if stack:
                    result[stack[-1]]+=timeStamp-previousTime
                stack.append(functionId)
                previousTime=timeStamp
            else:
                result[stack.pop()]+=timeStamp-previousTime+1
                previousTime=timeStamp+1
        return result
n=1
logs=["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
obj1=Solution()
print(obj1.ExclusiveFunction(n,logs))



