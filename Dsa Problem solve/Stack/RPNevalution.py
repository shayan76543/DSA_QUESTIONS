# Learning in this problem is Truncate like print the value  near the zeronlike 
# int(5 / float(-3))
# -1 ✅ not -2
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        left = None
        right = None
        result = None
        n = len(tokens)
        for i in range(0, n):
            if tokens[i] in ("+", "-","*","/"):
                right = stack.pop()
                left = stack.pop()
                if tokens[i] == "+":
                    result = left+right
                    stack.append(result)
                elif tokens[i] == "-":
                    result = left-right
                    stack.append(result)
                elif tokens[i] == "*":
                    result = left*right
                    stack.append(result)
                elif tokens[i] == "/":
                    result = int(float(left) / right)
                    stack.append(result)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
tokens=[3,2,"+"]
obj1=Solution()
print(obj1.evalRPN(tokens))
