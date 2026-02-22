def First_occurance():
    string="Shayan ahmad"
    Target="ahmad"
    n=len(string)
    m=len(Target)
    for i in range(n-m+1):
        match=True
        for j in range(m):
            if string[i+j]!=Target[j]:
                match=False
                break
        if match:
            return i
    return -1
print(First_occurance())