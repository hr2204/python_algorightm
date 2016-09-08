# 236. Lowest Common Ancestor of a Binary Tree
# Difficulty: Medium
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
# two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a
# node to be a descendant of itself).”
#
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5,
# since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val<root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val>root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == root:
            return p
        if q == root:
            return q
        if self.isContainNode(root.left,p) and self.isContainNode(root.right,q):
            return root
        if self.isContainNode(root.right,p) and self.isContainNode(root.left,q):
            return root
        if self.isContainNode(root.left,p) and self.isContainNode(root.left,q):
            return self.lowestCommonAncestor(root.left,p,q)
        if self.isContainNode(root.right,p) and self.isContainNode(root.right,q):
            return self.lowestCommonAncestor(root.right,p,q)

    def isContainNode(self,root,node):
        if not root:
            return False
        if root == node:
            return True
        else:
            return self.isContainNode(root.left,node) or self.isContainNode(root.right,node)

if __name__ == '__main__':
    root = build_tree([6,2,8,0,4,7,9,"",3,5])
    printTree(root)
    k = TreeNode(2)
    # print Solution().isContainNode(root,k)

    p = root.left.left #2
    q = root.left.right.left #3

    print Solution().lowestCommonAncestor(root,p,q).val