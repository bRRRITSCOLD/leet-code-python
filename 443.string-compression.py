import unittest

# String Compression
# Category	Difficulty	Likes	Dislikes
# algorithms	Medium (56.82%)	5414	8291
# Tags
# Companies
# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

 

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

# Constraints:

# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
# Submissions | Solution

#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars) and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        chars[:len(chars)] =  chars[:res]
        return res
        
# @lc code=end






class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()

        input_1 = ["a","a","b","b","c","c","c"]
        output_1 = sol.compress(input_1)
        self.assertEqual(output_1, 6)
        self.assertEqual(input_1, ["a","2","b","2","c","3"])
        
        input_2 = ["a"]
        output_2 = sol.compress(input_2)
        self.assertEqual(output_2, 1)
        self.assertEqual(input_2, ["a"])

        input_3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        output_3 = sol.compress(input_3)
        self.assertEqual(output_3, 4)
        self.assertEqual(input_3, ["a","b","1","2"])

        input_4 = ["a","a","a","b","b","a","a"]
        output_4 = sol.compress(input_4)
        self.assertEqual(output_4, 6)
        self.assertEqual(input_4, ["a","3","b","2", "a", "2"])

if __name__ == '__main__':
    unittest.main()