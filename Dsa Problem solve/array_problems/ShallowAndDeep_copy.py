import copy

a = [[1, 2], [3, 4]]
b = a                  # same list
c = copy.copy(a)       # shallow
d = copy.deepcopy(a)   # deep
c.append([2,3])
print(a)