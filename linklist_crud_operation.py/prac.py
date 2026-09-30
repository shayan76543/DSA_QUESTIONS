# s="sha-yan-ahm-ad"
# string=""
# dashess=""
# k=2
# for i in s:
#     if i=="-":
#         continue
#     else:
#         string+=i
# string.upper()
# dashes="-"
# no_of_dashes=len(string)%k
# dashess+=string[:no_of_dashes]
# for i in range(string):
    
s = input("Enter license key: ")
k = int(input("Enter k: "))

# Remove existing dashes and convert to uppercase
s = s.replace("-", "").upper()
# Find size of the first group
first_size = len(s) % k

# If remainder is 0, first group should have k characters
if first_size == 0:
    first_size = k

# Create the first group
groups = [s[:first_size]]
# Create the remaining groups of size k
for i in range(first_size, len(s), k):
    groups.append(s[i:i+k])
# Join groups with dashes
result = "-".join(groups)
print(result)