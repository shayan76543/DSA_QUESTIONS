def gettingTemperature():
    temperature=[30,60,90]
    stack=[]
    ans=[0]*len(temperature)
    index=0
    for i in range(0,len(temperature)):
        while stack and temperature[i]>temperature[stack[-1]]:
            index=stack.pop()
            ans[index]=i-index
        stack.append(i)
    return ans
print(gettingTemperature())
    