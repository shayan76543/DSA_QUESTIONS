def string_rotation():
    original="abcd"
    n=len(original)
    check="cbab"
    k=1
    for i in range(n):
        check=check[k:]+check[:k]
        if check==original:
            return "rotation successfull"
    return "rotation is fail"
print(string_rotation())
