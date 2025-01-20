import unittest

# Reverse Words in a String
# Category	Difficulty	Likes	Dislikes
# algorithms	Medium (48.93%)	9044	5301
# Tags
# Companies
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

# Submissions | Solution

class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        r = []
        for i in range(len(split)):
            r.insert(0, split[i])
        return ' '.join(r)

        
        

# @lc code=end


class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()
        self.assertEqual(sol.reverseWords("blue is sky the"), "the sky is blue")
        self.assertEqual(sol.reverseWords("  hello world  "), "world hello")
        self.assertEqual(sol.reverseWords("a good   example"), "example good a")

if __name__ == '__main__':
    unittest.main()