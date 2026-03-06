def parenthesis_checker():
    brackets="{[(]})"
    stack=[]
    for i in brackets:
        if i in "([{":
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            p=stack.pop()
            if (
                p=="(" and i==")"
                or p=="{" and i=="}" 
                or p== "[" and i=="]"
            ):
                continue
            else:
                return False
    return len(stack)==0
print(parenthesis_checker())    



