# 368. Largest Divisible Subset
# Difficulty: Medium
# Contributor: LeetCode
# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements
#  in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        for num in nums:
            res.append([num])




if __name__ == '__main__':
    ipnut = [1,2,3]
    print Solution().largestDivisibleSubset(input)