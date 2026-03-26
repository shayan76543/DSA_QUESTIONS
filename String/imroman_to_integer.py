def roman_integer():
    roman_library={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    string="CMD"
    integer=0
    n=len(string)
    for i in range(0,n):
        if i<n-1 and roman_library[string[i]]<roman_library[string[i+1]]:
            integer-=roman_library[string[i]]
        else:
            integer+=roman_library[string[i]]
    return f"Your Roman To Integer Convergen is={integer}"
print(roman_integer())