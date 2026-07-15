class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        my_set = set()
        for num in nums:
            if num not in my_set:
                my_set.add(num)
        return len(nums) != len(my_set)
         