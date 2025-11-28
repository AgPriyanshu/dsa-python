# Problem Statement: Given the Postorder and Inorder traversal of a Binary Tree, construct the Unique Binary Tree represented by them.
from typing import List, Type


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


def prepare(inorder: List, postorder: List) -> TreeNode:
    if len(inorder) != len(postorder):
        return None
    inorder_map = {val: i for i, val in enumerate(inorder)}

    return buildTree(0, len(inorder) - 1, inorder_map, 0, len(postorder) - 1, postorder)


def buildTree(is_, ie, inorder_map, ps, pe, postorder):
    if ps > pe or is_ > ie:
        return None

    root = TreeNode(postorder[pe])
    inorder_root_index = inorder_map[postorder[pe]]
    nums_elements = inorder_root_index - is_
    # import pdb

    # pdb.set_trace()
    # print(
    #     f"is_:{is_},ie:{ie},inorder_root_index:{inorder_root_index},ps:{ps},pe:{pe},postorder:{postorder}"
    # )

    root.left = buildTree(
        is_, inorder_root_index - 1, inorder_map, ps, ps + nums_elements - 1, postorder
    )
    root.right = buildTree(
        inorder_root_index + 1,
        ie,
        inorder_map,
        ps + nums_elements,
        pe - 1,
        postorder,
    )

    return root


def inorder(node: TreeNode):
    if node is None:
        return

    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)


if __name__ == "__main__":
    inorder(prepare([40, 20, 50, 10, 60, 30], [40, 50, 20, 60, 30, 10]))
