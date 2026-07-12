def mountain():
    array = [1, 2, 3, 2, 3]
    i = 1
    if len(array)<3:
        return False
    while i <= len(array)-1 and array[i-1] < array[i]:
        i += 1
    if i == 1:
        return False
    elif i == len(array):
        return False
    while i <= len(array)-1 and array[i-1] > array[i]:
        i += 1
    if i == len(array):
        return True
    else:
        return False
print(mountain())
# [2,5,5]
# [2,1]
# [0,3,2,1]
