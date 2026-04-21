"""Tree traversal algorithms."""


def inorder_traversal(root):
    if not root:
        return

    inorder_traversal(root.left)
    print(f"{root.value} ->",end="")
    inorder_traversal(root.right)

def preorder_traversal(root):
    if not root:
        return

    print(f"{root.value} ->", end="")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def post_order_traversal(root):
    if not root: return

    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(f"{root.value} ->", end="")

# def level_order_traversal(root):
#     if not root: return
#
#     print(f"{root.value} ->", end="")
#     if root.left and root.right:
#         print(f"{root.left.value} ->", end="")
#         print(f"{root.right.value} ->", end="")
#     level_order_traversal(root.left)
#     level_order_traversal(root.right)


