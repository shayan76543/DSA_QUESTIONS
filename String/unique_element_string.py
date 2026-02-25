def unique_element1():
    str1="shayanahmad"
    str2="shayanaqank"
    unique_elementa=""
    for i in str1:
        found=False
        for j in str2:
            if i==j:
                found=True
                break
        if found is False:
           if i not in unique_elementa:
            unique_elementa+=i
    for i in str2:
        found=False
        for j in str1:
            if i==j:
                found=True
                break
        if found is False:
           if i not in unique_elementa:
               unique_elementa+=i
    return unique_elementa
# print(unique_element1())
# Know using builtin function 
def unique_element2():
    str1="shayanahmad"
    str2="shayanawan"
    unique_elementb=""
    unique_elementb=set(str1) ^ set(str2)
    return "".join(sorted(unique_elementb))
print(unique_element2()
    
    