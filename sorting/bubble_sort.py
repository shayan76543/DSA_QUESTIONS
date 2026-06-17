# bubble sort used the method of swapping of adjacent element 
# they mistake i am making in bubbule sort to make them sort in the way of selection sort 
def bubble_sort():
    array=[33,45,23,76,43]
    n=len(array)
    for i in range(0,n):
        for j in range(0,n-1-i):
            if array[j]>=array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]      
    return array
print(bubble_sort())
