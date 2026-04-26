def febonnaci(n):
    if n==2 or n==1:
        return 1
    else :
        return febonnaci(n-1) + febonnaci(n-2)
print(febonnaci(6))