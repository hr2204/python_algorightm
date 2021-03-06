# 389. Find the Difference
# Difficulty: Easy
# Contributors: Admin
# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s and then add one more letter at a random position.
#
# Find the letter that was added in t.
#
# Example:
#
# Input:
# s = "abcd"
# t = "abcde"
#
# Output:
# e
#
# Explanation:
# 'e' is the letter that was added.

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_sum, t_sum = 0, 0
        for char in s:
            s_sum += (ord(char)- 97)
        for char in t:
            t_sum += (ord(char)- 97)

        return chr(t_sum - s_sum + 97)
if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    print Solution().findTheDifference(s,t)