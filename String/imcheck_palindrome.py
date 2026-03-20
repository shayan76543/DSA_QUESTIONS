def check_palindrome():
    string="racktyuytkcar"
    n=len(string)
    j=n-1
    for i in range(0,n//2):
        if string[i]==string[j]:
            j-=1
            continue
        else:
            return "Not palindrome"
    return "string is palindrome"
print(check_palindrome())