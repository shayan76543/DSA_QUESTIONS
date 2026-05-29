def divide(arr, start, end):
    """
    Recursively divides the array into smaller subarrays.
    """
    # Base case: If the subarray has 1 or 0 elements, it's already sorted
    if start >= end:
        return

    # Find the middle point to split the array
    # Using floor division (//) in Python for integer results
    mid = start + (end - start) // 2

    # Recursively sort the left half
    divide(arr, start, mid)

    # Recursively sort the right half
    divide(arr, mid + 1, end)

    # Merge the two sorted halves together
    conquer(arr, start, mid, end)


def conquer(arr, start, mid, end):
    """
    Merges two sorted subarrays back into the original array.
    """
    # Create a temporary list to store the merged elements
    merged = []

    idx1 = start    # Pointer for the first sorted subarray (left side)
    idx2 = mid + 1  # Pointer for the second sorted subarray (right side)

    # Compare elements from both subarrays and append the smaller element
    while idx1 <= mid and idx2 <= end:
        if arr[idx1] <= arr[idx2]:
            merged.append(arr[idx1])
            idx1 += 1
        else:
            merged.append(arr[idx2])
            idx2 += 1

    # If there are remaining elements in the left subarray, copy them
    while idx1 <= mid:
        merged.append(arr[idx1])
        idx1 += 1

    # If there are remaining elements in the right subarray, copy them
    while idx2 <= end:
        merged.append(arr[idx2])
        idx2 += 1

    # Copy the sorted elements from the temporary list back into the original array
    for i in range(len(merged)):
        arr[start + i] = merged[i]


# Driver code to test the execution
if __name__ == "__main__":
    elements = [45, 7, 21, 89, 10, 5, 24]
    
    print("Original Array:", elements)
    
    # Call the divide function with initial parameters
    divide(elements, 0, len(elements) - 1)
    
    print("Sorted Array:  ", elements)