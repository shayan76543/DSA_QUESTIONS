from collections import Counter
def removeDuplicate(s:str)->str:
    frequency=Counter(s)
    visited=set()
    stack=[]
    for i in s:
        frequency[i]-=1
        if i in visited:
            continue
        while (stack and stack[-1]>i and frequency[stack[-1]]>0):
            removed=stack.pop()
            visited.remove(removed)
        stack.append(i)
        visited.add(i)
    return "".join(stack)
s="shayanahmad"
print(removeDuplicate(s))