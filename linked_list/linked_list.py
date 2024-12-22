from typing import Any, Optional, Union


class Node:
    def __init__(self, info: Any, next: Optional["Node"] = None):
        self.info = info
        self.next = next

    def __str__(self):
        return f"Node({self.info},{self.next})"


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


if __name__ == "__main__":
    list = LinkedList()
    list.append(2)
    list.append(4)
    list.append(8)
    # print(list)
    # print(len(list))
    print(list.index(20))
