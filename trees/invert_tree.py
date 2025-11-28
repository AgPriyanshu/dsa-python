from collections import deque
from typing import Optional, Type


class Node:
    def __init__(
        self, data, left: Type["Node"] | None = None, right: Type["Node"] | None = None
    ):
        self.data = data
        self.left = left
        self.right = right


def invertTreeLevelOrder(root: Optional[Node]) -> Optional[Node]:
    q = deque()

    if not root:
        return

    root2 = Node(root.val)
    q.append(
        (
            root,
            root2,
        )
    )
    while q:
        n = len(q)
        for i in range(n):
            node, node2 = q.popleft()

            if node.left:
                node2.right = Node(node.left.val)
                q.append(
                    (
                        node.left,
                        node2.right,
                    )
                )
            if node.right:
                node2.left = Node(node.right.val)
                q.append(
                    (
                        node.right,
                        node2.left,
                    )
                )
    return root2


def invertTree(self, root: Optional[Node]) -> Optional[Node]:
    if not root:
        return

    temp = root.left
    root.left = root.right
    root.right = temp

    self.invertTree(root.left)
    self.invertTree(root.right)

    return root


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
