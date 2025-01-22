import unittest

# Majority Element
# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (65.42%)	20245	697
# Tags
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?
# Submissions | Solution

#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
                
                

# @lc code=end




class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = [3,2,3]
        outp = sol.majorityElement(inp)
        self.assertEqual(outp, 3)


        inp = [2,2,1,1,1,2,2]
        outp = sol.majorityElement(inp)
        self.assertEqual(outp, 2)

if __name__ == '__main__':
    unittest.main()