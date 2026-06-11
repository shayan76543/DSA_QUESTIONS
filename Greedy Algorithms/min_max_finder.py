def min_max(array):
    n=len(array)
    max=0
    min=0
    j=n-1
    array.sort()
    for i in range(n//2):
        max=max+abs(array[i]-array[j])
        j-=1
    for i in range(0, n):
        min+=abs(array[2*i] - array[2*i+1])
    return min,max
array=[5,4,3,2,6,5]
print(min_max(array))
print(array)
