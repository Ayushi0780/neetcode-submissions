class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while(left<right):
            currr= numbers[left]+numbers[right]
            if target==currr:
                return [left +1,right+1]
            if target>currr:
                left+=1
            else:
                right=right-1        
        