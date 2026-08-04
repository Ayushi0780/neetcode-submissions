class Solution:
    def isPalindrome(self, s: str) -> bool:
        #he cleaned string equals its reverse
        # cleaned = "".join(char.lower() for char in s if char.isalnum())
        # return cleaned == cleaned[::-1]  
        clear="".join(c.lower() for c in s if c.isalnum())
        return clear == clear[::-1] 
        