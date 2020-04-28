"""
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,

    return [0, 1].
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Using a dict where key -> list value, value -> list index
        
        2 steps
        build the dict using the list,
        calculate the target key by subtracting target with the next list value
        if the target key is in the dict, return it, and the list index + 1
        """

        num_table = {}
        for i in range(0, len(nums) - 1):
            num_table[nums[i]] = i
            target_key = target - nums[i + 1]

            if target_key in num_table:
                return [num_table[target_key], i + 1]
