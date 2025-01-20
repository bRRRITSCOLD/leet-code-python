import unittest
#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k: 
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base 
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""
        


            
            
          
            
# @lc code=end

class TestRoot(unittest.TestCase):

    def test(self):
        sol =  Solution()
        self.assertEqual(sol.gcdOfStrings('ABCABC', 'ABC'), 'ABC')
        self.assertEqual(sol.gcdOfStrings('ABABAB', 'ABAB'), 'AB')
        self.assertEqual(sol.gcdOfStrings('LEET', 'CODE'), '')

if __name__ == '__main__':
    unittest.main()