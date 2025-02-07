# Can Place Flowers
# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (28.83%)	6836	1235
# Tags
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
# Submissions | Solution

# 
#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
import unittest


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        k = 0
        for i in range(len(flowerbed)):
            prev = 0 if i == 0 else flowerbed[i - 1]
            curr = flowerbed[i]
            nex = 0 if i == (len(flowerbed) - 1) else flowerbed[i + 1]
            if prev == 0 and curr == 0 and nex == 0:
                flowerbed[i] = 1
                k += 1
                if k >= n:
                    return True
        return k >= n
        
# @lc code=end


class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()
        self.assertEqual(sol.canPlaceFlowers([1,0,0,0,1], 1), True)
        self.assertEqual(sol.canPlaceFlowers([1,0,0,0,1], 2), False)
        self.assertEqual(sol.canPlaceFlowers([1,0,0,0,0,1], 2), False)
        self.assertEqual(sol.canPlaceFlowers([0,0,1,0,1], 1), True)

if __name__ == '__main__':
    unittest.main()