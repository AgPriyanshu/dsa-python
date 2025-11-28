from collections import deque
from typing import Optional, Type


class Node:
    def __init__(
        self, data, left: Type["Node"] | None = None, right: Type["Node"] | None = None
    ):
        self.data = data
        self.left = left
        self.right = right


def is_symmetric(node1: Node, node2: Node):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    return (
        node1.data == node2.data
        and is_symmetric(node1.left, node2.right)
        and is_symmetric(node1.right, node2.left)
    )


if __name__ == "__main__":
    root1 = Node(
        1,
        Node(
            2,
            Node(
                6,
                Node(5),
                Node(7),
            ),
            Node(4),
        ),
        Node(
            2,
            Node(4),
            Node(
                6,
                Node(7),
                Node(5),
            ),
        ),
    )

    print(is_symmetric(root1.left, root1.right))
