from copy import copy, deepcopy
from typing import Any, Optional, Union


class Node:
    def __init__(self, info: Any, next: Optional["Node"] = None):
        self.info = info
        self.next = next

    def __str__(self):
        return f"Node({self.info},{self.next})"


class DNode:
    def __init__(
        self, info: Any, next: Optional["Node"] = None, prev: Optional["Node"] = None
    ):
        self.info = info
        self.next = next
        self.prev = prev

    def __str__(self):
        prev = self.prev and self.prev.info
        next = self.next and self.next.info
        return f"DNode({prev},{self.info},{next})"


class LinkedList:
    head: Union[Node, None] = None

    def __init__(self):
        pass

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            tail = self.get_tail()
            node = Node(value)
            tail.next = node

    def pop(self, index=None):
        if self.head is None:
            return None

        elif self.head.next is None:
            popped = self.head
            self.head = None
            return popped

        current = self.head
        while current.next.next is not None:
            current = current.next
        popped = current.next
        current.next = None
        return popped

    def index(self, value):
        index, value = self.__find(value)
        return index

    def find_node(self, value):
        index, value = self.__find(value)
        return value

    def __find(self, value):
        i = 0
        current = self.head
        while current is not None:
            if current.info == value:
                return i, current
            else:
                i += 1

            current = current.next
        return -1, None

    def get_tail(self):
        current = self.head
        while current.next is not None:
            current = current.next
        return current

    def __str__(self):
        repr = "Linked List: "
        current = self.head
        while current.next is not None:
            repr += f"{current.info}->"
            current = current.next
        repr += str(current.info)
        return repr

    def __len__(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length


class DLinkedList:
    head: Union[DNode, None] = None
    tail: Union[DNode, None] = None

    def __init__(self):
        pass

    def append(self, value):
        if self.head is None:
            self.head = DNode(value)
            self.tail = self.head
        else:
            node = DNode(value)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def pop(self, index=None):
        if self.head is None:
            return None

        elif len(self) == 1:
            popped = self.head
            self.head = None
            return popped

        if index == len(self) - 1 or index is None:
            popped = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            if index == 0:
                popped = self.head
                self.head = self.head.next
                self.head.prev = None
                return popped

            count = 0
            current = self.head
            while count != index:
                count += 1
                current = current.next

            current.prev.next = current.next
            current.next.prev = current.prev
            popped = current
            current = None

        return popped

    def index(self, value):
        index, value = self.__find(value)
        return index

    def find_node(self, value):
        index, value = self.__find(value)
        return value

    def reverse(self) -> "DLinkedList":
        dlist = deepcopy(self)
        current = dlist.head

        while current.next is not None:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp

        current.next = current.prev
        current.prev = None

        dlist.tail = dlist.head
        dlist.head = current

        return dlist

    def __find(self, value):
        i = 0
        current = self.head
        while current is not None:
            if current.info == value:
                return i, current
            else:
                i += 1

            current = current.next
        return -1, None

    def __str__(self):
        repr = "Doubly Linked List: "
        current = self.head
        while current.next is not None:
            repr += f"{current.info}->"
            current = current.next
        repr += str(current.info)
        return repr

    def __len__(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length


if __name__ == "__main__":
    list = LinkedList()
    list.append(2)
    list.append(4)
    list.append(8)

    dlist = DLinkedList()
    dlist.append(2)
    dlist.append(4)
    dlist.append(8)
    # print(len(dlist))
    # dlist.pop(2)
    print(dlist.reverse())
    # print(len(list))
    # print(dlist.index(20))
