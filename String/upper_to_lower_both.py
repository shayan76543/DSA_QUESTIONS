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
# ✅ 5. Most Asked String Questions
# If you master these, you are strong:
# Reverse a string .
# Check palindrome
# Count vowels/consonants
# Check anagram
# Longest substring without repeating characters
# Remove duplicates
# String compression
# Valid parentheses
# Roman to integer
# Implement strstr()
