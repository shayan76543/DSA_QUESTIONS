def array_sorted(arr):
    n=len(arr)
    for i in range(0,n-1):
        if arr[i]<=arr[i+1]:
            continue
        else:
            return "array is not sorted"
    return "array is sorted"
arr=[3,45,67,99,105]
print(array_sorted(arr))
# direct method throght function 
def check_sorted(arr):
    return arr==sorted(arr)
print(check_sorted(arr))