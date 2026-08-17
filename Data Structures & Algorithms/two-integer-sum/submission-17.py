class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            # 
            # for i in range(0,len(nums)):
            #     for j in range(0,i):
            #         if nums[i]+nums[j]==target:
            #             return [j,i]

            seen={}
            for i , n in enumerate(nums):
                comp=target-n
                if comp  in seen:
                    return[seen[comp],i]
                seen[n]=i
            return[]        