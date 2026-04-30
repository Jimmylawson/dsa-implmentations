from node import TreeNode
from traversals import *
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

    # print(f"Search item {bst.search(5)}")
    #
    # print(f"Depth of the tree is: {bst.maxDepth(bst.root)}")
    # print(f"Minimum value in the tree is: {bst.findMin()}")
    # print(f"Maximum value in the tree is: {bst.findMax()}")
    bst.removeNode(bst.root, 5)
    preorder_traversal(bst.root)
    # inorder_traversal(bst.root)
    # print()
    # post_order_traversal(bst.root)
    # print()
    # preorder_traversal(bst.root)
