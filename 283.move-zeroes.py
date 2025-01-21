import unittest

# Move Zeroes
# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (62.40%)	17411	500
# Tags
# Companies
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?
# Submissions | Solution

#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l = len(nums)

        if l == 1:
            return nums
        
        w = 0
        for r in range(l):
            if nums[r] != 0:
                nums[w] = nums[r]
                w += 1
        
        while w < l:
          nums[w] = 0
          w += 1
              
        
        return 
                
        
# @lc code=end


class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = [0,1,0,3,12]
        sol.moveZeroes(inp)
        self.assertEqual(inp, [1,3,12,0,0])


        inp = [0]
        sol.moveZeroes(inp)
        self.assertEqual(inp, [0])

        inp = [0,1]
        sol.moveZeroes(inp)
        self.assertEqual(inp, [1,0])

        inp = [4,2,4,0,0,3,0,5,1,0]
        sol.moveZeroes(inp)
        self.assertEqual(inp, [4,2,4,3,5,1,0,0,0,0])
        

if __name__ == '__main__':
    unittest.main()