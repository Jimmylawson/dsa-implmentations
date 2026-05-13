"""Practice problems built on tree concepts."""
from node import TreeNode

class TreeProblems:
    def __init__(self,root:TreeNode|None = None)->None:
        self.root = root

    def max_depth(self,root)->int:
        if not root:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        return max(left_depth, right_depth) + 1
#is_same_tree means: do
# two trees have the exact same structure and the exact same values in matching
    def is_same_tree(self, p, q):
        if not p and not q:
         return True
        if not p or not  q:
            return False
        return p.value == q.value and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
    