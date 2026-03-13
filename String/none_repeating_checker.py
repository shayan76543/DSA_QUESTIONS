def none_repeat_checker():
    word = "Shayanahmad".lower()
    characters = [0]*26
    none_repeat=""
    n=len(characters)
    for i in word:
        characters[ord(i)-ord("a")] += 1
    for i in range(n):
        if characters[i]==1:
            none_repeat+=chr(i+ord("a"))
    if not none_repeat:
        none_repeat="@"
    return none_repeat
print(none_repeat_checker())
