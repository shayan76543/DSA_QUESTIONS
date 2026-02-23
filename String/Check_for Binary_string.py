def binary_string():
    string="0000"
    n=len(string)
    found=True
    for i in range(0,n):
        if string[i]!= "0" and string[i]!="1":
            found=False
            return found
    return found
print(binary_string())
        