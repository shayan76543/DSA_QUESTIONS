# letters = "bcabc"
# monotomic = []
# seen = set()
# for i in letters:
#     if i in seen:
#         continue
#     seen.add(i)
#     monotomic.append(i)
# monotomic.sort()
# string="".join(monotomic)
# print(string)
class Solution(object):
    def removeDuplicateLetters(self, s):
        monotomic=[]
        seen=set()
        for i in s:
            if i in seen:
                continue 
            seen.add(i)
            monotomic.append(i)
        monotomic.sort()
        sd="".join(monotomic)
        return sd
s="cbacdcbc"
obj1=Solution()
print(obj1.removeDuplicateLetters(s))