import unittest

# Search Insert Position
# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (47.99%)	16917	793
# Tags
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
# Submissions | Solution

#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = len(nums)
        left = 0
        right = l - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
# @lc code=end

class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        # inp = [1,3,5,6], 5
        # outp = sol.searchInsert(*inp)
        # self.assertEqual(outp, 2)

        inp = [1,3,5,6], 7
        outp = sol.searchInsert(*inp)
        self.assertEqual(outp, 4)

if __name__ == '__main__':
    unittest.main()