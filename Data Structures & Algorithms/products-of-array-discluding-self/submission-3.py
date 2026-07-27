class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [1] * n
        
       
        # prefix = 1
        # for i in range(n):
        #     res[i] = prefix
        #     prefix *= nums[i]
            
      
        # suffix = 1
        # for i in range(n - 1, -1, -1):
        #     res[i] *= suffix
        #     suffix *= nums[i]
            
        # return res
        n=len(nums)
        left,right,result=[1]*n,[1]*n,[1]*n

        ### loop for left side
        for i in range(1,n):
            left[i]=left[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            right[i]=right[i+1]*nums[i+1] 

        for i in range(n):
            result[i]=left[i]*right[i]   
        return result             


    