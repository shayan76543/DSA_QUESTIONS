def heapify(arr,ind,value):
    if arr[ind] > value :
        heapify_down(arr,ind,value)
    else:
        heapify_up(arr,ind,value)
    return arr
def heapify_down(arr,ind):
    largest_index=ind
    left_child=(2*ind)+1
    right_child=(2*ind)+2
    if left_child<len(arr) and arr[left_child]>arr[largest_index]:
        largest_index=left_child
    if right_child<len(arr) and arr[right_child]>arr[largest_index]:
        largest_index=right_child
    if largest_index!=ind:
        arr[ind],arr[largest_index]=arr[largest_index],arr[ind] 
        heapify_down(arr,largest_index)
def heapify_up(arr,ind):
    parent_ind=(ind-1)//2
    if parent_ind>=0 and arr[ind]>arr[parent_ind]:
        arr[ind],arr[parent_ind]=arr[parent_ind],arr[ind]
        heapify_up(arr,parent_ind)
heapify([1,2,3,4,5,6],0)
