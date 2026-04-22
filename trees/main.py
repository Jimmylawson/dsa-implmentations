from node import TreeNode
from traversals import (inorder_traversal,
                        preorder_traversal, post_order_traversal)
from binary_search_tree import BinarySearchTree

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
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)

    # print(bst.search(20))
    print(bst.maxDepth(bst.root))

    # inorder_traversal(bst.root)
