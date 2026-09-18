def heapify_down(arr, ind):
    largest_index = ind
    left_child = (2 * ind) + 1
    right_child = (2 * ind) + 2
    if left_child < len(arr) and arr[left_child] > arr[largest_index]:
        largest_index = left_child
    if right_child < len(arr) and arr[right_child] > arr[largest_index]:
        largest_index = right_child
    if largest_index != ind:
        arr[ind], arr[largest_index] = arr[largest_index], arr[ind]
        heapify_down(arr, largest_index)
def heapify_up(arr, ind):
    parent_ind = (ind - 1) // 2
    if parent_ind >= 0 and arr[ind] > arr[parent_ind]:
        arr[ind], arr[parent_ind] = arr[parent_ind], arr[ind]
        heapify_up(arr, parent_ind)
def heapify(arr):
    start = (len(arr) // 2) - 1
    for ind in range(start, -1, -1):
        heapify_down(arr, ind)
    return arr
arr = [1, 2, 3, 4, 5, 6]
print(heapify(arr))