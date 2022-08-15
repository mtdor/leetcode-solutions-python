NONE_VALUE = "null"


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
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

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

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


if __name__ == '__main__':
    data_origin: str = "[1,2,3,null,null,4,5]"
    root_node = Codec().deserialize(data_origin)
    print('root_node', root_node)
    data_serialized = Codec().serialize(root_node)
    print("data_serialized", data_serialized)
    # ser = Codec()
    # deser = Codec()
    # ans = deser.deserialize(ser.serialize(root))
    # ans
