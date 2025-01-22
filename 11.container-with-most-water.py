import unittest

# Container With Most Water
# Category	Difficulty	Likes	Dislikes
# algorithms	Medium (56.84%)	30408	1908
# Tags
# Companies
# bloomberg

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
# Submissions | Solution

#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        m = 0

        j = len(height) - 1
        i = 0
        while i != j:
            m = max(m, (min(height[i], height[j]) * (j - i)))

            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j] or height[i] == height[j]:
                j -= 1

        return m
# @lc code=end



class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = [1,8,6,2,5,4,8,3,7]
        outp = sol.maxArea(inp)
        self.assertEqual(outp, 49)


        inp = [1,1]
        outp = sol.maxArea(inp)
        self.assertEqual(outp, 1)

if __name__ == '__main__':
    unittest.main()