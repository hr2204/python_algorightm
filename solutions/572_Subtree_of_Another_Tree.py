# 572. Subtree of Another Tree
# Difficulty: Easy
# Contributors:
# xljob
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values
# with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.
# Subscribe to see which companies asked this question.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if not s and t:
            return False

        if s and not t:
            return False

        if not s and not t:
            return True

        if s.val == t.val:
            return self.isSubtree(s.left,t.left) and self.isSubtree(s.right,t.right)

        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)


