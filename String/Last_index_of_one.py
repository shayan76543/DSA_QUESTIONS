def Last_index_of_one():
    string="00000001"
    n=len(string)
    Last_index=None
    for i in range(0,n):
        if string[i]=="1":
            Last_index=i
    if Last_index is None:
        return -1
    else:
        return Last_index
print(Last_index_of_one())