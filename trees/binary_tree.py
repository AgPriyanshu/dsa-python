from typing import Type
from enum import Enum
from collections import deque


class TraversalType(Enum):
    INORDER = "inorder"
    PREORDER = "preorder"
    POSTORDER = "postorder"
    LEVELORDER = "leverorder"


class Node:
    def __init__(
        self, data, left: Type["Node"] | None = None, right: Type["Node"] | None = None
    ):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root: Node | None = None):
        self.root = root

    def traverse(self, traversal_type: TraversalType = TraversalType.INORDER):
        if traversal_type == TraversalType.INORDER:
            print("Inorder:", end=" ")
            self.__inorder(self.root)
        elif traversal_type == TraversalType.PREORDER:
            print("Preorder:", end=" ")
            self.__preorder(self.root)
        elif traversal_type == TraversalType.PREORDER:
            print("Postorder:", end=" ")
            self.__postorder(self.root)
        else:
            print(f"Levelorder:{self.__levelorder(self.root)}", end=" ")

    def __inorder(self, node: Node):
        if node is None:
            return

        self.__inorder(node.left)
        print(node.data, end=" ")
        self.__inorder(node.right)

    def __postorder(self, node: Node):
        if node is None:
            return

        self.__postorder(node.left)
        self.__postorder(node.right)
        print(node.data, end=" ")

    def __preorder(self, node: Node):
        if node is None:
            return

        print(node.data, end=" ")
        self.__preorder(node.left)
        self.__preorder(node.right)

    def __levelorder(self, node: Node):
        result = []
        if not node:
            return result
        queue = deque()
        queue.append(node)
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                pop_node = queue.popleft()
                level.append(pop_node.data)
                if pop_node.left:
                    queue.append(pop_node.left)
                if pop_node.right:
                    queue.append(pop_node.right)
            result.append(level)
        return result

    def height(self, node: Node, height=0):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1


if __name__ == "__main__":
    root = Node(
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

    btree = BinaryTree(root)
    # btree.traverse(TraversalType.INORDER)
    # print()
    # btree.traverse(TraversalType.PREORDER)
    # print()
    # btree.traverse(TraversalType.POSTORDER)
    # btree.traverse(TraversalType.LEVELORDER)
    print(btree.height(root))
