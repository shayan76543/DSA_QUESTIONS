string="ShayanAhmad@gmail.com"

if "@" in string:
    first_char=string[0]
    mid_string="*****"
    at_position=string.index("@")
    last_value=string[at_position-1]
    domain=string[at_position:]
    result=first_char+mid_string+last_value+domain
    print(result.lower())
else:
    string=string.replace('(','')
    string=string.replace(')','')
    string=string.replace(',','')
    string=string.replace('-','')
    string=string.replace('+','')
    mid_value="***-***"
    last_number=string[-4:]
    country_code=len(string)%10
    if country_code>0:
        digits="+"+"*"*country_code+"-"+mid_value+"-"+last_number
    else:
        digits=mid_value+"-"+last_number
    print(digits)
# break the larger task in the in smaller task