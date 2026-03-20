def remove_duplicate():
    string="ShayanAhmadAwan".lower()
    arr=list(string)
    n=len(arr)
    seen=26*[False]
    write=0
    for read in range(0,n):
        index=ord(arr[read])-ord('a')
        if  not seen[index]:
            seen[index]=True
            arr[write]=arr[read]
            write+=1 
            # with write variable we can ignore all remaining value after overwriting 
    result="".join(arr[:write])
    return result
print(remove_duplicate())
    