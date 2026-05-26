def selection_sort():
    array=[33,2,5,15,6,7,54,3]
    n=len(array)
    for i in range(n-1):
        min=i
        for j in range(i,n):
            if array[min]>array[j]:
                min=j
        array[i],array[min]=array[min],array[i]
    return array
print(selection_sort())