class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        replacement=s.replace('-','')
        capitilization=replacement.upper()
        modulo=len(capitilization)%k
        groups=[]
        if modulo==0:
            for i in range(modulo,len(capitilization),k):
                groups.append(capitilization[i:i+k])
        else:
            groups=[capitilization[:modulo]]
            for i in range(modulo,len(capitilization),k):
                groups.append(capitilization[i:i+k])
        result="-".join(groups)
        return result
        
s="5F3Z-2e-9-w"
k=4
try1=Solution()
print(try1.licenseKeyFormatting(s,k))