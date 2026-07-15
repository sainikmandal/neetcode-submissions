class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):  # Start j from i + 1 to avoid duplicates and redundant checks
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # Return an empty list if no solution is found
