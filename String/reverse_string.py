def reverse_string():
    reverse_string1=""   # I did mistake there by not assigning here Double quotes like this =("")
    string="My Name is Shayan"
    n=len(string)
    for i in range(n-1,-1,-1):
        reverse_string1+=string[i]
    return reverse_string1
print(reverse_string())