"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            result.append(root.val)
            traverse(root.right)

        traverse(root)

        return result


if __name__ == '__main__':
    Solution().inorderTraversal()
