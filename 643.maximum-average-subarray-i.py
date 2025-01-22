import unittest

# Maximum Average Subarray I
# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (44.39%)	3717	345
# Tags
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104
# Submissions | Solution

#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = maxsum = sum(nums[:k])
        for i in range(k, len(nums), +1):
            curr += nums[i] - nums[i - k]
            if curr > maxsum:
                maxsum = curr
        return maxsum / k
# @lc code=end





class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = [1,12,-5,-6,50,3], 4
        outp = sol.findMaxAverage(*inp)
        self.assertEqual(outp, 12.75000)


        inp = [5], 1
        outp = sol.findMaxAverage(*inp)
        self.assertEqual(outp, 5)

if __name__ == '__main__':
    unittest.main()