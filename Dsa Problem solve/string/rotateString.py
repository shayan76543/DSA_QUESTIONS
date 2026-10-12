class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        result=""
        for i in range(0,n):
            result=s[i:]+s[:i]
            if result==goal:
                return True
        return False
s="abcd"
goal="cdab"
try1=Solution()
print(try1.rotateString(s,goal))
