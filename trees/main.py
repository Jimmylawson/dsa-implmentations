from node import TreeNode
from traversals import *
from binary_search_tree import BinarySearchTree
import tree_problems
from tree_problems import TreeProblems


def build_sample_tree():
    bst_2 = BinarySearchTree()
    bst_2.insert(10)
    bst_2.insert(5)
    bst_2.insert(15)


    return bst_2.root




if __name__ == "__main__":
    bst = BinarySearchTree()
    # bst.insert(10)
    # bst.insert(5)
    # bst.insert(15)
    # bst.insert(3)
    # bst.insert(7)
    # bst.insert(12)
    # bst.insert(18)
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    # print(f"Search item {bst.search(5)}")
    #
    # print(f"Depth of the tree is: {bst.maxDepth(bst.root)}")
    # print(f"Minimum value in the tree is: {bst.findMin()}")
    # print(f"Maximum value in the tree is: {bst.findMax()}")
    # bst.removeNode(bst.root, 5)
    # inorder_traversal(bst.root)
    # problem = TreeProblems()
    # print(type(problem))
    # print(problem.is_same_tree(bst.root, build_sample_tree()))
    # inorder_traversal(bst.root)
    # print()
    # post_order_traversal(bst.root)
    # print()
    # preorder_traversal(bst.root)
    res = bst.rightSideViewDFS(bst.root)
    print(res)
