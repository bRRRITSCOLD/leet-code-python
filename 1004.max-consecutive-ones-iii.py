import unittest

# Max Consecutive Ones III
# Category	Difficulty	Likes	Dislikes
# algorithms	Medium (64.88%)	9092	154
# Tags
# Companies
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
# Submissions | Solution

#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]

            if k < 0:
                k += 1 - nums[left]
                left += 1

        return right - left + 1
# @lc code=end


class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = [1,1,1,0,0,0,1,1,1,1,0], 2
        outp = sol.longestOnes(*inp)
        self.assertEqual(outp, 6)

        inp = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3
        outp = sol.longestOnes(*inp)
        self.assertEqual(outp, 10)

if __name__ == '__main__':
    unittest.main()