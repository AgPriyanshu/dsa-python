import sys
from typing import Type


class TreeNode:
    def __init__(
        self,
        val,
        left: Type["TreeNode"] | None = None,
        right: Type["TreeNode"] | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


max_sum = -sys.maxsize


def max_sum_path(root: TreeNode):
    global max_sum
    if root is None:
        return 0

    left_sum = max(0, max_sum_path(root.left))
    right_sum = max(0, max_sum_path(root.right))
    max_sum = max(max_sum, left_sum + right_sum + root.val)

    return max(left_sum, right_sum) + root.val


if __name__ == "__main__":
    root1 = TreeNode(
        -10,
        TreeNode(
            9,
        ),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7),
        ),
    )
    print(max_sum_path(root1))
    print(max_sum)
