def non_repeating_longest_sub(string):
    n=len(string)
    left=0
    max_len=0
    box=set()
    for right in range(0,n):
        while string[right] in box:
            box.remove(string[left])
            left+=1
        box.add(string[right])
        max_len=max(max_len,right-left+1)
    return max_len
print(non_repeating_longest_sub("shayan_ahmad"))
