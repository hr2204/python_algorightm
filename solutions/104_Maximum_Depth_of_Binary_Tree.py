# 104. Maximum Depth of Binary Tree
# Difficulty: Easy
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        depth = 0
        if not root:
            return depth
        else:
            return self.helper(root,depth)

    def helper(self,node,depth):
        depth += 1
        if not node.left and not node.right:
            return depth
        if node.left and node.right:
            return max(self.helper(node.left,depth),self.helper(node.right,depth))
        if node.left:
            return self.helper(node.left,depth)
        if node.right:
            return self.helper(node.right,depth)





if __name__ == '__main__':
    root = build_tree([1,3,4,4])
    printTree(root)
    print Solution().maxDepth(root)