def set_mismatch(array):
    n=len(array)
    missing=-1
    duplicate=-1
    frequency=[0]*(n+1)
    for i in array:
        frequency[i]+=1
    for j in range(1,n+1):
        if frequency[j]==2:
            duplicate=j
        elif frequency[j]==0:
            missing=j
    return [missing,duplicate]
array=[1,2,3,4,4,6]
print(set_mismatch(array))
    