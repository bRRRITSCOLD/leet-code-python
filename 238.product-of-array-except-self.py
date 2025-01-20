import unittest

# Product of Array Except Self
# Category	Difficulty	Likes	Dislikes
# algorithms	Medium (67.20%)	23509	1494
# Tags
# Companies
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Submissions | Solution

#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        l = [0] * length
        r = [0] * length
        a = [0] * length
        
        l[0] = 1
        for i in range(1, len(nums)):
            l[i] = l[i - 1] * nums[i - 1]
        
        r[length - 1] = 1
        for i in reversed(range(length - 1)):
            r[i] = r[i + 1] * nums[i + 1]
          
        for i in range(length):
            a[i] = l[i] * r[i]

        return a

        
# @lc code=end

class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()
        self.assertEqual(sol.productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(sol.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])

if __name__ == '__main__':
    unittest.main()