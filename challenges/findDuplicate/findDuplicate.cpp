#include <algorithm>

/*
    Solution in O(1) space | O(n log n) time
    Sort is in place (breaks read-only input restriction)
    
    
    Sort array so that the duplicate number will occur in the next index
    Walk array testing current with prev element to find duplicate
    Return duplicate
*/

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        
        int prev = 0;

        // Walk vector and compare current iterator value with previous
        for(int i: nums){
            if (i == prev){
                return i;
            } else {
                // Move prev up
                prev = i;
            }
        }
        
        return 0;
    }
};