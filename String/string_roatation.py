def string_rotation():
    original="abcd"
    n=len(original)
    check="cdab"
    if len(original)!=len(check):
        return "fail rotation"
    if original in check+check:
        return "rotation successfull"
    return "rotation is fail"
print(string_rotation())
