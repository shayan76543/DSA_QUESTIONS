def sub_array():
    arr = [9,3,3,3]
    longest_subarray = []

    n = len(arr)
    target = int(input("Enter target: "))

    current = 0
    start = 0
    max_length = 0
    start_index = -1
    end_index = -1

    for i in range(n):
        current += arr[i]

        while current > target:
            current -= arr[start]
            start += 1

        if current == target:
            length = i - start + 1

            if length > max_length:
                max_length = length
                start_index = start
                end_index = i

    if start_index == -1:
        return "Not found"

    for j in range(start_index, end_index+1):
        longest_subarray.append(arr[j])
    return longest_subarray
print(sub_array())