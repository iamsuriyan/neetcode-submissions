class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set(nums)
        if len(duplicate) != len(nums):
            return True
        return False 