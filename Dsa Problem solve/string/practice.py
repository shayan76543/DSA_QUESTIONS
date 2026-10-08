# string="abcdabcD".lower()
# k=0
# n=len(string)
# for i in range(2,n//2+1):
#     target=n%i
#     print(n,"%",i,"=",n%i)
#     if target==0:
#         k=i
#     repeat=n//k
# result=string[0:k]*repeat
# if string==result:
#     print(True)
# print(k,n,repeat,result)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        k=0
        n=len(s)
        for i in range(1,n//2+1):
            if n%i==0:
                k=i
                print(k)
            repeat=n//k
            result=s[0:k]*repeat
            if result==s:
                return True,n,"%",i,n%i,repeat,result,k    
        return False,n,"%",i,n%i
try1=Solution()
s="ababababab"
print(try1.repeatedSubstringPattern(s))

        


        
