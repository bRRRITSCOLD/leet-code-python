import unittest

# Max Number of K-Sum Pairs
# Category	Difficulty	Likes	Dislikes
# algorithms	Medium (55.65%)	3286	101
# Tags
# Companies
# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109
# Submissions | Solution

#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        ops = 0
        d = {}
        for i in range(len(nums)):
            diff = k - nums[i]
            if diff in d and d[diff] > 0:
                d[diff] -= 1
                ops += 1
            else:
                d[nums[i]] = (d[nums[i]] if nums[i] in d else 0) + 1
        return ops
                
                

# @lc code=end




class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = [1,2,3,4], 5
        outp = sol.maxOperations(*inp)
        self.assertEqual(outp, 2)


        inp = [3,1,3,4,3], 6
        outp = sol.maxOperations(*inp)
        self.assertEqual(outp, 1)

if __name__ == '__main__':
    unittest.main()