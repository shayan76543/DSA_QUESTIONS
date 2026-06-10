def max_min(array, start, end):
    if array[start] == array[end]:
        return array[start], array[end]
    if array[start+1] == array[end]:
        if (array[start] < array[end]):
            return array[start], array[end]
        else:
            return array[end], array[start]
    mid = start+(end-start)//2
    min1, max1 = max_min(array, start, mid)
    min2, max2 = max_min(array, mid+1, end)
    return min(min1, min2), max(max1, max2)
array = [4,1,9,10,5,1,2,9,65,23]
min, max = max_min(array, 0, len(array)-1)
print("minimum value is =", min)
print("maximun value is =", max)
