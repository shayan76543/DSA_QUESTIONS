def vow_con():
    string="shayan_ahmad_awan@gmail.com"
    vowel=0
    consonent=0
    other_char=0
    for i in string:
        if i.isalpha():
            if i in "aeiou":
                vowel+=1
            else:
                consonent+=1
        else:
            other_char+=1
    return f"vowel={vowel} or consonent={consonent} or other-character={other_char}"
print(vow_con())
# IMPORTANT METHOD IN STRING
# isdigit()

# isalnum()

# isspace()