class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        start=0
        max_length=0
        for end in range(len(s)):
            current_char=s[end]

            if current_char in seen and seen[current_char]>=start:
                start=seen[current_char]+1

            seen[current_char]=end

            current_win=end-start+1
            max_length=max(current_win,max_length) 
        return max_length       


        