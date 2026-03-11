def anagram_checker():
    str1="shayan"
    str2="nasayh"
    n=len(str1)
    m=len(str2)
    if n!=m:
        return False
    count=[0]*26
    for i in str1:
        count[ord(i)-ord("a")]+=1
    for j in str2:
        count[ord(j)-ord("a")]-=1
    for c in count:
        if c!=0:
            return False
    return True
print(anagram_checker())
