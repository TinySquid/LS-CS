class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        If a list contains a duplicate, return true, else false
        Using a set, we can compare lengths in O(1) time / O(n) space
        """
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
