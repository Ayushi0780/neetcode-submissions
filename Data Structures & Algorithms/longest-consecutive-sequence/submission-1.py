class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak=0
        num=set(nums)
        for s in num:
            if (s-1) not in num:
                current=s
                curr_streak=1

                while (current+1) in num:
                    current+=1
                    curr_streak+=1

                longest_streak=max(longest_streak,curr_streak)
        return longest_streak            

                

        