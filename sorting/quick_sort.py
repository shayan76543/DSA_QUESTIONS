def quick_sort(array, l, r):
    if l < r:
        p = partition(array, l, r)
        quick_sort(array, l, p - 1)
        quick_sort(array, p + 1, r)


def partition(array, l, r):
    pivot = array[l]
    i = l + 1
    j = r
    while True:
        while i <= j and array[i] < pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            break
    array[l], array[j] = array[j], array[l]
    return j


array = [3, 6, 5, 1, 3, 2, 4, 7, 9, 7, 2, 4]
quick_sort(array, 0, len(array) - 1)
print(array)
