from typing import Type


class Node:
    def __init__(
        self, data, left: Type["Node"] | None = None, right: Type["Node"] | None = None
    ):
        self.data = data
        self.left = left
        self.right = right


def is_identical(node1: Node, node2: Node):
    if node1 is None and node2 is None:
        return
    elif node1 is None or node2 is None:
        return False
    return (
        node1.data == node2.data
        and is_identical(node1.left, node2.left)
        and is_identical(node1.right, node2.right)
    )


if __name__ == "__main__":
    root1 = Node(
        1,
        Node(
            2,
        ),
        Node(
            5,
            Node(
                4,
                Node(5),
            ),
            Node(6),
        ),
    )
    root2 = Node(
        1,
        Node(
            2,
        ),
        Node(
            5,
            Node(
                4,
                Node(5),
            ),
            Node(6),
        ),
    )

    print(is_identical(root1, root2))
