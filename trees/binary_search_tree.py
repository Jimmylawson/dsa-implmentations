"""Binary search tree implementation."""
from node import TreeNode


class BinarySearchTree:
    def __init__(self,root:TreeNode| None = None) -> None:
        self.root = root

    def insert(self,value:int) -> None:
        current = self.root
        if not current:
            current = TreeNode(value)
            self.root = current
            return

        while current:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right
            else:
                return

    def search(self, value: int):
        current = self.root

        if not current: return None

        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current.value

        return None

    def findMin(self):
        current = self.root

        if not current: return None

        while current.left:
            current = current.left
        return current.value

    def findMax(self):
        current = self.root
        if not current: return None

        while current.right:
            current = current.right
        return current.value

    def maxDepth(self,root):
        if not root: return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1











