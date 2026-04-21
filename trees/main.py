from node import TreeNode
from traversals import (inorder_traversal,
                        preorder_traversal, post_order_traversal, level_order_traversal)

def build_sample_tree() -> TreeNode:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)

    return root






if __name__ == "__main__":
    root = build_sample_tree()
    level_order_traversal(root)
