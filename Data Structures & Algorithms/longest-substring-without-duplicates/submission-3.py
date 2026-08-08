class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left=0
        right=0
        max_sub=0
        while right <len(s):
            if s[right] in seen:
                left=max(left,seen[s[right]]+1)


            max_sub=max(max_sub,right-left+1)   
            seen[s[right]]=right
            right+=1 
        return max_sub    



        