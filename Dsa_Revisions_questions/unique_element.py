# revision question of unique Element
def unique_element():
    str1="shyanAhmad"
    str2="shayankhan"
    unique_element=""
    for i in str1:
        found=False
        for j in str2:
            if i==j:
                found=True
        if found is False:
            unique_element+=i
    for i in str2:
        found=False
        for j in str1:
            if i==j:
                found=True
        if found is False:
            unique_element+=i
    return unique_element
print(unique_element())
       

