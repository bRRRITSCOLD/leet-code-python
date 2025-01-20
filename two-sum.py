import unittest
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
        
# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      d = {}
      for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        if diff in d:
           return [d[diff], i]
        else:
           d[num] = i

      return False
          
      
        
# @lc code=end


class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()
        self.assertEqual(sol.twoSum([3,2,4], 6), [1,2])

if __name__ == '__main__':
    unittest.main()