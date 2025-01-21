import unittest

# Is Subsequence
# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (48.16%)	10018	564
# Tags
# Companies
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
# Submissions | Solution

#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        if len(s) == 0:
            return True

        if len(t) == 0:
            return False

        if s == t:
            return True

        j = 0
        for i in range(len(t)):
          if t[i] == s[j]:
            j += 1
          if j == len(s):
              return True

        return False
                
        
# @lc code=end


class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = 'abc', 'ahbgdc'
        out = sol.isSubsequence(*inp)
        self.assertEqual(out, True)

        inp = 'axc', 'ahbgdc'
        out = sol.isSubsequence(*inp)
        self.assertEqual(out, False)
        

if __name__ == '__main__':
    unittest.main()