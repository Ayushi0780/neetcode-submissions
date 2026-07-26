class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a=set(nums)
        # if len(a)!=len(nums):
        #     return True
        # else:
        #     return False
        seen={}
        for i in nums:
            if i in seen:
                return True
            seen[i]=True
        return False        