"""
origin:
https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation-

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/396124/Python-very-easy-to-understand-recursive-preorder-with-comments
https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
"""
from typing import Union, Optional, List

NONE_VALUE = "null"


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


# def deserialize(string):
#     if string == '[]':
#         return None
#     nodes = [None if val == NONE_VALUE else TreeNode(int(val))
#              for val in string.strip('[]').split(',')]
#     kids = nodes[::-1]
#     root = kids.pop()
#     for node in nodes:
#         if node:
#             if kids:
#                 node.left = kids.pop()
#             if kids:
#                 node.right = kids.pop()
#     return root

def serialize_pre_order(root):
    """
    pre-order traversal algorithm to serialize
    """
    def serialize_pre_order_internal(root_inner):
        if root_inner is None:
            return NONE_VALUE
        root_val = root_inner.val
        left_val = serialize_pre_order_internal(root_inner.left)
        right_val = serialize_pre_order_internal(root_inner.right)
        # return root_val, left_val, right_val
        return ','.join([str(root_val), left_val, right_val])
    result = serialize_pre_order_internal(root)
    return f"[{result}]"


    # tree_list = []
    # tree_list.append(tree.val)
    # if tree.left:
    #     tree_list.extend(serialize(tree.left))
    # # else:
    # #     tree_list.append(None)
    # if tree.right:
    #     tree_list.extend(serialize(tree.right))
    # # else:
    # #     tree_list.append(None)
    # return tree_list


def deserialize_nodes(string: str):
    # nodes = [None if val == NONE_VALUE else TreeNode(int(val)) for val in string.split(',')]
    for raw_val in string.strip('[]').split(','):
        if raw_val == NONE_VALUE:
            val = None
        else:
            val = TreeNode(int(raw_val))

        yield val
    # return nodes


# [TreeNode(3), TreeNode(9), None, None, TreeNode(20), TreeNode(15), None, None, TreeNode(7), None, None]
def deserialize_pre_order_old(sequence):
    try:
        root = next(sequence)
    except StopIteration:
        return None
    # root
    if root is None:
        return None
    root.left = deserialize_pre_order(sequence)
    root.right = deserialize_pre_order(sequence)
    return root


def deserialize_pre_order(data: str):
    sequence = (None if val == NONE_VALUE else TreeNode(int(val)) for val in data.strip('[]').split(','))

    def deserialize_pre_order_inner(nodes):
        try:
            root = next(nodes)
        except StopIteration:
            return None
        if root is None:
            return None
        root.left = deserialize_pre_order_inner(nodes)
        root.right = deserialize_pre_order_inner(nodes)
        return root

    return deserialize_pre_order_inner(sequence)


# string = string.strip('[]')
# if not string:
#     return None

# nodes = [None if val == NONE_VALUE else TreeNode(int(val)) for val in string.strip('[]').split(',')]

# nodes
# kids = nodes[::-1]
# root = kids.pop()
# for node in nodes:
#     if node:
#         if kids:
#             node.left = kids.pop()
#         if kids:
#             node.right = kids.pop()
# return root


def is_identical(a, b) -> bool:
    # 1. both is None
    if a is None and b is None:
        return True

    # 2. only one is None
    if a is None or b is None:
        return False

    # 3. both is not None
    root_is_identical = a.val == b.val
    left_is_identical = is_identical(a.left, b.left)
    right_is_identical = is_identical(a.right, b.right)
    return root_is_identical and left_is_identical and right_is_identical


if __name__ == '__main__':
    # assert is_identical(
    #     deserialize('[3,9,20,null,null,15,7]'),
    #     TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15), TreeNode(7))),
    # )
    # assert is_identical(
    #     TreeNode(3),
    #     TreeNode(3),
    # )

    # tree: TreeNode = TreeNode(3)
    # tree_origin --> tree_serialized
    # tree_origin: TreeNode = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))

    tree_serialized_origin = "[3,9,null,null,20,15,null,null,7,null,null]"
    tree_origin: TreeNode = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    tree_serialized = serialize_pre_order(tree_origin)
    assert tree_serialized_origin == tree_serialized
    print('tree_serialized', tree_serialized)
    # tree_serialized = "3,9,null,null,20,15,null,null,7,null,null"
    # tree_serialized = "3,9,#,#,20,15,#,#,7,#,#"

    # tree_serialized = f"[{tree_serialized}]"
    # nodes_deserialized = deserialize_nodes(tree_serialized_origin)
    # tree_deserialized = deserialize_pre_order_old(nodes_deserialized)
    tree_deserialized = deserialize_pre_order(tree_serialized_origin)
    print('tee_deserialized', tree_deserialized)
    assert is_identical(tree_origin, tree_deserialized)
