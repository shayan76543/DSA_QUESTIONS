def stack():
    array=[3,3,4,9,2,4,5]
    max_area=0
    stack=[]
    array.append(0)
    for i in range(0,len(array)):
        while stack and array[i]<array[stack[-1]]:
            height=array[stack.pop()]
            if stack:
                width=i-stack[-1]-1
            else:
                width=i
            area=height*width
            max_area=max(max_area,area)
        stack.append(i)
    return max_area
print(stack())

