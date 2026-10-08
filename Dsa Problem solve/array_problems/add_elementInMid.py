arr = [10, 20, 30, 40, 50]
position = 2
value = 25
arr.append(None)  # create extra space
for i in range(len(arr) - 1, position, -1):
    arr[i] = arr[i - 1]
arr[position] = value

print(arr)