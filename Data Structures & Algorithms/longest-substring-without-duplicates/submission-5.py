class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen={}
        # left=0
        # right=0
        # max_sub=0
        # while right<len(s):

        #     if s[right] in seen:
        #         left=max(left,seen[s[right]]+1)


        #     max_sub=max(max_sub,right-left+1)
        #     seen[s[right]]=right
        #     right+=1
        # return max_sub       
        seen = set()  # Stores unique characters in current window
        left = 0
        right = 0
        max_sub = 0
        
        while right < len(s):
            # Shrink window step-by-step until duplicate is removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[right])  # Safe to add now
            max_sub = max(max_sub, right - left + 1)
            right += 1
            
        return max_sub
                 

        