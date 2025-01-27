import unittest

# Maximum Number of Vowels in a Substring of Given Length
# Category	Difficulty	Likes	Dislikes
# algorithms	Medium (59.56%)	3614	138
# Tags
# Companies
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length
# Submissions | Solution

#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        length = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)

        maxsum = count
        
        for i in range(k, length, +1):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            maxsum = max(maxsum, count)

        return maxsum
# @lc code=end





class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        inp = 'abciiidef', 3
        outp = sol.maxVowels(*inp)
        self.assertEqual(outp, 3)

if __name__ == '__main__':
    unittest.main()