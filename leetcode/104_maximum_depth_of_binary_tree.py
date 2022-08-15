"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/



docs:
https://www.educative.io/answers/binary-trees-in-python


q: Tree Visualizer
https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/2268391/How-to-transform-list-to-a-tree-object


a:
https://stackoverflow.com/questions/58896039/how-do-i-make-treenode-from-list-by-python
LeetCode's help center:
https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation-


explanation:
https://www.youtube.com/watch?v=hTM3phVI6YQ
"""
from typing import Optional

# Definition for a binary tree node.
from leetcode.helpers.trees import deserialize


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    tree = deserialize("[3,9,20,null,null,15,7]")
    result = Solution().maxDepth(tree)
    assert result == 3, result
