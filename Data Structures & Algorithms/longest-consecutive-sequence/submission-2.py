class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak=0
        num=set(nums)
        for  i in num:
            if  (i-1) not in num:
                curr=i
                curr_streak=1
                while (curr+1) in num:
                    curr+=1
                    curr_streak+=1
                
                longest_streak=max(longest_streak,curr_streak)

        return longest_streak            

        