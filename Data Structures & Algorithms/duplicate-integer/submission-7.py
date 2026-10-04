class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # seen={}
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen[i]=True
        # return False        
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)  
        return False
        ### T.C=O(n)
            #S.C=O(n)      