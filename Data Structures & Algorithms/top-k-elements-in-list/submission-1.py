class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
            sorted_key=sorted(count.keys(),key=lambda x:count[x] ,reverse=True)
        return sorted_key[:k]
