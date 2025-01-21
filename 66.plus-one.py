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
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
              digits[i] = 0
            else:
                digits[i] += 1
                return digits

        return [1] + digits
# @lc code=end

class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = [1,2,3]
        outp = sol.plusOne(inp)
        self.assertEqual(outp, [1,2,4])


        inp = [9, 9, 9, 9, 9]
        outp = sol.plusOne(inp)
        self.assertEqual(outp, [1, 0, 0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()