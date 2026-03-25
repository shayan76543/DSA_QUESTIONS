def string_compression():
    string="aaabba"
    result=[]
    n=len(string)
    character=string[0]
    count=1
    for i in range(1,n):
        if string[i]==character:
            count+=1
        else: 
            if count>1:
                result.append(character + str(count))
            else:
                result.append(character)
            count=1
            character=string[i]
    if count>1:
        result.append(character + str(count))
    else:
        result.append(character)
    return "".join(result)
print(string_compression())