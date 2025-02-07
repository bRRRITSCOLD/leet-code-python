import unittest

# Increasing Triplet Subsequence
# Category	Difficulty	Likes	Dislikes
# algorithms	Medium (39.22%)	8357	604
# Tags
# Companies
# facebook

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

# Constraints:

# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
# Submissions | Solution

#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        f = float("inf")
        s = float("inf")
        for n in nums:
          if n <= f:
              f = n
          elif n <= s:
              s = n
          else:
              return True
        return False
# @lc code=end




class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()
        self.assertEqual(sol.increasingTriplet([1,2,3,4,5]), True)
        self.assertEqual(sol.increasingTriplet([5,4,3,2,1]), False)
        self.assertEqual(sol.increasingTriplet([2,1,5,0,4,6]), True)

if __name__ == '__main__':
    unittest.main()