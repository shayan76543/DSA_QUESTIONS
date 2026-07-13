from collections import Counter
name = "shayan ahmad"
frequency = Counter(name)
print(frequency)
s="shayan ahmad"
frequency={}
for i in s:
    frequency[i]=frequency.get(i,0)+1