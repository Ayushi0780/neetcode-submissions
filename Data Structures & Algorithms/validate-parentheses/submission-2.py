class Solution:
    def isValid(self, s: str) -> bool:
        brac={']':'[',")":"(","}":"{"}
        stack=[]
        for c in s:
            if c in brac:
                if not stack:
                    return False
                top=stack.pop()
                if brac[c]!=top:
                    return False
            else:
                stack.append(c)
        return len(stack)==0
                   
        
        