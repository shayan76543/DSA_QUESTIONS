def upper_lower():
    string="ShaYaN AhmAD"
    upper_case=""
    for ch in string:
        if "a"<=ch<="z":
            upper_case+=chr(ord(ch)-(ord("a")-ord("A")))
        else:
            upper_case+=ch
    return upper_case
def lower_upper():
    string="ShaYaN AhmAD"
    lower_case=""
    for ch in string:
        if "A"<=ch<="Z":
            lower_case+=chr(ord("a")-ord("A")+ord(ch))
        else:
            lower_case+=ch
    return lower_case
print(lower_upper())
print(upper_lower())
