# Question 1
def is_full(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return is_full(root.left) and is_full(root.right)
    return False

# Question 2
def num_nodes(root):
    if root is None:
        return 0
    return 1 + num_nodes(root.left) + num_nodes(root.right)

# Question 3
def num_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return num_leaves(root.left) + num_leaves(root.right)

# Question 4
def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))

# Question 5
def is_perfect(root):
    return num_nodes(root) == 2 ** (height(root) + 1) - 1

# Question 6
def has_value_bst(root, val):
    if root is None:
        return False
    if root.val == val:
        return True
    elif val < root.val:
        return has_value_bst(root.left, val)
    else:
        return has_value_bst(root.right, val)
