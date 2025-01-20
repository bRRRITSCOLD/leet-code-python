import unittest
#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # final = []
        # len1 = len(word1)
        # len2 = len(word2)
        # i = 0
        # j = 0
        # while ((i if len1 > len2 else j) < (len1 if len1 > len2 else len2)):
        #   if i < len1:
        #     final.append(word1[i])
        #     i = i + 1
        #   if j < len2:
        #     final.append(word2[j])
        #     j = j + 1
        # return ''.join(final)
        final = ''
        n = min(len(word1),len(word2))
        for i in range(n):
            final += word1[i]
            final += word2[i]
        final += word1[n:]
        final += word2[n:]
        return final

            
            
          
            
# @lc code=end

class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()
        self.assertEqual(sol.mergeAlternately('abc', 'pqrst'), 'apbqcrst')

if __name__ == '__main__':
    unittest.main()