from collections import deque
from typing import Optional, Type


class Node:
    def __init__(
        self, data, left: Type["Node"] | None = None, right: Type["Node"] | None = None
    ):
        self.data = data
        self.left = left
        self.right = right


def is_identical(node1: Node, node2: Node):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    return (
        node1.data == node2.data
        and is_identical(node1.left, node2.left)
        and is_identical(node1.right, node2.right)
    )


def subtree_of_another_tree(node1: Node, node2: Node):
    if node2 is None:
        return True
    if node1 is None:
        return False

    if is_identical(node1, node2):
        return True

    return subtree_of_another_tree(node1.left, node2) or subtree_of_another_tree(
        node1.right, node2
    )
