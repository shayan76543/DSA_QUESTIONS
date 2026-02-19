# SEARCH A NUMBER IN A LIST AND PRINT ITS INDEX
arr=[3,2,5,7,6,8,12,43,67]
n=len(arr)
search_num=int(input("ENTERE THE NUMBER TO BE SEARCHED: "))
for i in range(n):
    if arr[i]==search_num:
        print(f"search_number is:{search_num} fond at index: {i}")
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
