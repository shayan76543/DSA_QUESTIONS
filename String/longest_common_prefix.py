def longest_common_prefix(arr):
    if len(arr)==0:
        return ""
    prefix=arr[0]
    for word in arr[1:]:
        i=0
        while i<len(prefix) and i<len(word) and word[i]==prefix[i]:
            i+=1
        prefix=word[:i]
        if prefix == "":
            return ""
    return prefix
arr=["shayan","shaya","shan"]
print(longest_common_prefix(arr))



