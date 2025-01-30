import unittest

# Longest Subarray of 1’s After Deleting One Element
# Category	Difficulty	Likes	Dislikes
# algorithms	Medium (68.50%)	4125	88
# Tags
# Companies
# Unknown

# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# Submissions | Solution

#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        longest = 0
        count = 0
        for right in range(len(nums)):
            count += int(nums[right] == 0)

            while count > 1:
                count -= int(nums[left] == 0)
                left += 1

            longest = max(longest, right - left)

        return longest
# @lc code=end


class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = [1,1,0,1]
        outp = sol.longestSubarray(inp)
        self.assertEqual(outp, 3)

        inp = [0,1,1,1,0,1,1,0,1]
        outp = sol.longestSubarray(inp)
        self.assertEqual(outp, 5)

        inp = [1,1,1]
        outp = sol.longestSubarray(inp)
        self.assertEqual(outp, 2)

if __name__ == '__main__':
    unittest.main()