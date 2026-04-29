class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, val in enumerate(nums):
            diff = target - nums[i]
            if diff in prev:
                return [prev[diff], i]
            prev[val] = i

        

        