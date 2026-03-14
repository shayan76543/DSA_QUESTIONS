def longest_common_string(arr):
    if len(arr)==0:
        return ""
    common_string=arr[0]
    for word in arr[1:]:
        i=0
        while i<len(common_string) and i<len(word) and word[i]==common_string[i]:
            i+=1
        common_string=word[:i]
        if common_string == "":
            return ""
    return common_string
arr=["h","he","hello"]
print(longest_common_string(arr))
