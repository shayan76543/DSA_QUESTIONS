nums = [1, 1]
n = len(nums)
disapper = []
frequency = [0]*(n+1)
for i in nums:
    frequency[i] += 1
for j in range(1, n+1):
    if frequency[j] == 0:
        disapper.append(j)
print(frequency, disapper)
