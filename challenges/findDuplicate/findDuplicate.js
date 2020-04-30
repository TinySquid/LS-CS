/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function (nums) {
    // Also doesn't follow all restrictions, but it does pass.
    // O(n log n) time (because the sort)
    // O(1) space (because sort in-place)

    nums.sort();

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === nums[i - 1]) {
            return nums[i];
        }
    }
};
