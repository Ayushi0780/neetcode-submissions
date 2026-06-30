class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array

        for i in range(len(nums)):
            # If the first number is > 0, the remaining numbers will also be > 0.
            # They can never sum up to 0, so we can stop completely.
            if nums[i] > 0:
                break

            # Step 3: Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 4: Two-pointer approach for the remaining two numbers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Move pointers forward and backward
                    left += 1
                    right -= 1

                    # Skip duplicate values for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values for the third number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif three_sum < 0:
                    left += 1  # Sum is too small, need a larger number
                else:
                    right -= 1  # Sum is too big, need a smaller number

        return res