"""Core tree node definitions."""
from __future__ import annotations


class TreeNode:
    def __init__(self, value:int):
        self.value:int  = value
        self.left:TreeNode | None = None
        self.right: TreeNode | None = None


