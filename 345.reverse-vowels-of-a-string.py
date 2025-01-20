import unittest

# Reverse Vowels of a String
# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (56.22%)	4815	2820
# Tags
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.
# Submissions | Solution

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        r = list(s)
        i = 0
        j = len(r) - 1
        while i < j:
            ri = r[i]
            rj = r[j]
            while 
            if ri.lower() not in vowels:
                i += 1
            if rj.lower() not in vowels:
                j -= 1
            if ri.lower() in vowels and rj.lower() in vowels:
                r[i] = rj
                r[j] = ri
                i += 1
                j -= 1

        return ''.join(r)
        

# @lc code=end


class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()
        self.assertEqual(sol.reverseVowels("leetcode"), "leotcede")
        self.assertEqual(sol.reverseVowels("IceCreAm"), "AceCreIm")

if __name__ == '__main__':
    unittest.main()